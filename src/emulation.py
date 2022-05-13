from dis import dis
import pygame as pyg

from pathlib import Path

from display import Display
from memory import Memory
from settings import Settings


class Emulation(pyg.Surface):
    '''
    Composes and manages the emulation and handles emulation-level events.
    '''

    # variable declarations
    _settings: dict
    _display: Display
    _memory: Memory


    # methods
    def __init__(self) -> None:
        # get settings
        display_settings: dict = Settings.load(Path('data/settings.json5'), 'display')
        memory_settings: dict = Settings.load(Path('data/settings.json5'), 'memory')
        
        display_size: tuple = (display_settings['width'], display_settings['height'])

        # subclass init
        pyg.Surface.__init__(self, size=display_size)

        # initialize variables
        self._display = Display(display_settings['width'], display_settings['height'])
        self._memory = Memory(memory_settings['amount'])

    def update(self,dt: float) -> None:
        # do updates 
        self._display.update(dt)

        # render
        self._render()

    def _render(self):
        self.blit(self._display.get_surface(), (0, 0))
