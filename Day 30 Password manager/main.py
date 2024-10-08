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
import json

def save_to_file():

    # Getting data from entries
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }

    }

    # Checking if any of entries are left empty
    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:  #
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError: # This handles the error occuring when file is not created
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)  # writing into JSON file
        finally:
            # Clearing entries by deleting data
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Find password ------------------------------- #

def find_password():
   website = website_entry.get()
   try:
       with open("data.json") as data_file:
           data = json.load(data_file) # # Load the JSON data from the file and parse it into a Python object
   except FileNotFoundError:
       messagebox.showinfo(title="Error", message="No Data File Found")
   else:
        if website in data:
            email = data[website]["email"] # This line retrieves the email address associated with the website specified by the website variable.
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for {website} exists.")


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

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus() # focuses the cursor into the entry

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=21)
email_username_entry.grid(row=2, column=1)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, padx=50)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
