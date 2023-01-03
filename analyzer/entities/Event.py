from dataclasses import dataclass
from typing import Optional, List, Dict


# TODO: make a separate event for each type
@dataclass(kw_only=True)
class Event:
    ability_game_id: Optional[int] = None
    extra_ability_game_id: Optional[int] = None
    amount: Optional[int] = None
    fight: Optional[int] = None
    ability: Optional[int] = None
    source_id: Optional[int] = None
    attacker_id: Optional[int] = None
    fight_id: Optional[int] = None
    hit_type: Optional[int] = None
    target_id: Optional[int] = None
    unmitigated_amount: Optional[int] = None
    mitigated: Optional[int] = None
    packet_id: Optional[int] = None
    duration: Optional[int] = None
    stack: Optional[int] = None
    extra_info: Optional[int] = None
    value: Optional[int] = None
    bars: Optional[int] = None
    target_instance: Optional[int] = None
    finalized_amount: Optional[float] = None
    direct_hit_percentage: Optional[int] = None
    absorbed: Optional[int] = None
    absorb: Optional[int] = None
    actor_potency_ratio: Optional[float] = None
    guess_amount: Optional[int] = None
    expected_amount: Optional[int] = None
    expected_crit_rate: Optional[int] = None
    bonus_percent: Optional[int] = None
    source_instance: Optional[int] = None
    overheal: Optional[int] = None
    multiplier: Optional[float] = None
    auras: Optional[List[Dict]] = None
    direct_hit: Optional[bool] = None
    simulated: Optional[bool] = None
    melee: Optional[bool] = None
    tick: Optional[bool] = None
    unpaired: Optional[bool] = None
    type: str
    timestamp: int
