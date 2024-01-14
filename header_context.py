# MIT License
#
# Copyright (c) 2023 Clément RAOUL
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

"""Module to add header (LICENSE) to all python files"""

import os

DIRECTORY_PATH = "."


# Read header from file
def read_header() -> str:
    """
    Read header from file

    Returns:
        str: header
    """
    with open("LICENSE", "r", encoding="utf-8") as file:
        header = file.readlines()
        header = "".join(f"# {line}" for line in header)
    return header


def header_present(file_path: str, header: str) -> bool:
    """
    Check if header is present in file

    Args:
        file_path (str): file path
        header (str): header

    Returns:
        bool: True if header is present, False otherwise
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read(len(header))
    return header.replace(" ", "") in content.replace(" ", "")


def add_header(header: str) -> None:
    """
    Add header to file
    """
    for dirpath, _, filenames in os.walk(DIRECTORY_PATH):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)

                if not header_present(file_path, header):
                    with open(file_path, "r+", encoding="utf-8") as file:
                        content = file.read()
                        file.seek(0, 0)
                        file.write(header.rstrip("\r\n") + "\n\n" + content)


if __name__ == "__main__":
    HEADER = read_header()
    add_header(HEADER)
