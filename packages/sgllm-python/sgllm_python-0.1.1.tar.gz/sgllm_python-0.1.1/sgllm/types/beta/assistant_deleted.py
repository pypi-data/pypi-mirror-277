
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AssistantDeleted"]


class AssistantDeleted(BaseModel):
    id: str

    deleted: bool

    object: Literal["assistant.deleted"]
