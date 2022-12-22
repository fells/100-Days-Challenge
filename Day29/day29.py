"""

"""

# Final Project
# Creating a Password generator with Tkinter
from tkinter import *
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)



# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=100, pady=100)

# Logo
photo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=189)
canvas.create_image(100, 95, image=photo)
canvas.grid(column=1, row=0)


# Labels
label_website = Label(text="Website:")
label_email_user = Label(text="Email/Username:")
label_password = Label(text="Password:")

label_website.config(padx=20)
label_email_user.config(padx=20)
label_password.config(padx=20)

label_website.grid(column=0, row=1)
label_email_user.grid(column=0, row=2)
label_password.grid(column=0, row=3)


# Entrys

entry_website = Entry(width=40)
entry_email_user = Entry(width=40)
entry_password = Entry(width=20)

entry_website.grid(column=1, row=1)
entry_email_user.grid(column=1, row=2)
entry_password.grid(column=1, row=3, rowspan=2)


# Buttons

btn_generate_password = Button(text="Generate Password", width=20)
btn_add = Button(text="Add", width=80)

btn_generate_password.grid(column=1, row=3)
btn_add.grid(column=1, row=4)

window.mainloop()