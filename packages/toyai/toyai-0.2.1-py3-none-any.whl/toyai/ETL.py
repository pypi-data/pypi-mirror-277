import os
import shutil
import uuid
import logging
import argparse
from .tools.os import mkdir
import sys
from abc import ABC, abstractmethod
import gc

from .Trainer import Trainer


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

    def update(self, new_args: dict[str, any]):
        if new_args:
            for key, value in new_args.items():
                self.args_dict[key] = value


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


class ETL(ABC):
    @abstractmethod
    def extract(self, input_dir) -> dict[str, any]:
        pass

    @abstractmethod
    def transform(self, data: dict[str, any]) -> dict[str, any]:
        data = None
        return data

    @abstractmethod
    def load(self, trainer: Trainer, results: dict[str, any]):
        pass

    def __init__(
        self,
        name=None,
        input_dir=None,
        output_dir=None,
        is_logs=False,
        log_level=logging.INFO,
        args: dict[str, any] = None,
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
        parser.add_argument("-i", "--input_dir", required=False, default="data")
        argv, unknown_args = parser.parse_known_args()

        self.name = argv.name
        self.output_dir = argv.output_dir
        self.root_output_dir = self.output_dir
        self.input_dir = argv.input_dir
        self.is_logs = argv.logs
        self.log_level = log_level

        if name is not None:
            self.name = name

        if input_dir is not None:
            self.input_dir = input_dir

        if output_dir is not None:
            self.output_dir = output_dir

        if is_logs:
            self.is_logs = True

        self.args = UnknownArgs(unknown_args)
        if args is not None:
            self.args.update(args)

    # def log_warning(self, message, category, filename, lineno, file=None, line=None):
    #     self.logger.info(f"{category.__name__}: {message} (from {filename}:{lineno})")

    def handle_exception_thread(self, args):
        self.logger.info(
            "Uncaught thread exception",
            exc_info=(args.exc_type, args.exc_value, args.exc_traceback),
        )

    def __enter__(self):
        if self.name is None or self.name is "":
            raise Exception("ETL name cannot be empty.")
        self.nameunique = f"{self.name}"
        self.output_dir = f"{self.output_dir}/_{self.nameunique}"

        # Create or get the logger
        logging.captureWarnings(True)
        self.logger = logging.getLogger()
        self.logger.setLevel(self.log_level)

        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s|%(levelname)s|%(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )

        if not self.logger.hasHandlers():
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.log_level)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
            for handler in self.logger.handlers:
                handler.setFormatter(formatter)

        if self.is_logs and self.name is not None:
            # Create handler for logging to a file
            log_file_path = self.get_save_filepath(".log")
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setLevel(self.log_level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        # sys.excepthook = self.handle_exception
        # threading.excepthook = self.handle_exception_thread

        return self

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            # Call the default excepthook saved at sys.__excepthook__
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        self.logger.error(
            "Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback)
        )

    def setattr(self, name: str, value: any) -> None:
        super.__setattr__(name, value)

    def getattr(self, name: str) -> any:
        return super.__getattribute__(name)

    def train(self, trainer_class, epochs: int):
        try:
            trainer = trainer_class(args=self.args, logger=self.logger)

            self.logger.info("#extract")
            data = self.extract(self.input_dir)

            self.logger.info("#transform")
            data = self.transform(data)

            self.logger.info("#train")
            results = trainer.train(epochs=epochs, data=data)

            self.logger.info("#load")
            self.load(trainer, results)
        except Exception as e:
            # self.logger.error(e)
            raise Exception(e)

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type is not None:
            self.logger.error(
                "Exiting with error", exc_info=(exc_type, exc_val, exc_tb)
            )
        else:
            self.logger.info("Exiting ETL.")
        if os.path.exists(self.output_dir):
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
            gc.collect()

    def get_save_filepath(self, extension):
        filepath = f"{self.output_dir}/{self.name}{extension}"
        if not os.path.exists(self.output_dir):
            return mkdir(filename=filepath)

        return filepath
