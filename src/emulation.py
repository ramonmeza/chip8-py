import json5
import pygame as pyg

from pathlib import Path

from display import Display
from memory import Memory
from settings import Settings
from stack import Stack


class Emulation(pyg.Surface):
    '''
    Composes and manages the emulation and handles emulation-level events.
    '''

    # variable declarations
    _settings: dict
    _display: Display
    _memory: Memory
    _stack: Stack


    # methods
    def __init__(self) -> None:
        # get settings
        display_settings: dict = Settings.load(Path('data/settings.json5'), 'display')
        memory_settings: dict = Settings.load(Path('data/settings.json5'), 'memory')
        font_settings: dict = Settings.load(Path('data/settings.json5'), 'font')
        
        # subclass init
        pyg.Surface.__init__(self, size=(display_settings['width'], display_settings['height']))

        # initialize variables
        self._display = Display(display_settings['width'], display_settings['height'])
        self._memory = Memory(memory_settings['amount'])
        self._stack = Stack()
        
        # load font
        self._load_font(font_settings['name'])

    def _load_font(self, font_name: str) -> None:
        # load font data
        with open('data/fonts.json5', 'r') as fp:
            font_data = json5.load(fp)[font_name]

        # copy data into memory
        self._memory.copy(0x50, font_data)

    def update(self,dt: float) -> None:
        # do updates 
        self._display.update(dt)

        # render
        self._render()

    def _render(self):
        self.blit(self._display.get_surface(), (0, 0))
