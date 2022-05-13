from typing import List


class Memory:

    # variable declarations
    _bytes: List[int]


    # methods
    def __init__(self, amount: int) -> None:
        self.clear()

    def clear(self) -> None:
        self._bytes =  [0] * 4096

    def set(self, address: int, value: int) -> None:
        self._bytes[address] = value

    def get(self, address: int) -> int:
        return self._bytes[address]

    def copy(self, offset: int, data: List[int]) -> None:
        for byte in data:
            self.set(offset, byte)
            offset += 1

    def draw_sprite(self, sprite: List[int]) -> None:
        pass
