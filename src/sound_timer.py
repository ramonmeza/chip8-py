from sound import Sound
from timer import Timer


class SoundTimer(Timer):

    # variable declarations
    _sound: Sound


    # methods
    def __init__(self, rate: int) -> None:
        super().__init__(rate)
        self._sound = Sound()

    def set_value(self, value: int) -> None:
        super().set_value(value)

    def tick(self) -> None:
        if self.get_value() > 0 and not self._sound.is_playing():
            self._sound.play()
        elif self.get_value() <= 0 and self._sound.is_playing():
            self._sound.stop()
