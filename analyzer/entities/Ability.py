from dataclasses import dataclass

@dataclass(kw_only=True)
class Ability:
    id: int
    name: str
    description: str
