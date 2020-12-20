import base64
import struct
import zlib

from typing import Iterable, NamedTuple, NamedTupleMeta, Type

from sim import GameState


class Record(NamedTuple):
    @staticmethod
    def signature() -> str:
        """Signature to deserialize this record type with struct.unpack"""
        raise NotImplementedError()

    @staticmethod
    def length() -> int:
        """Length (in bytes) of serialized record"""
        raise NotImplementedError()


class Header(Record, metaclass=NamedTupleMeta):
    save_version: int
    reserved: int
    play_fab_season: int
    season_number: int
    halloween_monsters: int
    breath_effects: int
    egg_rng_state: int
    egg_stack_size: int
    cta_faction_casts: int
    alignment_index: int
    checksum_index: int

    @staticmethod
    def signature() -> str:
        return '>6HI2H2I'

    @staticmethod
    def length() -> int:
        return 28


class Building(Record, metaclass=NamedTupleMeta):
    uid: int
    current_quantity: int
    r_built: float
    r_max_built: float
    t_built: float
    t_max_built: float
    reserved1: float
    reserved2: float
    reserved3: float
    reserved4: float
    reserved5: float
    reserved6: float

    @staticmethod
    def signature() -> str:
        return '>2I10d'

    @staticmethod
    def length() -> int:
        return 88


class Upgrade(Record, metaclass=NamedTupleMeta):
    uid: int
    u1: bool
    u2: bool
    u3: bool
    rng_state: int

    @staticmethod
    def signature() -> str:
        return '>I3?I'

    @staticmethod
    def length() -> int:
        return 11



class Trophy(Record, metaclass=NamedTupleMeta):
    uid: int
    u1: bool
    u2: int

    @staticmethod
    def signature() -> str:
        return '>I?B'

    @staticmethod
    def length() -> int:
        return 6


class Spell(Record, metaclass=NamedTupleMeta):
    uid: int
    active_ticks: int
    autocast: bool
    primary_autocast_priority: int
    secondary_autocast_priority: int
    independent_autocast_priority: int
    tiers: int
    active_tiers: int
    casts: float
    r_casts: float
    t_casts: float
    time_active: float
    r_time_active: float
    t_time_active: float
    spell_rng_state: int

    @staticmethod
    def signature() -> str:
        return '>Ii?4ib6dI'

    @staticmethod
    def length() -> int:
        return 78


class CurrentGame(Record, metaclass=NamedTupleMeta):
    alignment: int
    faction: int
    prestige_faction: int
    elite_prestige_faction: int
    gems: float
    reincarnation: int
    ascension: int
    secondary_alignment: int
    last_save: int
    mana: float
    coins: float
    rubies: float
    excavations: float

    @staticmethod
    def signature() -> str:
        return '>4bd2HbI4d'

    @staticmethod
    def length() -> int:
        return 53


class FactionCoin(Record, metaclass=NamedTupleMeta):
    coins: float
    exchanges: int

    @staticmethod
    def signature() -> str:
        return '>dI'

    @staticmethod
    def length() -> int:
        return 12


class EventResource(Record, metaclass=NamedTupleMeta):
    resource: float

    @staticmethod
    def signature() -> str:
        return '>d'

    @staticmethod
    def length() -> int:
        return 8


class Statistic(Record, metaclass=NamedTupleMeta):
    stat: float
    r_stat: float
    t_stat: float

    @staticmethod
    def signature() -> str:
        return '>3d'

    @staticmethod
    def length() -> int:
        return 24


class Lineage(Record, metaclass=NamedTupleMeta):
    level: float

    @staticmethod
    def signature() -> str:
        return '>d'

    @staticmethod
    def length() -> int:
        return 8


class Serializer:
    def __init__(self, save_data: str) -> None:
        self._raw = Serializer._get_bytes(save_data)
        self._pos = 0

    @staticmethod
    def deserialize(save_data: str) -> GameState:
        serializer = Serializer(save_data)

        header = serializer.read_one(Header)
        buildings = serializer.read_many(Building)
        upgrades = serializer.read_many(Upgrade)
        trophies = serializer.read_many(Trophy)
        [artifact_rng_state] = serializer.read('>I', 4)
        spells = serializer.read_many(Spell)
        current_game = serializer.read_one(CurrentGame)
        faction_coins = serializer.read_many(FactionCoin)
        event_resources = serializer.read_many(EventResource)
        stats = serializer.read_many(Statistic)
        lineages = serializer.read_many(Lineage)

        print(header)
        print(buildings)
        print(upgrades)
        print(trophies)
        print(artifact_rng_state)
        print(spells)
        print(current_game)
        print(faction_coins)
        print(event_resources)
        print(stats)
        print(lineages)

        return GameState()

    def consume(self, num_bytes: int) -> bytes:
        start = self._pos
        self._pos += num_bytes
        return self._raw[start:start + num_bytes]

    def read(self, signature: str, length: int) -> tuple:
        return struct.unpack(signature, self.consume(length))

    def read_one(self, record_type: Type[Record]) -> Record:
        return record_type(*self.read(record_type.signature(), record_type.length()))

    def read_many(self, record_type: Type[Record]) -> Iterable[Record]:
        [num_records] = self.read('>H', 2)
        records = []
        for _i in range(num_records):
            records.append(self.read_one(record_type))
        return records

    @staticmethod
    def _get_bytes(savedata: str) -> bytes:
        decoded = base64.b64decode(savedata[4:-2])
        decompressed = zlib.decompress(decoded, 15)

        key = b'therealmisalie'
        deciphered = b''
        for i, byte in enumerate(decompressed):
            deciphered += bytes([byte ^ key[i % len(key)]])

        return deciphered


DATA = "$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$e"
Serializer.deserialize(DATA)
