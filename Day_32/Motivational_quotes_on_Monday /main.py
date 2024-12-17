import datetime as dt
import random
today = dt.datetime.today()
weekday = today.weekday()
if weekday == 1: #testing if the current day is Monday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines() # placing the whole content of a file into a list
        quote = random.choice(all_quotes) # choosing a random quote




import smtplib

my_email = "email@gmail.com"
password = "vpck hxvh ijpp fdpc"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="anotheremail@gmail.com", msg=quote)
connection.close()

