
from typing_extensions import Literal

from .image_url import ImageURL
from ...._models import BaseModel

__all__ = ["ImageURLContentBlock"]


class ImageURLContentBlock(BaseModel):
    image_url: ImageURL

    type: Literal["image_url"]
    """The type of the content part."""
