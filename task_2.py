#!/usr/bin/env python3
# -*- config: utf-8 -*-

# напишите программу по следующему описанию. Нажатие Enter в
# однострочном текстовом поле приводит к перемещению текста из него в список (экземпляр
# Listbox ). При двойном клике ( <Double-Button-1> ) по элементу-строке списка, она должна
# копироваться в текстовое поле.

from tkinter import *

root = Tk()
root.geometry("500x300+300+300")
root.title("Задание 2")

ent1 = Entry()
lb1 = Listbox()

ent1.pack()
lb1.pack()
ent1.bind('<Return>', lambda e:  lb1.insert(0, ent1.get()))
lb1.bind('<Double-Button-1>', lambda e: ent1.insert(0, lb1.get(lb1.curselection())))

root.mainloop()
