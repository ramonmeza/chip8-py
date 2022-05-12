from turtle import width
import pygame as pyg


class Display:
    
    # variable declarations
    _pixels: pyg.PixelArray


    # methods
    def __init__(self, width: int, height: int) -> None:
        size: tuple = (width, height)
        surface: pyg.Surface= pyg.Surface(size)

        self._pixels = pyg.PixelArray(surface)

    def update(self, dt: float) -> None:
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

    def get_surface(self) -> pyg.Surface:
        return self._pixels.make_surface()