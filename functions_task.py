from datetime import date
print("FUNCTIONS TASK")
print("The Age Calculator")

def check_birthdate(y, m, d):
    today = date.today()
    if int(today.year) > int(y) or int(today.year) == int(y):
        return True
    else:
        return False

def calculate_age(y, m, d):
    birth_year = int(today.year) - int(y)
    birth_month = abs(int(today.month) - int(m))
    birth_day = abs(int(today.day) - int(d))
    print("You are " + str(birth_year) + " years, " + str(birth_month) + " months, and " + str(birth_day) + " days")

today = date.today()
print ("Today's date is: ", today)
print ("----------------------------")

year = input("Enter year of birth: ")
month = input("Enter month of birth: ")
day = input("Enter day of birth: ")
if check_birthdate(year, month, day):
    calculate_age(year, month, day)
else:
    print("You are in the future :)")




    
    
    
