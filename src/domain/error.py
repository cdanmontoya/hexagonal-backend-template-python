from dataclasses import dataclass


@dataclass(frozen=True)
class Error(Exception):
    message: str
