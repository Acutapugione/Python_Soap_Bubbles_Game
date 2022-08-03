#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


class Ball:
    def __init__(self, canvas, paddle, score, color) -> None:
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.color = color
        self.hitted = False
        
        self.id = canvas.create_oval(10,10,40,40, fill=color)
        self.canvas.move(self.id, 245, 100)
        
        starts = [-2, -1, 1, 2]
        random.shuffle(starts)

        self.x = starts[1]
        self.y = -2

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hit_paddle(self, pos)->bool:
        paddle_pos = self.canvas.coords(self.paddle.id)

        if (pos[2] >= paddle_pos[0]
            and pos[0] <= paddle_pos[2]
            and pos[3] >= paddle_pos[1]
            and pos[3] <= paddle_pos[3]
            ):
            self.score.hit()
            return True
        return False
    
    def draw(self)->None:
        self.canvas.move(
            self.id, 
            self.x,
            self.y)
        pos = self.canvas.coords(self.id)

        # если шарик падает сверху  
        if pos[1] <= 0:
            # задаём падение на следующем шаге = 2
            self.y = 2
        # если шарик правым нижним углом коснулся дна
        if pos[3] >= self.canvas_height:
            # помечаем это в отдельной переменной
            self.hitted = True
            # выводим сообщение и количество очков
            self.canvas.create_text(250, 120, text='You lose', font=('Courier', 30), fill='red')
        # если было касание платформы
        if self.hit_paddle(pos) == True:
            # отправляем шарик наверх
            self.y = -2
        # если коснулись левой стенки
        if pos[0] <= 0:
            # движемся вправо
            self.x = 2
        # если коснулись правой стенки
        if pos[2] >= self.canvas_width:
            # движемся влево
            self.x = -2