import os
import shutil
import uuid
import logging
import argparse
from .tools.os import mkdir
import warnings
import sys


class UnknownArgs:
    def __init__(self, args):
        self.args_dict = {}
        for arg in args:
            if arg.startswith("--"):
                key, value = arg[2:].split("=")
                self.args_dict[key] = value

    def __getattr__(self, item):
        return self.args_dict.get(item)

    def __getitem__(self, item):
        return self.args_dict.get(item)

    def __str__(self):
        return str(self.args_dict)


class StreamToLogger:
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """

    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ""

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        pass


class ETL:
    def __init__(
        self,
        name=None,
        datasets_dir=None,
        inventory_dir=None,
        output_dir=None,
        is_logs=False,
    ) -> None:
        parser = argparse.ArgumentParser(description="Base ETL")
        parser.add_argument("-n", "--name", required=False)

        parser.add_argument(
            "-l",
            "--logs",
            action="store_true",
            help="Enable logging",
            required=False,
            default=False,
        )
        parser.add_argument("-o", "--output_dir", required=False, default="dist")
        parser.add_argument("-i", "--inventory_dir", required=False)
        parser.add_argument("-d", "--datasets_dir", required=False)
        args, unknown_args = parser.parse_known_args()

        self.name = args.name
        self.output_dir = args.output_dir
        self.root_output_dir = self.output_dir
        self.inventory_dir = args.inventory_dir
        self.datasets_dir = args.datasets_dir
        self.is_logs = args.logs

        if name is not None:
            self.name = name

        if datasets_dir is not None:
            self.datasets_dir = datasets_dir

        if inventory_dir is not None:
            self.inventory_dir = inventory_dir

        if output_dir is not None:
            self.output_dir = output_dir

        if is_logs:
            self.is_logs = True

        self.args = UnknownArgs(unknown_args)

    def log_warning(self, message, category, filename, lineno, file=None, line=None):
        self.logger.warning(
            f"{category.__name__}: {message} (from {filename}:{lineno})"
        )

    def __enter__(self):
        self.nameunique = f"{self.name}"
        self.output_dir = f"{self.output_dir}/_{self.nameunique}"

        # Create or get the logger
        logging.captureWarnings(True)
        warnings.simplefilter("always")
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )

        if not self.logger.hasHandlers():
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
            for handler in self.logger.handlers:
                handler.setFormatter(formatter)

        if self.is_logs and self.name is not None:
            # Create handler for logging to a file
            log_file_path = self.get_save_filepath(".log")
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        # Capture warnings

        # Redirect stdout and stderr
        # warnings.showwarning = self.log_warning  # Override showwarning to log warnings

        # sys.stdout = StreamToLogger(self.logger, logging.INFO)
        # sys.stderr = StreamToLogger(self.logger, logging.ERROR)

        # Hook to capture uncaught exceptions
        # sys.excepthook = self.handle_exception

        # warnings.showwarning = self.log_warning  # Override showwarning to log warnings

        return self

        # if self.logger.hasHandlers():
        #     # If the logger has handlers, reset their format
        #     for handler in self.logger.handlers:
        #         handler.setFormatter(formatter)
        # else:
        # If no handlers exist, create new handlers
        # Create handler for console output

        # # สร้าง logger
        # self.logger = logging.getLogger(f"{self.name}_logger")
        # self.logger.setLevel(logging.INFO)

        # if not self.logger.hasHandlers():
        #     # Create handler for console output
        #     console_handler = logging.StreamHandler()
        #     console_handler.setLevel(logging.INFO)

        #     # Add the console handler to the logger
        #     self.logger.addHandler(console_handler)
        #     # Create formatter and add it to both handlers
        #     formatter = logging.Formatter(
        #         "%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        #     )
        #     console_handler.setFormatter(formatter)

        #     if self.is_logs and self.name is not None:
        #         # Create handler for logging to a file
        #         file_handler = logging.FileHandler(
        #             mkdir(f"{self.output_dir}/{self.name}.log")
        #         )
        #         file_handler.setLevel(logging.INFO)

        #         file_handler.setFormatter(formatter)

        #         # Add the file handler to the logger
        #         self.logger.addHandler(file_handler)

        # return self

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            # Call the default excepthook saved at sys.__excepthook__
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        self.logger.error(
            "Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback)
        )

    def log_warning(self, message, category, filename, lineno, file=None, line=None):
        self.logger.warning(
            f"{category.__name__}: {message} (from {filename}:{lineno})"
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        if os.path.exists(self.output_dir):
            # เปลี่ยนชื่อโฟลเดอร์
            to_dir = self.output_dir.replace(f"_{self.nameunique}", self.nameunique)
            if os.path.exists(to_dir):
                tmp_dir = f"{self.root_output_dir}/.tmp/{self.name}/{uuid.uuid4()}"
                self.logger.info(f"Move existing file to: {tmp_dir}")
                shutil.move(
                    to_dir,
                    tmp_dir,
                    copy_function=shutil.copy2,
                )
            shutil.move(
                self.output_dir,
                to_dir,
                copy_function=shutil.copy2,
            )

            self.logger.info(f"Created : {to_dir}")

    def get_save_filepath(self, extension):
        filepath = f"{self.output_dir}/{self.name}{extension}"
        if not os.path.exists(self.output_dir):
            return mkdir(filename=filepath)

        return filepath
