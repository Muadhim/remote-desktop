# shared/protocol.py
from dataclasses import dataclass

@dataclass
class Message:
    type: str
    data: str
