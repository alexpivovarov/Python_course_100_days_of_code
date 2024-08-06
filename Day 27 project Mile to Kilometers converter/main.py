import tkinter
from tkinter import END


window = tkinter.Tk()
window.geometry("300x200")

label = tkinter.Label(text="Mile to Km converter", font=("Arial", 15))
label.grid(column=2, row=1)


text = tkinter.Text(height=2, width=10)
text.focus() # Puts cursor in textbox.
text.grid(column=2, row=2)


miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=3, row=2)

km_label = tkinter.Label(text="Km")
km_label.grid(column=3, row=3)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=1, row= 3)

km_value_label = tkinter.Label(window, text="0")
km_value_label.grid(column=2, row=3)


def calculation():
    miles_value = float(text.get("1.0", END))  # Get the value from the text widget and convert it from string to float
    km_value = miles_value * 1.60934
    km_value_label.config(text=str(km_value)) # updating km_value_label with the string representation of the calculated km_value

button = tkinter.Button(text="Calculate", command=calculation)
button.grid(column="2", row="4")



window.mainloop()
