from enum import Enum


class CopyResponse400Status(str, Enum):
    FAILURE = "failure"

    def __str__(self) -> str:
        return str(self.value)
