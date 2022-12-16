"""
            LEARNING TKINTER


"""

# Final project
import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Creating a Label

my_label = tkinter.Label(text="I`m a label", font=("Arial", 24, "italic"))
my_label.pack(side="left")   # --> This is a method in order to place the label in the screen


window.mainloop()