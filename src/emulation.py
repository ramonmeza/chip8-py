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

    def update(self,dt: float) -> None:
        # do updates 
        self._display.update(dt)

        # render
        self._render()

    def _render(self):
        self.blit(self._display.get_surface(), (0, 0))
