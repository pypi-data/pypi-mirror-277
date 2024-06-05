
from __future__ import annotations

from typing import Union
from typing_extensions import Literal

from .assistant_tool_choice_param import AssistantToolChoiceParam

__all__ = ["AssistantToolChoiceOptionParam"]

AssistantToolChoiceOptionParam = Union[Literal["none", "auto", "required"], AssistantToolChoiceParam]
