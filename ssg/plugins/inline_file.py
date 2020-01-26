from typing import List, Callable

from ssg.source import Source
from ssg.filter import Filter
from ssg.plugin import Plugin


class InlineFileFilter(Filter):
    file_source: Source

    def __init__(self, file_source: Source):
        self.file_source = file_source

    def get_name(self) -> str:
        return "inline_file"

    def get_callable(self) -> Callable:
        return lambda file: self.file_source.read_file_as_string(file)


class InlineFilePlugin(Plugin):
    file_source: Source

    def __init__(self, file_source: Source):
        self.file_source = file_source

    def get_template_filters(self) -> List[Filter]:
        return [
            InlineFileFilter(
                self.file_source
            )
        ]


def create_plugin(file_source: Source):
    return InlineFilePlugin(file_source)
