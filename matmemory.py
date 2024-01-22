from tkinter import *
from tkinter import ttk

import random

"""
import os

# Setup kartica
file_extensions = {}
directory = os.fsencode(".\\Cards")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    f = filename.split(".")
    file_extensions[tuple(map(int, f[0].split("_")))] = f[1]
"""

GLOBAL_STATE = 0


def resize_image(image, maxsize):
    r1 = image.width()/maxsize[0]  # width ratio
    r2 = image.height()/maxsize[1]  # height ratio
    ratio = max(r1, r2)
    newsize = (int(image.width()/ratio), int(image.height()/ratio))
    image = image.resize(newsize, PhotoImage.ANTIALIAS)
    return image


def stick(i, j):
    s = ""
    if i != 0: s += "w"
    if i != 5: s += "e"
    if j != 0: s += "n"
    if j != 5: s += "s"
    return s


class Card:
    def __init__(self, index, member):
        self.index = index
        self.member = member
        self.image = PhotoImage(file=f"{index}_{member} resized.png")
        # self.frame = ttk.Frame(startframe)
        # self.frame.configure(width=250, height=150)
        self.button = Button(startframe, text="1", width=250, height=150, command=self.turn)

        # self.frame.rowconfigure(0, weight=1)
        # self.frame.columnconfigure(0, weight=1)

        self.state = 0

    def turn_around(self):
        self.button.configure(image=self.image)

    def turn_back(self):
        self.button.configure(image="")

    def turn(self):
        if self.state == 0:
            self.turn_around()
            self.state = 1
        elif self.state == 1:
            self.turn_back()
            self.state = 0


def start():
    pass


root = Tk()
root.title("MathMemory")
startframe = ttk.Frame(root, padding="12 12 12 12")
startframe.grid(column=0, row=0, sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
startframe.columnconfigure(0, weight=1)
for i in range(6):
    startframe.rowconfigure(i, weight=1)
    startframe.columnconfigure(i, weight=1)

start_button = ttk.Button(startframe, text="Start", command=...)

choices = random.sample(list(range(1, 33)), 18)
cards = [Card(c, i) for c in choices for i in [1, 2]]
random.shuffle(cards)

for i in range(6):
    for j in range(6):
        cards[i*6+j].button.grid(column=i, row=j)

root.mainloop()
