from typing import Callable, List

from component import Component
from stack import Stack


class Cpu(Component):

    # constants
    NUM_OF_REGISTERS: int = 16


    # variable declarations
    _program_counter: int
    _registers: List[int]
    _get_memory: Callable
    _stack: Stack

    # methods
    def __init__(self, rate: int) -> None:
        Component.__init__(self, rate)
        self._program_counter = 0
        self._registers = [0] * Cpu.NUM_OF_REGISTERS
        self._get_memory = None
        self._stack = Stack()

    def register_memory(self, func: Callable) -> None:
        self._get_memory = func

    def set_program_counter(self, value: int) -> None:
        self._program_counter = value

    def tick(self) -> None:
        instruction: List[int] = self._fetch()
        self._decode()
        self._execute()

    def _fetch(self) -> List[int]:
        op_code: List[int] = list([
            self._get_memory(self._program_counter),
            self._get_memory(self._program_counter + 1)
        ])
        self._program_counter += 2
        return op_code

    def _decode(self) -> None:
        pass

    def _execute(self) -> None:
        pass
