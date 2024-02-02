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


class State:
    def __init__(self):
        self.state = 0
        self.selected = None
        self.member = None
        self.first = None
        self.second = None

    def reset(self):
        self.__init__()


state = State()


def resize_image(image, maxsize):
    r1 = image.width() / maxsize[0]  # width ratio
    r2 = image.height() / maxsize[1]  # height ratio
    ratio = max(r1, r2)
    newsize = (int(image.width() / ratio), int(image.height() / ratio))
    image = image.resize(newsize, PhotoImage.ANTIALIAS)
    return image


def stick(i, j):
    s = ""
    if i != 0: s += "w"
    if i != 5: s += "e"
    if j != 0: s += "n"
    if j != 5: s += "s"
    return s


class Card(ttk.Frame):
    def __init__(self, index, member):

        ttk.Frame.__init__(self, cardfield, height=125, width=225, padding=0)
        self.disabled = False
        self.index = index
        self.member = member
        self.image = PhotoImage(file=f"{index}_{member} resized.png")

        self.grid_propagate(False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.button = ttk.Button(self)
        self.button.grid(row=0, column=0, sticky="nsew")

        # self.frame.rowconfigure(0, weight=1)
        # self.frame.columnconfigure(0, weight=1)

        self.state = 0

    def turn_around(self):
        self.button.configure(image=self.image)

    def turn_back(self):
        self.button.configure(image=PhotoImage())

    def turn(self):
        if self.disabled:
            return
        if self.state == 0:
            self.turn_around()
            self.state = 1
        elif self.state == 1:
            self.turn_back()
            self.state = 0

    def emphasize(self, b):
        if not b:
            self.button.configure(style="TButton")
        else:
            self.button.configure(style="TurnedCard.TButton")


def disable_all(b: bool):
    global cards
    for c in cards:
        c.disabled = b




def turn(card):

    def reset():
        global card_dict
        global state

        disable_all(False)
        card_dict[state.first].emphasize(False)
        card_dict[state.second].emphasize(False)

        if state.first[0] == state.second[0] and state.first[1] != state.second[1]:
            card_dict[state.first].button.state(["disabled"])
            card_dict[state.second].button.state(["disabled"])

            card_dict.pop(state.first)
            card_dict.pop(state.second)
        else:
            card_dict[state.first].turn()
            card_dict[state.second].turn()

        state.reset()

    def wrapped():
        global state
        if state.state == 0:
            state.selected = card.index
            state.member = card.member
            state.first = (card.index, card.member)
            card.turn()
            card.disabled = True
            card.emphasize(True)
            state.state = 1
        elif state.state == 1:
            if state.selected != card.index or state.member != card.member:
                card.turn()
                card.emphasize(True)
                state.second = (card.index, card.member)
                disable_all(True)
                state.state = 2
                root.after(2000, reset)

    return wrapped


root = Tk()
root.title("MatMemory")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

style = ttk.Style()
style.configure("TurnedCard.TButton", background="red", foreground="green")

mainframe = ttk.Frame(root, padding=12)
mainframe.grid(row=0, column=0, sticky="nsew")
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

cardfield = ttk.Frame(mainframe)
cardfield.grid(column=0, row=0)
for i in range(6):
    cardfield.rowconfigure(i, weight=1)
    cardfield.columnconfigure(i, weight=1)

# start_button = ttk.Button(startframe, text="Start", command=...)

choices = random.sample(list(range(1, 33)), 18)
cards = [Card(c, i) for c in choices for i in [1, 2]]
random.shuffle(cards)
card_dict = {(card.index, card.member): card for card in cards}

for i in range(6):
    for j in range(6):
        cards[i * 6 + j].grid(column=i, row=j)
        cards[i * 6 + j].button.configure(command=turn(cards[i * 6 + j]))

root.mainloop()
