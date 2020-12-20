from abc import ABC, abstractmethod
from enum import Enum, auto

class Alignment(Enum):
    NEUTRAL = auto()
    GOOD = auto()
    EVIL = auto()


class Faction(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Name of faction"""

    @property
    @abstractmethod
    def alignment(self) -> Alignment:
        """Alignment of faction"""
