"""
        Creating a Flash Card app
"""

# Final Project

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
import pandas

# ------------------------------UI SETUP-----------------------------------

screen = Tk()
screen.title("Flash Card")
screen.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
fg = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=fg)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
correct = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

btn_correct = Button(image=correct, highlightthickness=0)
btn_wrong = Button(image=wrong, highlightthickness=0)

btn_correct.grid(column=1, row=1)
btn_wrong.grid(column=0, row=1)

screen.mainloop()
