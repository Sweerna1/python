print("CONDITION TASK")
print("The Calculator")

x = input("Enter the first number: ")
y = input("Enter the second number: ")

op = input("Choose the opertaion (+, -, /, *): ")

if x.isdigit() and y.isdigit():
    if op == "+":
        print ("The answer is " + str(int(x)+int(y)))
    elif op == "-":
        print ("The answer is " + str(int(x)-int(y)))
    elif op == "/":
        print ("The answer is " + str(int(x)/int(y)))
    elif op == "*":
        print ("The answer is " + str(int(x)*int(y)))
    else:
        print("Invalid operation!")
else:
    print("Invalid numbers, Enter two digit numbers")

print("END")

        
