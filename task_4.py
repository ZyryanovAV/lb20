#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Создайте на холсте подобное изображение:

from tkinter import *

root = Tk()
root.geometry("500x300+300+300")
root.title("Задание 4")
c = Canvas(root, width=200, height=200, bg='white')
c.pack()
c.create_rectangle(50, 90, 140, 175,
                   fill='orange', outline='orange')
c.create_polygon(30, 90, 160, 90, 95, 40,
                 fill='yellow', outline='yellow')
c.create_oval(150, 10, 190, 50,
              fill='yellow', outline='yellow')
x = -20
while x < 200:
    c.create_arc(x, 170, x + 40, 250, outline='orange',
                 style=ARC, start=200, extent=-80,
                 width=2)
    x += 10
root.mainloop()
