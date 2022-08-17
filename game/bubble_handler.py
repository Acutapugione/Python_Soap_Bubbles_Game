from game.bubble import Bubble


class BubbleHandler:
    """docstring for BubbleHandler."""

    @staticmethod
    def collision(
        bubble1:Bubble,
        bubble2:Bubble
        )->bool:
        x1, y1 = bubble1.coords
        x2, y2 = bubble2.coords

        distanceX = abs(x1 - x2)
        distanceY = abs(y1 - y2)
        return (
            distanceX < bubble1.width
            or distanceY < bubble1.height
        )

    @staticmethod
    def handle_collision(
        bubble1:Bubble,
        bubble2:Bubble
        )->None:
        if not (
            bubble1.collision_handled
            and bubble2.collision_handled
        ):
            if BubbleHandler.collision(bubble1, bubble2):
                print(f'1 -> {bubble1.coords} 2 -> {bubble2.coords}')
            bubble1.collision_handled = True
            bubble2.collision_handled = True
