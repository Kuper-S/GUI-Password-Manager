import json
from tkinter import *
import tkinter
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    # instant copy the new password for any use.
    pyperclip.copy(text=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = email_pass_entry.get()
    website = website_entry.get()
    pass_word = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": pass_word
    }
    }

    if len(website) == 0 or len(pass_word) == 0:
        messagebox.showerror(title="Invalid length .", message=" Invalid length of one or two lines .")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.jason", "w") as data_file:
                # Updating old data with new data
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.jason", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.jason") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]['email']
            passwrd = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email :{email} \n Password : {passwrd}")
        else:
            messagebox.showinfo(title="Error", message="No Website Data (Email and Password) Exists .")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)
# Labels
website_label = tkinter.Label(text="Website:", bg="white", highlightthickness=0, font=("ariel", 8, "bold"))
website_label.grid(row=1, column=0)
email_pass_label = tkinter.Label(text="Email/Username:", bg="white", highlightthickness=0, font=("ariel", 7, "bold"))
email_pass_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:", bg="white", highlightthickness=0, font=("ariel", 8, "bold"))
password_label.grid(row=3, column=0)

# Entry's
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
# put the corsair straight in the website entry line with the (focus method)
website_entry.focus()
email_pass_entry = tkinter.Entry(width=35)
email_pass_entry.grid(row=2, column=1, columnspan=2)
email_pass_entry.insert(index=0, string="kupkup1992@gmail.com")
password_entry = tkinter.Entry(width=30)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = tkinter.Button(text="Generate Password", bg="white", highlightthickness=0,
                                          font=("ariel", 8, "bold"), command=generate_password)
generate_password_button.grid(row=3, column=3)

add_password_button = tkinter.Button(text="Add", width=36, bg="white", highlightthickness=0,
                                     font=("ariel", 8, "bold"), command=save)
add_password_button.grid(row=4, column=1, columnspan=2)

search_button = tkinter.Button(text="Search", width=16, bg="white", highlightthickness=0,
                               font=("ariel", 8, "bold"), command=find_password)
search_button.grid(row=1, column=3)
window.mainloop()
