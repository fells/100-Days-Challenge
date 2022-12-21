"""

"""

# Final Project
# Build a Pomodoro App
from tkinter import *
import math

# CONSTANTS

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# Timer Reset
def reset():
    label.config(text="Timer", fg=GREEN)
    canvas.config(timer_text())
# Timer Mechanism

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label.config(text="Break", fg=RED)
        countdow(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        countdow(short_break_sec)
    else:
        label.config(text="Work", fg=GREEN)
        countdow(work_sec)

# Countdown Mechanism
def countdow(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        screen.after(1000, countdow, count - 1)
    else:
        start_timer()

# UI Setup

screen = Tk()
screen.title("Pomodoro App")
screen.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# TIMER LABEL

label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), bg=YELLOW, fg=GREEN)
label.grid(column=1, row=0)

check_mark = Label(text="✓", font=(FONT_NAME, 15, "normal"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)
# BUTTONS

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset")
reset.grid(column=2, row=2)

screen.mainloop()
