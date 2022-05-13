from sound import Sound
from timer import Timer


class SoundTimer(Timer):

    # variable declarations
    _sound: Sound


    # methods
    def __init__(self, rate: int) -> None:
        super().__init__(rate)

    def set_value(self, value: int) -> None:
        super().set_value(value)

        if value > 0:
            self._sound.start()

    def update(self, dt: float) -> None:
        super.update(dt)
        if self.get_value() <= 0:
            self._sound.stop()
