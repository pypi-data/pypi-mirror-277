
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileSearchTool"]


class FileSearchTool(BaseModel):
    type: Literal["file_search"]
    """The type of tool being defined: `file_search`"""
