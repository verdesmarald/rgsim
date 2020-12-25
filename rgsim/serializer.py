import base64
import struct
import zlib

from dataclasses import dataclass
from typing import Iterable, List, Type, cast

from pyamf import sol #type: ignore

from .simulator import GameState


@dataclass
class Record:
    @staticmethod
    def signature() -> str:
        """Signature to deserialize this record type with struct.unpack"""
        raise NotImplementedError()

    @staticmethod
    def length() -> int:
        """Length (in bytes) of serialized record"""
        raise NotImplementedError()


@dataclass
class Header(Record):
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


@dataclass
class Building(Record):
    id_: int
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


@dataclass
class Upgrade(Record):
    id_: int
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


@dataclass
class Trophy(Record):
    id_: int
    u1: bool
    u2: int

    @staticmethod
    def signature() -> str:
        return '>I?B'

    @staticmethod
    def length() -> int:
        return 6


@dataclass
class Spell(Record):
    id_: int
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


@dataclass
class CurrentGame(Record):
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


@dataclass
class FactionCoin(Record):
    coins: float
    exchanges: int

    @staticmethod
    def signature() -> str:
        return '>dI'

    @staticmethod
    def length() -> int:
        return 12


@dataclass
class EventResource(Record):
    resource: float

    @staticmethod
    def signature() -> str:
        return '>d'

    @staticmethod
    def length() -> int:
        return 8


@dataclass
class Statistic(Record):
    stat: float
    r_stat: float
    t_stat: float

    @staticmethod
    def signature() -> str:
        return '>3d'

    @staticmethod
    def length() -> int:
        return 24


@dataclass
class Lineage(Record):
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

        # print(header)
        # print(buildings)
        # print(upgrades)
        # print(trophies)
        # print(artifact_rng_state)
        # print(spells)
        # print(current_game)
        # print(faction_coins)
        # print(event_resources)
        # print(stats)
        # print(lineages)

        upgrades = cast(List[Upgrade], list(upgrades))
        upgrades.sort(key=lambda u: u.id_)
        i = 0
        for upgrade in upgrades:
            if upgrade.u1 or upgrade.u2 or upgrade.u3:
                print(f'{i:3d}: {upgrade}')
                i += 1

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


SAVE_FILE = 'C:/Users/James/AppData/Roaming/com.kongregate.mobile.realmgrinder.air/Local Store/#SharedObjects/RealmGrinderDesktop.swf/realm-grinder.sol'
Serializer.deserialize(sol.load(SAVE_FILE)['save'])
