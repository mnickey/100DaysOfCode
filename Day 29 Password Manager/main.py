from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(symbols) for _ in range(nr_symbols)]
    password_symbols = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    pwd_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    username = email_entry.get()
    password = pwd_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo("Error", "Please fill all fields")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"Do you really want to save this password?\n"
                                                      f"{username}\n {password}\n")

        if is_ok:
            with open('data.txt', 'a')  as file:
                file.write(f"{website} | {username} | {password}\n")

                # Clear all entries after saving
                website_entry.delete(0, END)
                pwd_entry.delete(0, END)

                messagebox.showinfo("Password Added", "Your information has been saved.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.configure(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, background="white")
IMG = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=IMG)
canvas.grid(row=0, column=1)

# ---------- LABELS ---------- #
website_label = Label(window, text="Website:", bg='white')
website_label.grid(row=1, column=0)

email_label = Label(window, text="E-mail/Username:", bg='white')
email_label.grid(row=2, column=0)

password_label = Label(window, text="Password:", bg='white')
password_label.grid(row=3, column=0)

# ---------- ENTRYS ---------- #
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "someone@example.com")

pwd_entry = Entry(width=17)
pwd_entry.grid(row=3, column=1)

# ---------- BUTTONS ---------- #
add_button = Button(width=36, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

window.mainloop()
