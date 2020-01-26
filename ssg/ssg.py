import abc
import os
import pathlib
import shutil
from typing import AnyStr

from ssg.file_source import FileSource

src_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "src")
dist_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dist")

class FileProcessor:
    def process(self, filename: str, file_source: FileSource):
        pass


if __name__ == "__main__":
    for root, dirs, files in os.walk(src_path):
        for file in files:
            file_src_path = os.path.join(root, file)
            file_dist_path = file_src_path.replace(src_path, dist_path)
            file_dirs_dir = os.path.dirname(file_dist_path)
            pathlib.Path(file_dirs_dir).mkdir(parents=True, exist_ok=True)
            # todo handle case when one of the parent directories is a file
            if '.html' in file or '.xml' in file:
                env = Environment(autoescape=True, loader=FileSystemLoader(src_path))
                env.filters['inline_file'] = inline_file
                template = env.get_template(file_src_path.replace(src_path + os.path.sep, ""))
                content = template.render()
                with open(file_dist_path, "w") as f:
                    f.write(content)
            elif '.scss' in file:
                if not file.startswith("_"):
                    with open(file_dist_path.replace(".scss", ".css"), "w") as f:
                        f.write(parser.load(file_src_path))
            else:
                shutil.copyfile(file_src_path, file_dist_path)
    for root, dirs, files in os.walk(dist_path):
        for file in files:
            file_dist_path = os.path.join(root, file)
            file_src_path = file_dist_path.replace(dist_path, src_path)
            if not os.path.exists(file_src_path):
                os.remove(file_dist_path)
