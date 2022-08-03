#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


class Paddle:
    def __init__(self, canvas, color):
        # canvas означает, что платформа будет нарисована на нашем изначальном холсте
        self.canvas = canvas
        # создаЄм пр€моугольную платформу 10 на 100 пикселей, закрашиваем выбранным цветом и получаем еЄ внутреннее им€ 
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        # задаЄм список возможных стартовых положений платформы
        start_1 = [40, 60, 90, 120, 150, 180, 200]
        # перемешиваем их
        random.shuffle(start_1)
        # выбираем первое из перемешанных
        self.starting_point_x = start_1[0]
        # перемещаем платформу в стартовое положение
        self.canvas.move(self.id, self.starting_point_x, 300)
        # пока платформа никуда не движетс€, поэтому изменений по оси х нет
        self.x = 0
        # платформа узнаЄт свою ширину
        self.canvas_width = self.canvas.winfo_width()
        # задаЄм обработчик нажатий
        # если нажата стрелка вправо Ч выполн€етс€ метод turn_right()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        # если стрелка влево Ч turn_left()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        # пока игра не началась, поэтому ждЄм
        self.started = False
        # как только игрок нажмЄт Enter Ч всЄ стартует
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)
    # движемс€ вправо 
    def turn_right(self, event):
        # будем смещатьс€ правее на 2 пиксел€ по оси х
        self.x = 2
    # движемс€ влево
    def turn_left(self, event):
        # будем смещатьс€ левее на 2 пиксел€ по оси х
        self.x = -2
    # игра начинаетс€
    def start_game(self, event):
        # мен€ем значение переменной, котора€ отвечает за старт
        self.started = True
    # метод, который отвечает за движение платформы
    def draw(self):
        # сдвигаем нашу платформу на заданное количество пикселей
        self.canvas.move(self.id, self.x, 0)
        # получаем координаты холста
        pos = self.canvas.coords(self.id)
        # если мы упЄрлись в левую границу 
        if pos[0] <= 0:
            # останавливаемс€
            self.x = 0
        # если упЄрлись в правую границу 
        elif pos[2] >= self.canvas_width:
            # останавливаемс€
            self.x = 0




