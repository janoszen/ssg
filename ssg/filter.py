import abc
from typing import Callable


class Filter(abc.ABC):
    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_callable(self) -> Callable:
        pass

