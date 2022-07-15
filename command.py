from dataclasses import dataclass
from typing import List

@dataclass
class Command(object):
    command: str
    arguments: List[str]