
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["VectorStoreFileDeleted"]


class VectorStoreFileDeleted(BaseModel):
    id: str

    deleted: bool

    object: Literal["vector_store.file.deleted"]
