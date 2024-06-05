
from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AssistantResponseFormatParam"]


class AssistantResponseFormatParam(TypedDict, total=False):
    type: Literal["text", "json_object"]
    """Must be one of `text` or `json_object`."""
