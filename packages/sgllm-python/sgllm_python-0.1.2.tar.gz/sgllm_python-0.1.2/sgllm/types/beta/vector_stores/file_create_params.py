
from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """
    A [File](https://platform.sgllm.com/docs/api-reference/files) ID that the
    vector store should use. Useful for tools like `file_search` that can access
    files.
    """
