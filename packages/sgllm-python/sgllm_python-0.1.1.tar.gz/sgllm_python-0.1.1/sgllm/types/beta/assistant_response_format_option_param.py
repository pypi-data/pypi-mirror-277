
from __future__ import annotations

from typing import Union
from typing_extensions import Literal

from .assistant_response_format_param import AssistantResponseFormatParam

__all__ = ["AssistantResponseFormatOptionParam"]

AssistantResponseFormatOptionParam = Union[Literal["none", "auto"], AssistantResponseFormatParam]
