import random
import time
from turtle import color
import config as c
from Game import Game
from TextObject import TextObject
from Ball import Ball
import pygame

class Breakout(Game):
    def __init__(self, b, paddle) -> None:
        super().__init__()
        # Регистрация метода handle_mouse_event() объекта кнопки
        self.mouse_handlers.append(b.handle_mouse_event)

        # Регистрация метода handle() ракетки для обработки событий клавиш
        self.keydown_handlers[pygame.K_LEFT].append(paddle.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(paddle.handle)
        self.keyup_handlers[pygame.K_LEFT].append(paddle.handle)
        self.keyup_handlers[pygame.K_RIGHT].append(paddle.handle)
    
    def show_message(self, 
                     text, 
                     color=color.WHITE, 
                     font_name='Arial', 
                     font_size=20, 
                     centralized=False):
        message = TextObject(c.screen_width // 2, 
                             c.screen_height // 2, 
                             lambda: text, color, 
                             font_name, font_size)
        self.draw()
        message.draw(self.surface, centralized)
        pygame.display.update()
        time.sleep(c.message_duration)
    
    def handle(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        else:
            self.moving_right = not self.moving_right
    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)

    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'

    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.state = 'pressed'

    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'

    def create_ball(self):
        speed = (random.randint(-2, 2), c.ball_speed)
        self.ball = Ball(c.screen_width // 2,
                         c.screen_height // 2,
                         c.ball_radius,
                         c.ball_color,
                         speed)
        self.objects.append(self.ball)