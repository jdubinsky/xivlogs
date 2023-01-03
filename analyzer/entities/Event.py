from dataclasses import dataclass


@dataclass(kw_only=True)
class Event:
    ability: int
    source_id: int
    fight_id: int
    auras: list[dict]
    type: str
    timestamp: int
