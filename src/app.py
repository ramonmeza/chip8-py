import pygame as pyg
import pygame_gui as gui

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
    _gui_manager: gui.UIManager


    # methods
    def __init__(self) -> None:
        pyg.init()

        self._is_running = False
        self._time_since_last_frame = 0.0

        self._initialize_window()
        self._initialize_gui()
        self._initialize_emulation()

    def __del__(self) -> None:
        pyg.quit()

    def _initialize_window(self) -> None:
        settings: dict = Settings.load(Path('data/settings.json5'), 'window')
        window_size: tuple = (settings['width'], settings['height'])
        is_fullscreen: bool = settings['fullscreen']

        if is_fullscreen:
            self._window = pyg.display.set_mode(window_size, pyg.FULLSCREEN)
        else:
            self._window = pyg.display.set_mode(window_size)

        pyg.display.set_caption('Pygame Chip-8 Interpreter')

    def _initialize_gui(self) -> None:
        self._gui_manager = gui.UIManager(self._window.get_size())
        self._fps_counter = gui.elements.UILabel(pyg.Rect((0, 0), (50, 20)), 'FPS', self._gui_manager)

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
            
            self._gui_manager.process_events(event)

    def _update(self) -> None:
        # get delta time
        ticks: int = pyg.time.get_ticks()
        dt: float = (ticks - self._time_since_last_frame) / 1000.0
        self._time_since_last_frame = ticks
        
        # update components
        self._emulation.update(dt)
        self._gui_manager.update(dt)

        fps = int(1 / (dt if dt > 0 else 1))
        self._fps_counter.set_text(f'{fps} FPS')

    def _render(self) -> None:
        # draw the emulation to the window
        self._window.blit(pyg.transform.scale(self._emulation, self._window.get_rect().size), (0, 0))
        
        # draw the gui
        self._gui_manager.draw_ui(self._window)
        
        pyg.display.flip()


if __name__ == '__main__':
    app: App = App()
    app.run()
