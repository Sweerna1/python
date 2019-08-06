print("LISTS AND DICTIONARIES TASK")
print("---------------------------")

print("Welcome to the special recuitment program, please answer the following questions:")
name = input("Name: ")
age = input("Age: ")
years = input("How many years of experience do you have? ")
print("Skills:")
skills = ['python', 'C++', 'JavaScript', 'Juggling', 'Running', 'Eating']

for i, item in enumerate(skills,1):
    print (i, '- ', item)

skill_1 = input("Choose a skill from above: ")
skill_2 = input("Cgoose another skill from above: ")

cv = {}
cv ['name'] = name
cv ['age'] = age
cv ['experience'] = years
cv ['skills'] = []

x1 = int(skill_1)
x2 = int(skill_2)

check1=0
check2=0
#--------------------------------#
if x1 == 1:
    cv ['skills'].append(skills[0])
elif x1 ==2:
    cv ['skills'].append(skills[1])
elif x1 ==3:
    cv ['skills'].append(skills[2])
elif x1 ==4:
    cv ['skills'].append(skills[3])
elif x1 ==5:
    cv ['skills'].append(skills[4])
elif x1 ==6:
    cv ['skills'].append(skills[5])
else:
    print("Invalid number")
    
if x2 == 1:
    cv ['skills'].append(skills[0])
elif x2 ==2:
    cv ['skills'].append(skills[1])
elif x2 ==3:
    cv ['skills'].append(skills[2])
elif x2 ==4:
    cv ['skills'].append(skills[3])
elif x2 ==5:
    cv ['skills'].append(skills[4])
elif x2 ==6:
    cv ['skills'].append(skills[5])
else:
    print("Invalid number")

print("---------------------------")
print("Your CV:")
print(cv)
print("---------------------------")

if int(age) > 25 and int(age) < 40 and int(years) >=3:
    check1 = 1
else:
    check1 = 0

for k in cv:
    for v in cv[k]:
        if 'python' in v:
            check2 = 1
      #  else:
      #      check2 = 0

#print(check1)
#print(check2)
      
if check1 and check2 == 1:
    print("You have been accpeted,",name.title())
else:
    print("You haven't been accepted")

print("END")
