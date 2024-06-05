
from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TextContentBlockParam"]


class TextContentBlockParam(TypedDict, total=False):
    text: Required[str]
    """Text content to be sent to the model"""

    type: Required[Literal["text"]]
    """Always `text`."""
