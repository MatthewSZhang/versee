"""WeDevote Bible webpages scraper"""

from ._debug import _print_etree
from ._file import write_file
from ._web import web

__all__ = [
    "write_file",
    "web",
    "_print_etree",
]
