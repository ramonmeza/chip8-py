import abc


class Component(abc.ABC):

    # variable declarations
    _rate: int
    _time_elapsed: float


    # methods
    def __init__(self, rate: int) -> None:
        self._rate = rate
        self._time_elapsed = 0.0

    def update(self, dt: float) -> None:
        ms: float = (1 / self._rate)
        if self._time_elapsed >= ms:
            self._time_elapsed -= ms
            self.tick()
    
    @abc.abstractmethod
    def tick(self) -> None:
        pass
