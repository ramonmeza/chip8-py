from audioop import add
from typing import Array


class Memory:

    # variable declarations
    _bytes: Array[int]


    # methods
    def __init__(self, amount: int) -> None:
        self.clear()

    def clear(self) -> None:
        self._bytes =  [0] * 4096

    def set(self, address: int, value: int) -> None:
        self._bytes[address] = value

    def get(self, address: int) -> int:
        return self._bytes[address]
