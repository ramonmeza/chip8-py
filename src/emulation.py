from dis import dis
import pygame as pyg

from pathlib import Path

from display import Display
from settings import Settings


class Emulation(pyg.Surface):
    '''
    Composes and manages the emulation and handles emulation-level events.
    '''

    # variable declarations
    _display: Display
    _time_since_last_frame: float


    # methods
    def __init__(self) -> None:
        # get settings
        settings: dict = Settings.load(Path('data/settings.json'), 'display')
        display_width: int = settings['width']
        display_height: int = settings['height']
        display_size: tuple = (display_width, display_height)

        # subclass init
        pyg.Surface.__init__(self, size=display_size)

        # initialize variables
        self._display = Display(display_width, display_height)
        self._time_since_last_frame = 0.0

    def update(self) -> None:
        # get delta time
        ticks: int = pyg.time.get_ticks()
        dt: float = (ticks - self._time_since_last_frame) / 1000.0
        self._time_since_last_frame = ticks

        # do updates 
        self._display.update(dt)

        # render
        self._render()

    def _render(self):
        self.blit(self._display.get_surface(), (0, 0))
