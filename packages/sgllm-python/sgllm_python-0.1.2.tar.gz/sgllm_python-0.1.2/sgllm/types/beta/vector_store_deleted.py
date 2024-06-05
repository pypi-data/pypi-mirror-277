
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VectorStoreDeleted"]


class VectorStoreDeleted(BaseModel):
    id: str

    deleted: bool

    object: Literal["vector_store.deleted"]
