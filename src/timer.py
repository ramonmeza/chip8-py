from component import Component


class Timer(Component):

    # variable declarions
    _value: int

    # methods
    def __init__(self, rate: int) -> None:
        Component.__init__(self, rate)
        self._time_elapsed = 0.0
        self._value = 0

    def set_value(self, value: int) -> None:
        self._value = value

    def get_value(self) -> int:
        return self._value

    def tick(self) -> None:
        self._value -= 1
