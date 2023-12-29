# Conditions for a leap year:
# A year is a leap year if it is divisible by 4.
# However, if the year is also divisible by 100, it is not a leap year unless it is divisible by 400.


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1] # - 1 because list starts with index 0


  
year = int(input("Input the year: ")) 
month = int(input("Input the month: ")) 
days = days_in_month(year, month)
print("There are " + str(days) + " days.")
