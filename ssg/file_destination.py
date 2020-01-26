from abc import ABC, abstractmethod
from typing import AnyStr, List


class FileDestination(ABC):
    @abstractmethod
    def enumerate(self) -> List[AnyStr]:
        """
        Enumerate all files at the destination.
        :return: a list of present files at the destination
        """

    @abstractmethod
    def create(self, file_name: AnyStr, content: AnyStr) -> None:
        """
        Create file with the given content
        :param file_name: file name relative to the project directory, starting with /
        :param content: the content of the file
        """
        pass

    @abstractmethod
    def delete(self, file_name: AnyStr) -> None:
        """
        Remove a file from the destination.
        :param file_name: file name relative to the project directory, starting with /
        :return:
        """
        pass
