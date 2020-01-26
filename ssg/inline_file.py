from typing import List, Callable

from ssg.file_source import FileSource
from ssg.filter import Filter
from ssg.plugin import Plugin


class InlineFileFilter(Filter):
    file_source: FileSource

    def __init__(self, file_source: FileSource):
        self.file_source = file_source

    def get_name(self) -> str:
        return "inline_file"

    def get_callable(self) -> Callable:
        return lambda file: self.file_source.read(file)


class InlineFilePlugin(Plugin):
    file_source: FileSource

    def __init__(self, file_source: FileSource):
        self.file_source = file_source

    def get_template_filters(self) -> List[Filter]:
        return [
            InlineFileFilter(
                self.file_source
            )
        ]


def create_plugin(file_source: FileSource):
    return InlineFilePlugin(file_source)

