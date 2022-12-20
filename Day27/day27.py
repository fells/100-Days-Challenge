"""
            LEARNING TKINTER

            window = Tk()
            window.title("My first GUI program")
            window.minsize(width=500, height=300)

            # Creating a Label

            my_label = Label(text="I`m a label", font=("Arial", 24, "italic"))
            my_label.pack(side="top")  # --> This is a method in order to place the label in the screen


            # Creating a Button

            def button_clicked():
                button.config(text="I changed")
                input = entry.get()
                my_label.config(text=input)


            button = Button(fg="blue", bg="white", text="Click me", command=button_clicked)
            button.pack()

            # Entry Component

            entry = Entry(width=15)  # --> This is a input field
            entry.insert(END, string="Email")
            entry.pack()

            # Text Editor

            text = Text(width=30, height=5)  # --> This is a method where you can type in a text
            text.focus()
            text.pack()


            # Spin Box
            def spinbox_used():
                # Gets the current value of the SpinBox
                print(spin_box.get())


            spin_box = Spinbox(from_=0, to=10, width=5,
                               command=spinbox_used)  # --> This a method where you can choose a amount of number
            spin_box.pack()


            # Scale
            def scale_used(value):
                print(value)


            scale = Scale(from_=0, to=100, command=scale_used)
            scale.pack()


            # Check Box
            def check_button_used():
                # Prints 1 If ON otherwise 0
                print(checked_state.get())


            checked_state = IntVar()
            check = Checkbutton(text="Is on ?", variable=checked_state, command=check_button_used)
            check.pack()


            # Radio button
            def radio_used():
                print(radio_state.get())


            radio_state = IntVar()
            radio1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
            radio2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)

            radio1.pack()
            radio2.pack()


            # List Box

            def listbox_used(event):
                # prints current selection from listbox
                print(list_box.get(list_box.curselection()))


            list_box = Listbox(height=4)
            fruits = ["Orange", "Apple", "Banana", "Pear"]
            for item in fruits:
                list_box.insert(fruits.index(item), item)
            list_box.bind("<<ListboxSelect>>", listbox_used)
            list_box.pack()

            window.mainloop()

"""

# Final project
# Create a Mile;Km converter

from tkinter import *
FONT = ("Times", 12, "normal")

window = Tk()
window.title("Distance Converter")
window.minsize(width=300, height=180)
window.config(padx=10, pady=10)
clicked = True
def switch_clicked():
    global clicked
    if clicked:
        miles.config(text="Km", font=FONT)
        km.config(text="Miles", font=FONT)
        conversion.config(text="0", font=FONT)
        clicked = False
    else:
        miles.config(text="Miles", font=FONT)
        km.config(text="Km", font=FONT)
        conversion.config(text="0", font=FONT)
        clicked = True

    return clicked

def button_clicked():
    input1 = entry1.get()
    miles_to_km = (float(input1) * 1.609344)
    km_to_miles = (float(input1) / 1.609344)

    if clicked:
        conversion.config(text=f"{'%.4f' % miles_to_km}", font=FONT)
    else:
        conversion.config(text=f"{'%.4f' % km_to_miles}", font=FONT)


# Creating a Label

my_label = Label(text="Is equals to", font=FONT)
my_label.grid(column=0, row=2)  # --> This is a method in order to place the label in the screen
my_label.config(pady=5)

# Conversion

conversion = Label(text="0", font=FONT)
conversion.grid(column=1, row=2)
conversion.config(pady=5)


# Miles
miles = Label(text="Miles", font=FONT)
miles.grid(column=2, row=1)
miles.config(padx=10)

# Km
km = Label(text="Km", font=FONT)
km.grid(column=2, row=2)
km.config(padx=10)
# Creating a Button

button = Button(fg="black", bg="white", text="Convert", command=button_clicked)
button.grid(column=1, row=3)
button.config(pady=5)

switch = Button(fg="black", bg="white", text="↕", font=FONT, command=switch_clicked)
switch.grid(column=3, row=2)
switch.config(pady=5)

# Entry Component

entry1 = Entry(width=15)  # --> This is a input field
entry1.grid(column=1, row=1)
entry1.focus()

window.mainloop()
