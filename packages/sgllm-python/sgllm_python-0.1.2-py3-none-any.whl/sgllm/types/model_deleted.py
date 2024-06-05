


from .._models import BaseModel

__all__ = ["ModelDeleted"]


class ModelDeleted(BaseModel):
    id: str

    deleted: bool

    object: str
