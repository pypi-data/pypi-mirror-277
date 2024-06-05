
from typing_extensions import Literal

__all__ = ["RunStatus"]

RunStatus = Literal[
    "queued",
    "in_progress",
    "requires_action",
    "cancelling",
    "cancelled",
    "failed",
    "completed",
    "incomplete",
    "expired",
]
