#Exercise 9 
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

user_input = int(input("Enter a year: "))

if is_leap_year(user_input):
    print("Leap year")
else:
    print("Not a leap year")