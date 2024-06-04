from pygame import Surface, SRCALPHA, Rect


class ScrollSurfaceManager:
    def __init__(self, size: tuple):
        self.__surface: Surface = Surface(size, SRCALPHA)
        self.__surface_rect: Rect = self.__surface.get_rect()

    @property
    def surface(self):
        return self.__surface

    @property
    def surface_rect(self):
        return self.__surface_rect

    def check_if_in_surface(self, position: tuple):
        return self.__surface_rect.collidepoint(position)
