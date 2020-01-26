from typing import List, AnyStr


class Source:
    def enumerate_files(self):
        raise NotImplementedError

    def read_file_as_string(self, path):
        raise NotImplementedError
