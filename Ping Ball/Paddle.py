#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


class Paddle:
    def __init__(self, canvas, color):
        # canvas ��������, ��� ��������� ����� ���������� �� ����� ����������� ������
        self.canvas = canvas
        # ������ ������������� ��������� 10 �� 100 ��������, ����������� ��������� ������ � �������� � ���������� ��� 
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        # ����� ������ ��������� ��������� ��������� ���������
        start_1 = [40, 60, 90, 120, 150, 180, 200]
        # ������������ ��
        random.shuffle(start_1)
        # �������� ������ �� ������������
        self.starting_point_x = start_1[0]
        # ���������� ��������� � ��������� ���������
        self.canvas.move(self.id, self.starting_point_x, 300)
        # ���� ��������� ������ �� ��������, ������� ��������� �� ��� � ���
        self.x = 0
        # ��������� ����� ���� ������
        self.canvas_width = self.canvas.winfo_width()
        # ����� ���������� �������
        # ���� ������ ������� ������ � ����������� ����� turn_right()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        # ���� ������� ����� � turn_left()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        # ���� ���� �� ��������, ������� ���
        self.started = False
        # ��� ������ ����� ����� Enter � �� ��������
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)
    # �������� ������ 
    def turn_right(self, event):
        # ����� ��������� ������ �� 2 ������� �� ��� �
        self.x = 2
    # �������� �����
    def turn_left(self, event):
        # ����� ��������� ����� �� 2 ������� �� ��� �
        self.x = -2
    # ���� ����������
    def start_game(self, event):
        # ������ �������� ����������, ������� �������� �� �����
        self.started = True
    # �����, ������� �������� �� �������� ���������
    def draw(self):
        # �������� ���� ��������� �� �������� ���������� ��������
        self.canvas.move(self.id, self.x, 0)
        # �������� ���������� ������
        pos = self.canvas.coords(self.id)
        # ���� �� ������� � ����� ������� 
        if pos[0] <= 0:
            # ���������������
            self.x = 0
        # ���� ������� � ������ ������� 
        elif pos[2] >= self.canvas_width:
            # ���������������
            self.x = 0




