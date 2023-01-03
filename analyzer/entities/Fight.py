from dataclasses import dataclass


@dataclass(kw_only=True)
class Fight:
    """ Represents a single fight report """
    id: int
    name: str
    report_code: str
    difficulty: int
    encounter_id: int
    kill: bool
    boss_percentage: float
    players: list[int]
    start_time: int
    end_time: int
