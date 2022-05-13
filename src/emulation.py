import json5
import pygame as pyg

from pathlib import Path
from typing import List

from cpu import Cpu
from display import Display
from memory import Memory
from settings import Settings
from sound_timer import SoundTimer
from stack import Stack
from timer import Timer


class Emulation(pyg.Surface):
    '''
    Composes and manages the emulation and handles emulation-level events.
    '''

    # constants
    FONT_MEMORY_OFFSET: int = 0x050
    ROM_MEMORY_OFFSET: int = 0x200


    # variable declarations
    _settings: dict
    _display: Display
    _memory: Memory
    _stack: Stack
    _delay_timer: Timer
    _sound_timer: SoundTimer
    _cpu: Cpu


    # methods
    def __init__(self) -> None:
        # get settings
        display_settings: dict = Settings.load(Path('data/settings.json5'), 'display')
        memory_settings: dict = Settings.load(Path('data/settings.json5'), 'memory')
        font_settings: dict = Settings.load(Path('data/settings.json5'), 'font')
        delay_timer_settings: dict = Settings.load(Path('data/settings.json5'), 'delayTimer')
        sound_timer_settings: dict = Settings.load(Path('data/settings.json5'), 'soundTimer')
        cpu_settings: dict = Settings.load(Path('data/settings.json5'), 'cpu')
        
        # subclass init
        pyg.Surface.__init__(self, size=(display_settings['width'], display_settings['height']))

        # initialize variables
        self._display = Display(display_settings['width'], display_settings['height'], display_settings['rate'])
        self._memory = Memory(memory_settings['amount'])
        self._stack = Stack()
        self._delay_timer = Timer(delay_timer_settings['rate'])
        self._sound_timer = SoundTimer(sound_timer_settings['rate'])
        self._cpu = Cpu(cpu_settings['rate'])
        
        # load font
        self._load_font(font_settings['name'])

        # load a rom
        # eventually this will move to App
        self._load_rom(Path('data/roms/octojam1title.ch8'))


    def _load_font(self, font_name: str) -> None:
        # load font data
        with open('data/fonts.json5', 'r') as fp:
            font_data = json5.load(fp)[font_name]

        # copy data into memory
        self._memory.copy(Emulation.FONT_MEMORY_OFFSET, font_data)

    def _load_rom(self, path: Path) -> None:
        rom_data: List[int] = list(path.read_bytes())
        self._memory.copy(Emulation.ROM_MEMORY_OFFSET, rom_data)

    def update(self, dt: float) -> None:
        # do updates
        self._display.update(dt)

        # render
        self._render()

    def _render(self):
        self.blit(self._display.get_surface(), (0, 0))
