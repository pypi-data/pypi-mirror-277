from abc import ABC, abstractmethod
from logging import Logger


class Trainer(ABC):

    model = None

    def __init__(
        self,
        args: dict[str, any] = None,
        logger: Logger = None,
    ) -> None:
        self.args = args
        self.logger = logger

    @abstractmethod
    def train(
        self,
        epochs: int,
        data: dict[str, any],
    ) -> dict[str, any]:
        pass
