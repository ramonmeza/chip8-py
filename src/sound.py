class Sound:

    # variable declarations
    _is_playing: bool


    # methods
    def __init__(self) -> None:
        self._is_playing = False

    def play(self) -> None:
        self._is_playing = True

    def stop(self) -> None:
        self._is_playing = False

    def is_playing(self) -> bool:
        return self._is_playing
