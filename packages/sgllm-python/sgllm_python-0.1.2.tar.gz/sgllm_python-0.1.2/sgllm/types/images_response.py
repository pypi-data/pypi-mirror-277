
from typing import List

from .image import Image
from .._models import BaseModel

__all__ = ["ImagesResponse"]


class ImagesResponse(BaseModel):
    created: int

    data: List[Image]
