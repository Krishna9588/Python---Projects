class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"

    def mod(self, a, b):
        try:
            return a % b
        except ZeroDivisionError:
            return "Cannot modulo by zero"

    def exponent(self, a, b):
        return a ** b

calc = Calculator()

while True:
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    operation = input("Enter operation (+, -, *, /, %, **): ")

    if operation == '+':
        print(calc.add(a, b))
    elif operation == '-':
        print(calc.sub(a, b))
    elif operation == '*':
        print(calc.mul(a, b))
    elif operation == '/':
        print(calc.div(a, b))
    elif operation == '%':
        print(calc.mod(a, b))
    elif operation == '**':
        print(calc.exponent(a, b))
    else:
        print("Invalid operation")

    if input("Do you want to calculate again (y/n)? ").lower() != 'y':
        break

#
