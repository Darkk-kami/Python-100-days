from tkinter import *
from tkinter import messagebox
from passwd_gen import Passwd
import json

HEIGHT = 300
WIDTH = 500
EMAIL = 'dummy@gmail.com'


def generate():
    passwd = Passwd()
    passwd_entry.delete(0, END)
    passwd_entry.insert(0, passwd.new_password)




def save_passwd(secret_string):
    website_entry.delete(0, END)
    passwd_entry.delete(0, END)

    try:
        with open('secrets.json', 'r') as file:
            data = json.load(file)
            data.update(secret_string)

        with open('secrets.json', 'w') as file:
            json.dump(data, file, indent=4)

    except FileNotFoundError:
        with open('secrets.json', 'w') as file:
            json.dump(secret_string, file, indent=4)


def save_file():
    website_data = website_entry.get()
    passwd_data = passwd_entry.get()
    username_data = username.get()
    secret_string = {
        website_data: {
            "email": username_data,
            "passwd_data": passwd_data,
        }
    }

    if website_data == "" or passwd_data == "" or username_data == "":
        messagebox.askokcancel(title="Missing input", message="Spaces cannot be blank")

    else:
        is_ok = messagebox.askokcancel(title="Save Prompt", message="Do you want to save password?")
        if is_ok:
            save_passwd(secret_string)


def search():
    website_data = website_entry.get()
    try:
        with open('secrets.json') as file:
            data = json.load(file)
            if website_data in data:
                email = data[website_data]['email']
                passwd = data[website_data]["passwd_data"]

                passwd_entry.delete(0, END)
                passwd_entry.insert(0, passwd)

                username.delete(0, END)
                username.insert(0, email)

            else:
                messagebox.showinfo(title='Error', message='Entry not found')
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='Password file does not exist')

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.minsize(width=WIDTH, height=HEIGHT)
windows.maxsize(width=WIDTH, height=HEIGHT)
windows.title("Password Manager")


logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.pack()

website_entry = Entry(width=WIDTH//18, borderwidth=4)
website_entry.focus()
website_entry.pack(padx=(0, 110))

username = Entry(width=WIDTH//11, borderwidth=4)
username.insert(0, EMAIL)
username.pack()

passwd_entry = Entry(width=WIDTH//18, borderwidth=4)
passwd_entry.pack(padx=(0, 110))

# --------------------------Buttons-----------------------------------------------------------
add_button = Button(width=39, text="Add", pady=80, command=save_file)
add_button.pack()

gen_passwd = Button(width=17, text="Generate password", font=("Times new roman", 8, "normal"),
                    wraplength=100, command=generate)
gen_passwd.place(x=280, y=255)

search = Button(width=17, text="Search", font=("Times new roman", 8, "normal"),
                wraplength=100, command=search)
search.place(x=280, y=204)

text = Label(text="Website:\n\nEmail/Username:\n\nPassword:", justify="right", font=("Times new roman", 8, "normal"))
text.place(x=10, y=200)

windows.mainloop()
