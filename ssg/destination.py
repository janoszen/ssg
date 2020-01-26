from typing import AnyStr, List


class Destination:
    def enumerate_files(self):
        raise NotImplementedError

    def ensure_file(self, file_name, content):
        raise NotImplementedError

    def delete_file(self, file_name):
        raise NotImplementedError
