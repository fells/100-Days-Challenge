"""
        Creating a Flash Card app
"""

# Final Project

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
import pandas

data_dict = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Deutsch_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


# -----------------------------GENERATE RANDOM CARD------------------------
def next_card():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="Deutsch", fill="black")
    canvas.itemconfig(card_word, text=current_card["Deutsch"], fill="black")
    canvas.itemconfig(canvas_background, image=fg)
    flip_timer = screen.after(4000, func=flip_card)


# -----------------------------FLIP CARD-----------------------------------

def flip_card():
    canvas.itemconfig(card_title, text="Portuguese", fill="white")
    canvas.itemconfig(card_word, text=current_card["Portuguese"], fill="white")
    canvas.itemconfig(canvas_background, image=bg)



# -----------------------------KNOWN WORDS---------------------------------

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------------------------------UI SETUP-----------------------------------

screen = Tk()
screen.title("Flash Card")
screen.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = screen.after(4000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
fg = PhotoImage(file="images/card_front.png")
bg = PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=fg)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
correct = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

btn_correct = Button(image=correct, highlightthickness=0, command=is_known)
btn_wrong = Button(image=wrong, highlightthickness=0, command=next_card)

btn_correct.grid(column=1, row=1)
btn_wrong.grid(column=0, row=1)


next_card()
screen.mainloop()
