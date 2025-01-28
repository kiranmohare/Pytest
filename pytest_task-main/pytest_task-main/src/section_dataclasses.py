from dataclasses import dataclass
from typing import List, Optional


@dataclass()
class Person:
    name: str
    age: int
    hobbies: List[str]
    nickname: Optional[str] = None
