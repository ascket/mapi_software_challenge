"""Concatenates the path to the file in the correct format"""

import os
from typing import List, Union


def get_path(dir_name: Union[str, object], fd_name: List[str]):
    return os.path.join(dir_name, *fd_name)
