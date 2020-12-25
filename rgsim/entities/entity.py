"""Base class for all game entities"""

from __future__ import annotations

from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass(frozen=True)
class _Entity:
    uid: int = field(init=False)


class Entity(_Entity, ABC):
    """Base class for all game entities"""
    _next_uid: ClassVar[int] = 0

    uid: int = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, 'uid', Entity._next_uid)
        Entity._next_uid += 1

    @property
    @abstractmethod
    def name(self) -> str:
        """A name for this entity"""
