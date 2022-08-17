from game.bubble import Bubble


class BubbleHandler:
    """docstring for BubbleHandler."""

    @staticmethod
    def collision(
        bubble1:Bubble,
        bubble2:Bubble
        )->bool:
        return (
            abs(bubble1.coords - bubble2.coords)<bubble1.width
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
            if collision(bubble1, bubble2):
                print(f'1 -> {bubble1.coords} 2 -> {bubble2.coords}')
            bubble1.collision_handled = True
            bubble2.collision_handled = True
