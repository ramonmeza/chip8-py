import pygame as pyg

from pathlib import Path

from emulation import Emulation
from settings import Settings


class App:
    '''
    Manages the application window and handles application-level events.
    '''

    # variable declarations
    _is_running: bool
    _time_since_last_frame: float
    _window: pyg.Surface
    _emulation: Emulation
    

    # methods
    def __init__(self) -> None:
        pyg.init()

        self._is_running = False
        self._time_since_last_frame = 0.0

        self._initialize_window()
        self._initialize_emulation()

    def __del__(self) -> None:
        pyg.quit()

    def _initialize_window(self) -> None:
        settings: dict = Settings.load(Path('data/settings.json'), 'window')
        window_size: tuple = (settings['width'], settings['height'])
        is_fullscreen: bool = settings['fullscreen']

        if is_fullscreen:
            self._window = pyg.display.set_mode(window_size, pyg.FULLSCREEN)
        else:
            self._window = pyg.display.set_mode(window_size)

        pyg.display.set_caption('Pygame Chip-8 Interpreter')

    def _initialize_emulation(self) -> None:
        self._emulation = Emulation()

    def run(self):
        self._is_running = True
        while self._is_running:
            self._handle_events()
            self._update()
            self._render()
    
    def _handle_events(self) -> None:
        '''Handles application-level events, such as window operations.'''
        for event in pyg.event.get():
            if (event.type == pyg.QUIT) or (event.type == pyg.KEYDOWN and event.key == pyg.K_ESCAPE):
                self._is_running = False

    def _update(self) -> None:
        # get delta time
        ticks: int = pyg.time.get_ticks()
        dt: float = (ticks - self._time_since_last_frame) / 1000.0
        self._time_since_last_frame = ticks
        
        self._emulation.update(dt)

    def _render(self) -> None:
        self._window.blit(pyg.transform.scale(self._emulation, self._window.get_rect().size), (0, 0))
        pyg.display.flip()


if __name__ == '__main__':
    app: App = App()
    app.run()
