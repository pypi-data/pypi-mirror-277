from enum import Enum


class ExportResponse400Status(str, Enum):
    FAILURE = "failure"

    def __str__(self) -> str:
        return str(self.value)
