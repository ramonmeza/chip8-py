from turtle import width
import pygame as pyg


class Display:
    
    # variable declarations
    _width: int
    _height: int
    _pixels: pyg.PixelArray


    # methods
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        self.clear()
        self._test()

    def _test(self) -> None:
        # test to ensure display pixels work
        width: int = self._pixels.shape[0]
        height: int = self._pixels.shape[1]
        
        for y in range(height):
            for x in range(width):
                val: int = (y * 1) + x
                if val % 2 == 0:
                    self._pixels[x, y] = (255, 255, 255)
                else:
                    self._pixels[x, y] = (0, 0, 0)

    def update(self, dt: float) -> None:
        # clear if space is pressed
        if pyg.key.get_pressed()[pyg.K_SPACE]:
            self.clear()

    def get_surface(self) -> pyg.Surface:
        return self._pixels.make_surface()

    def clear(self) -> None:
        surface: pyg.Surface= pyg.Surface((self._width, self._height))
        self._pixels = pyg.PixelArray(surface)
