class Timer:

    # variable declarions
    _rate: int
    _time_elapsed: float
    _value: int

    # methods
    def __init__(self, rate: int) -> None:
        self._rate = rate
        self._time_elapsed = 0.0
        self._value = 0

    def set_value(self, value: int) -> None:
        self._value = value

    def get_value(self) -> int:
        return self._value

    def update(self, dt: float) -> None:
        self._time_elapsed += dt
        if self._time_elapsed >= (1 / self._rate):
            self._time_elapsed -= (1 / self._rate)
            self._value -= 1
