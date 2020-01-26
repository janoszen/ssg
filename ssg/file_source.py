from abc import abstractmethod, ABC
from typing import List, AnyStr


class FileSource(ABC):

    @abstractmethod
    def enumerate(self) -> List[AnyStr]:
        """
        Enumerate all files in the source.
        :return: a list of file paths starting with / relative to the project directory or virtual source root.
        """
        pass

    @abstractmethod
    def read(self, path: str) -> AnyStr:
        """
        Read a file specified by path from the file source and return it as a byte array.
        :param path: the path of the file, starting with a / from the project directory.
        :return: the contents of the file
        """
        pass
