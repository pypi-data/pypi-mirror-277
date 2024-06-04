from .content_bar import ContentBar
from pygame import Surface
from .scroll_speed_manager import ScrollSpeedManager
from .scroll_speed_animation_manager import ScrollSpeedAnimationManager
from .scroll_bar_event_handler import ScrollEventHandler
from .scroll_bar_position import ScrollBarPosition
from .scroll_surface_manager import ScrollSurfaceManager


class ScrollBarManager:
    def __init__(self, size: tuple[int, int], content_bar_list: list[ContentBar], position: tuple[int, int],
                 margin: int = 10, speed_per_frame: float = 0.05, max_scroll_speed: int = 20,
                 max_scroll_padding: int = 0):
        """
        Initializes the ScrollBarManager.

        Args:
            size (tuple[int, int]): The size of the scroll bar surface.
            content_bar_list (list[ContentBar]): List of content bars to manage.
            position (tuple[int, int]): The initial position of the scroll bar.
            margin (int, optional): Margin between content bars. Defaults to 10.
        """
        self.__check_if_content_bar(content_bar_list=content_bar_list)
        self.__scroll_speed_manager: ScrollSpeedManager = ScrollSpeedManager(max_speed=max_scroll_speed)
        self.__position: ScrollBarPosition = ScrollBarPosition(
            margin_between_content_bar=margin, position=position, scroll_speed_manager=self.__scroll_speed_manager
        )
        self.__surface_manager: ScrollSurfaceManager = ScrollSurfaceManager(size=size)
        self.__content_bar_list: list[ContentBar] = content_bar_list
        self.__scroll_speed_animation_manager: ScrollSpeedAnimationManager = ScrollSpeedAnimationManager(
            scroll_speed_manager=self.__scroll_speed_manager, speed_per_frame=speed_per_frame
        )
        self.__init_content_bar_list()
        self.__scroll_event_handler: ScrollEventHandler = ScrollEventHandler(
            position=self.__position, scroll_speed_animation_manager=self.__scroll_speed_animation_manager,
            scroll_surface_manager=self.__surface_manager, max_scroll_padding=max_scroll_padding
        )

    def __init_content_bar_list(self) -> None:
        """Initializes the position of each content bar in the list."""
        for index, content_bar in enumerate(self.__content_bar_list):
            content_bar.set_y_position(index, self.__position)

    @staticmethod
    def __check_if_content_bar(content_bar_list: list[ContentBar]) -> None:
        """
        Checks if all items in the list are instances of ContentBar.

        Args:
            content_bar_list (list[ContentBar]): List to check.

        Raises:
            Exception: If any item in the list is not of type ContentBar.
        """
        if not all(isinstance(item, ContentBar) for item in content_bar_list):
            raise Exception("Not all items are of type ContentBar!")

    def show(self, surface: Surface, window_height: int) -> None:
        """
        Renders the content bars onto the surface.

        Args:
            surface (Surface): The surface to render the content bars on.
            window_height (int): The height of the window to show the content bars.
        """
        self.__scroll_event_handler.check_for_events(content_bar_list=self.__content_bar_list,
                                                     surface=self.__surface_manager.surface)
        self.__surface_manager.surface.fill((0, 0, 0, 0))
        for content_bar in self.__content_bar_list:
            content_bar.show(window_height=window_height)
            self.__surface_manager.surface.blit(content_bar.surface, content_bar.position)
        self.__position.finish_scroll()
        surface.blit(self.__surface_manager.surface, self.__position.position)

    def check_if_scroll(self, event) -> None:
        """
        Checks if a scroll event has occurred and handles it.

        Args:
            event: The event to check.
        """
        self.__scroll_event_handler.check_if_scroll(event=event)

