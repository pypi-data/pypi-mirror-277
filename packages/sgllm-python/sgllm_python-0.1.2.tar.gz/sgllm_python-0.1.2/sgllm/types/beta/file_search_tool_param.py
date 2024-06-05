
from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FileSearchToolParam"]


class FileSearchToolParam(TypedDict, total=False):
    type: Required[Literal["file_search"]]
    """The type of tool being defined: `file_search`"""
