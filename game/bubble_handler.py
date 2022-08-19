import math
from game.bubble import Bubble


class BubbleHandler:
    """Static bubbles handler
    """

    @staticmethod
    def collision(
        bubble1: Bubble,
        bubble2: Bubble
    ) -> bool:
        """Static method fo checking bubbles on collision

        Args:
            bubble1 (Bubble): first bubble
            bubble2 (Bubble): second bubble

        Returns:
            bool: True if is collision happend else False
        """
        x1, y1 = bubble1.coords
        x2, y2 = bubble2.coords

        distance = math.sqrt(((x2 - x1) ** 2) + (y2 - y1) ** 2)
        return (
            distance <= bubble1.width//1.5
            or distance <= bubble2.width//1.5
            or distance <= bubble1.height//1.5
            or distance <= bubble2.height//1.5
        )

    @staticmethod
    def handle_collision(
        bubble1: Bubble,
        bubble2: Bubble
    ) -> None:
        """Static method what check bubbles on collision and handle logic

        Args:
            bubble1 (Bubble): first bubble
            bubble2 (Bubble): second bubble
        """
        if not (
            bubble1.collision_happend
            and bubble2.collision_happend
        ):
            if BubbleHandler.collision(bubble1, bubble2):
                print(f'1 -> {bubble1.coords} 2 -> {bubble2.coords}')
                bubble1.collision_happend = True
                bubble2.collision_happend = True
