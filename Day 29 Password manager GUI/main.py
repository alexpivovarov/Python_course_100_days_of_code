# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
  from random import choice, randint, shuffle

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


  password_list = []


  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers

  shuffle(password_list)

  password = "".join(password_list) # Converting "password_list" into a single string

  password_entry.insert(0, password)






# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_to_file():

    # Getting data from entries
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    # Checking if any of entries are left empty
    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any field empty")
    else:
        # Displaying a message_box
        is_ok = messagebox.askokcancel(title="Title", message=f"Details entered: \nEmail: {email_username} \nPassword: {password} \n Save it?")

        if is_ok:
            with open("data.txt", "a") as data_file:  # "a" stands for append mode. Keyword "with" allows to close the file after opening it.
                data_file.write(f"{website} | {email_username} | {password}\n") # writing data into data_file. Following 3 pieces of data are placed onto a new line
                # Clearing entries by deleting data
                website_entry.delete(0, END)
                email_username_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Password Manager")
window.geometry("500x500")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)  # placing logo in the middle of the image
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus() # focuses the cursor into the entry

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, padx=50)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
