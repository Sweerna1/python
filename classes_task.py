from datetime import date
print("CLASSES TASK")
print("Welco to HR Pro 2019")

class Employee:
    def __init__(self, name, age, salary, year):
        self.name = name
        self.age = age
        self. salary = salary
        self.year = year
        
    def get_working_years(self): #--------------1
        today = date.today()
        return (today.year - int(self.year))
    
    def __str__(self):
        return ("Name: %s, Age: %s, Salary: %s, Working years: %s" % (self.name, self.age, self.salary, self.get_working_years()))

         
class Manager(Employee):
    def __init__(self, name, age, salary, year, bonus):
        Employee.__init__(self, name, age, salary, year)
        self.bonus = bonus

    #def get_working_years(self): #-----------------2
     #   today = date.today()
      #  return (today.year - int(self.year))
        

    def get_bonus(self):
        return (float(self.bonus) * int(self.salary))

    def __str__(self):
        return("Name: %s, Age: %s, Salary: %s, Working years: %s, Bonus: %s" % (self.name, self.age, self.salary, self.get_working_years(), self.get_bonus()))


        

Emp = []
Mang = []

while True:
    print("Choose an action to do:")
    print("1. Show employees")
    print("2. Show managers")
    print("3. Add an rmployee")
    print("4. Add a manager")
    print("5. Exit")
    choice = input("What whould you like to do? ")
    print("---------------------------------")
    ch = int(choice)

    if ch == 1:
        print("Employees")
        for i in Emp:
            print(i)
        
            
    elif ch == 2:
        print("Managers")
        for i in Mang:
            print(i)
            
    elif ch == 3:
        name = input("Name: ")
        age = input("Age: ")
        salary = input("Salary: ")
        year = input ("Employement year: ")
        p = Employee(name, age, salary, year)
        Emp.append(p)
        
    elif ch == 4:
        name = input("Name: ")
        age = input("Age: ")
        salary = input("Salary: ")
        year = input ("Employement date: ")
        bonus = input("Bonus percentage: ")
        q = Manager(name, age, salary, year, bonus)
        Mang.append(q)
        
    elif ch == 5:
        break
    else:
        print("Invalid number")
    

    

    

