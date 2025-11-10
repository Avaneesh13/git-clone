"""Core abstract base classes for the Git clone system."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional


class ObjectType(Enum):
    """Types of objects in the object database."""

    BLOB = "blob"
    TREE = "tree"
    COMMIT = "commit"


@dataclass
class IndexEntry:
    """Entry in the staging index."""

    path: str
    hash: str
    mode: str
    size: int
    mod_time: datetime


class Storage(ABC):
    """Abstract interface for object storage."""

    @abstractmethod
    def store(self, content: bytes, obj_type: ObjectType) -> str:
        """Store content and return its hash."""
        pass

    @abstractmethod
    def retrieve(self, hash: str) -> bytes:
        """Retrieve content by hash."""
        pass

    @abstractmethod
    def exists(self, hash: str) -> bool:
        """Check if object exists."""
        pass


class Index(ABC):
    """Abstract interface for staging index."""

    @abstractmethod
    def add(self, filepath: str) -> None:
        """Add file to staging area."""
        pass

    @abstractmethod
    def remove(self, filepath: str) -> None:
        """Remove file from staging area."""
        pass

    @abstractmethod
    def get_entries(self) -> List[IndexEntry]:
        """Get all staged entries."""
        pass

    @abstractmethod
    def write(self) -> None:
        """Write index to disk."""
        pass

    @abstractmethod
    def read(self) -> None:
        """Read index from disk."""
        pass

    @abstractmethod
    def clear(self) -> None:
        """Clear all entries from index."""
        pass


class Repository(ABC):
    """Abstract interface for repository operations."""

    @abstractmethod
    def init(self, path: str) -> None:
        """Initialize a new repository."""
        pass

    @abstractmethod
    def get_object(self, hash: str) -> bytes:
        """Get object by hash."""
        pass

    @abstractmethod
    def store_object(self, content: bytes, obj_type: ObjectType) -> str:
        """Store object and return hash."""
        pass

    @abstractmethod
    def get_head(self) -> Optional[str]:
        """Get current HEAD commit hash."""
        pass

    @abstractmethod
    def set_head(self, hash: str) -> None:
        """Set HEAD to commit hash."""
        pass
