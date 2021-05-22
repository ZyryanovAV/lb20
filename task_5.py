#!/usr/bin/env python3
# -*- config: utf-8 -*-

# в данной программе создается анимация круга, который движется от левой
# границы холста до правой:

from tkinter import *
import time
import random

WIDTH = 1024
HEIGHT = 720

tk = Tk()
cv = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title('Tkinter ballz')
cv.pack()

class Ball:
    def __init__(self, size, color):
        self.shape = cv.create_oval(10, 10, size, size, fill=color)
        self.xspeed = random.randint(-6, 8)
        if self.xspeed == 0:
            self.xspeed = random.randint(-6, 8)
        self.yspeed = random.randint(-6, 8)
        if self.yspeed == 0:
            self.yspeed = random.randint(-6, 8)

    def move(self):
        cv.move(self.shape, self.xspeed, self.yspeed)
        pos = cv.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed

        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed

colors = ['red', 'gold', 'blue']
balls = []
for i in range(10):
    balls.append(Ball(70, random.choice(colors)))





while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(0.001)
