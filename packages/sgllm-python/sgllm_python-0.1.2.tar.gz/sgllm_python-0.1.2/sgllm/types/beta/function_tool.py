
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.function_definition import FunctionDefinition

__all__ = ["FunctionTool"]


class FunctionTool(BaseModel):
    function: FunctionDefinition

    type: Literal["function"]
    """The type of tool being defined: `function`"""
