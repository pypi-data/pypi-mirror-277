


from ..._models import BaseModel

__all__ = ["AssistantToolChoiceFunction"]


class AssistantToolChoiceFunction(BaseModel):
    name: str
    """The name of the function to call."""
