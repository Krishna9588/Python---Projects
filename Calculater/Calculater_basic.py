print("_______Calculator_______")
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def mod(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Cannot modulo by zero"

def cal(a, b):
    c = int(input("To perform the operation on the provided input\n" +
                  "1 - Addition\n" +
                  "2 - Subtraction\n" +
                  "3 - Multiplication\n" +
                  "4 - Division\n" +
                  "5 - Remainder\n" +
                  "Choose one option: "))
    if c == 1:
        print(add(a, b))
    elif c == 2:
        print(sub(a, b))
    elif c == 3:
        print(mul(a, b))
    elif c == 4:
        print(div(a, b))
    elif c == 5:
        print(mod(a, b))
    else:
        print("Invalid option")

while True:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    cal(a, b)
    if input("Do you want to calculate again (y/n)? ").lower() != 'y':
        break
