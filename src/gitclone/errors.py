"""Error types for Git clone system."""

from enum import Enum
from typing import Optional


class ErrorType(Enum):
    """Categories of errors."""

    REPOSITORY_ERROR = "Repository Error"
    OBJECT_ERROR = "Object Error"
    FILE_SYSTEM_ERROR = "File System Error"
    USER_INPUT_ERROR = "User Input Error"


class GitError(Exception):
    """Base exception for Git clone errors."""

    def __init__(
        self,
        error_type: ErrorType,
        message: str,
        cause: Optional[Exception] = None,
    ) -> None:
        self.error_type = error_type
        self.message = message
        self.cause = cause
        super().__init__(f"{error_type.value}: {message}")
