
from typing import Union
from typing_extensions import Annotated

from ...._utils import PropertyInfo
from .text_content_block import TextContentBlock
from .image_url_content_block import ImageURLContentBlock
from .image_file_content_block import ImageFileContentBlock

__all__ = ["MessageContent"]

MessageContent = Annotated[
    Union[ImageFileContentBlock, ImageURLContentBlock, TextContentBlock], PropertyInfo(discriminator="type")
]
