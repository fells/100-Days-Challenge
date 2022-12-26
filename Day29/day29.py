# Final Project
# Creating a Password generator with Tkinter
from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    lower_alphabet = list(string.ascii_lowercase)
    upper_alphabet = list(string.ascii_uppercase)
    numbers = list(string.digits)
    symbols = list(string.punctuation)
    all_characters = list(lower_alphabet + upper_alphabet + numbers + symbols)
    random_num = random.randint(8, 16)
    password_list = []

    for char in range(random_num):
        password_list.append(random.choice(all_characters))

    password_string = "".join(password_list)

    entry_password.insert(0, password_string)
    pyperclip.copy(password_string)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email_user.get()
    password = entry_password.get()

    if len(password) == 0 or len(website) == 0:
        messagebox.showerror(title="Error", message="Please complete the form in order to save")

    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered: \n"
                                                           f"Email: {email}\n"
                                                           f"Password: {password}\n"
                                                           f"Is it ok to save ?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0, END)
                entry_password.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# Logo
photo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_email_user = Label(text="Email/Username:")
label_password = Label(text="Password:")

label_website.grid(column=0, row=1)
label_email_user.grid(column=0, row=2)
label_password.grid(column=0, row=3)

# Entry's

entry_website = Entry(width=35)
entry_website.focus()
entry_email_user = Entry(width=35)
entry_email_user.insert(0, "micheldcalil@hotmail.com")
entry_password = Entry(width=21)

entry_website.grid(column=1, row=1, columnspan=2)
entry_email_user.grid(column=1, row=2, columnspan=2)
entry_password.grid(column=1, row=3)

# Buttons

btn_generate_password = Button(text="Generate Password", command=generate_password)
btn_add = Button(text="Add", width=33, command=save)

btn_generate_password.grid(column=2, row=3)
btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
