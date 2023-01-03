from dataclasses import dataclass

@dataclass(kw_only=True)
class Player:
    id: int
    name: str
    server: str
    type: str
    role: str
