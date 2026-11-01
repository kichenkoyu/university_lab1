from dataclasses import dataclass
from typing import List
from department import Department

@dataclass
class Faculty:
    name: str
    departments: List[Department]