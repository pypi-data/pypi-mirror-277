from pygame_animation import AnimationManager
from .scroll_speed_manager import ScrollSpeedManager


class ScrollSpeedAnimationManager(AnimationManager):
    def __init__(self, scroll_speed_manager: ScrollSpeedManager, speed_per_frame: float = 0.05):
        super().__init__(percentage_per_iteration=speed_per_frame)
        self.__scroll_speed_manager = scroll_speed_manager

    def animate(self) -> None:
        self.__scroll_speed_manager.current_speed = self.current_value

    def activated_animation_setup(self) -> None:
        self.set_target(current_value=self.__scroll_speed_manager.current_speed,
                        target_value=self.__scroll_speed_manager.max_speed)

    def deactivated_animation_setup(self) -> None:
        self.set_target(current_value=self.__scroll_speed_manager.current_speed, target_value=0)