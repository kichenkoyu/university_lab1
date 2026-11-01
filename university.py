from dataclasses import dataclass
from typing import List
from faculty import Faculty

@dataclass
class University:
    name: str
    faculties: List[Faculty]