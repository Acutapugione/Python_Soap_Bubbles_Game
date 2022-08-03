#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import time
import random
from Ball import Ball
from Paddle import Paddle
from Score import Score




def playGame(canvas, tk):

    score = Score(canvas, 'green')
    paddle = Paddle(canvas, 'White')
    ball = Ball(canvas, paddle, score, 'red')
    while not ball.hitted:
        if paddle.started == True:
            ball.draw()
            paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.001)
    time.sleep(3)

def main():
    try:
        tk = Tk()
        tk.title('Ping balls')
        tk.resizable(0, 0)
        tk.wm_attributes('-topmost', 1)

        canvas = Canvas(tk, width=400, height=500, highlightthickness=0)
        canvas.pack()
        tk.update()
        playGame(canvas, tk)
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)

