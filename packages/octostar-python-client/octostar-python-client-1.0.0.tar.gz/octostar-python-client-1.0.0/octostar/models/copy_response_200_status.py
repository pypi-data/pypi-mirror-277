from enum import Enum


class CopyResponse200Status(str, Enum):
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
