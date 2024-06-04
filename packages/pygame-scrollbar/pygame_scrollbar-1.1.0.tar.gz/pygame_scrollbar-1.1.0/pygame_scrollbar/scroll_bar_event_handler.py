from pygame_timer import ActivationTimer
from pygame import MOUSEBUTTONDOWN, mouse
from .scroll_speed_animation_manager import ScrollSpeedAnimationManager
from .scroll_bar_position import ScrollBarPosition
from .content_bar import ContentBar
from .scroll_surface_manager import ScrollSurfaceManager
from pygame.surface import Surface


class ScrollEventHandler:
    def __init__(self, scroll_speed_animation_manager: ScrollSpeedAnimationManager, position: ScrollBarPosition,
                 scroll_surface_manager: ScrollSurfaceManager, max_scroll_padding: int = 0):
        """
        Initializes the ScrollEventHandler.

        Args:
            scroll_speed_animation_manager (ScrollSpeedAnimationManager):
            The manager that handles scroll speed animation.
            position (ScrollBarPosition): The position of the scroll bar.
        """
        self.__scroll_up: bool = False
        self.__scroll_surface_manager = scroll_surface_manager
        self.__activation_timer: ActivationTimer = ActivationTimer()
        self.__position: ScrollBarPosition = position
        self.__scroll_speed_animation_manager: ScrollSpeedAnimationManager = scroll_speed_animation_manager
        self.__max_scroll_padding = max_scroll_padding

    def check_for_events(self, content_bar_list: list[ContentBar], surface: Surface) -> None:
        """
        Checks for scroll events and updates the position accordingly.

        Args:
            content_bar_list (list[ContentBar]): List of content bars.
            surface (Surface): The surface to render the content bars on.
        """
        self.__check_if_stop_scroll()
        if self.__scroll_up:
            if not content_bar_list[-1].is_scrollable_up(scroll_bar_height=surface.get_height(),
                                                         padding=self.__max_scroll_padding):
                return
            self.__position.scroll_up()
        else:
            if not content_bar_list[0].is_scrollable_down():
                return
            self.__position.scroll_down()

    def check_if_scroll(self, event) -> None:
        """
        Checks if a scroll event has occurred and handles it.

        Args:
            event: The event to check.
        """
        if event.type != MOUSEBUTTONDOWN:
            return
        if event.button not in [4, 5]:
            return
        if not self.__check_if_mouse_in_surface():
            return
        self.__activation_timer.activation_stopped(activated=True)
        self.__scroll_speed_animation_manager.check_for_animation(activated=True)
        self.__scroll_up = event.button == 5

    def __check_if_mouse_in_surface(self):
        x, y = mouse.get_pos()
        scroll_x, scroll_y = self.__position.position
        relative_position = x - scroll_x, y - scroll_y
        return self.__scroll_surface_manager.check_if_in_surface(position=relative_position)

    def __check_if_stop_scroll(self) -> None:
        """
        Checks if the scrolling should be stopped and updates the animation manager accordingly.
        """
        if not self.__activation_timer.activation_stopped(activated=False):
            return
        self.__scroll_speed_animation_manager.check_for_animation(activated=False)
