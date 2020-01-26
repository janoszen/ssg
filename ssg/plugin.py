from typing import List

from ssg.filter import Filter
from ssg.ssg import FileProcessor, Source


class Plugin:
    def get_template_filters(self) -> List[Filter]:
        return []

    def get_file_processors(self) -> List[FileProcessor]:
        return []


def load_plugin(
        package_name: str,
        file_source: Source
) -> Plugin:
    package = __import__(package_name)
    if package.create_plugin:
        return package.create_plugin(file_source)
    else:
        raise Exception("create_plugin function not found in package " + package + ", not a valid plugin.")
