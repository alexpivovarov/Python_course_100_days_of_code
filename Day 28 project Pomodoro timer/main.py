from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer) # cancels any scheduled "after" call that is currently running. It effectively stops the countdown if the timer is running.
    canvas.itemconfig(timer_text, text= "00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer(): # calls count_down function when trigerred
    global reps #  indicating that a variable declared inside a function refers to a variable defined in the global scope
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep
    if reps % 8 == 0:
        count_down((long_break_sec))
        title_label.config(text="Long Break", fg=RED)
    # If it's the 1st/3rd/5th/7th rep:
    elif reps % 2 == 1:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    # If it's the 2nd, 4th, 6th rep
    else:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60) # returns the largest integer less than or equal to 60
    count_sec = count % 60
    # Without the following two lines timer will show 5:0, 3:0 ... instead of 5:00, 3:00  and 2:1, 0:7 instead of 2:01, 0:07
    if count_sec < 10:  # Using dynamic typing. Data type of count_sec is changed from integer to a string
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2) # Using math.floor ensures we get an integer value rounding down to the nearest whole number
        for _ in range(work_sessions): # A loop that runs "work_sessions" times
            marks += "✔"
        check_marks.config(text=marks)

# ----------------------------- UI SETUP --------------------------------------#

window = Tk()
window.title("Pomodoro")
window.geometry("500x500")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50)) # fg - foreground
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # these values of width and height were chosen because tomato.png has size 200x223
tomato_img = PhotoImage(file="tomato.png") # storing an image
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer) # when user presses start_button start_timer is called
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()