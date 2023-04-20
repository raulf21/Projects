from distutils import command
from email import message
from tkinter import *
from tkinter import messagebox
import secrets
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd_length = 15

    while True:
        pwd = ""
        num_digits = 0
        num_special_chars = 0
        for i in range(pwd_length):
            char = secrets.choice(alphabet)
            pwd += char
            if char in special_chars:
                num_special_chars += 1
            elif char in digits:
                num_digits += 1
        
        if num_digits >= 2 and num_special_chars >= 2:
            break    
    password_entry.insert(0,pwd)
    pyperclip.copy(pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left anything empty")
    else:
        is_ok = messagebox.showinfo(title=website,message=f"These are the details entered \nEmail {email}"f"\nPassword:{password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt",'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=20) 
canvas = Canvas(width=200,height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(END,"raulflores650@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1,columnspan=2)


generate_password_button = Button(text="Generate Password",command=generate)
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save_password)
add_button.grid(row=4,column=1)


window.mainloop()