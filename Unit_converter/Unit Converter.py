'''
1. **Length Conversion**
   Example: Converting 1000 meters to kilometers
   Result: 1000 meters = 1 kilometer

2. **Weight Conversion**
   Example: Converting 500 grams to kilograms
   Result: 500 grams = 0.5 kilograms

3. **Temperature Conversion**
   Example: Converting 100°C to Fahrenheit
   Result: 100°C = 212°F

4. **Time Conversion**
   Example: Converting 2 hours to minutes
   Result: 2 hours = 120 minutes
'''
def length():
    print("\nWhat do you want to convert\n"
          "for kilometers to meters - 1\n"
          "for meters to kilograms - 2\n")
    b = int(input("Enter your choice: "))
    c = int(input("Enter your value to convert = "))
    if b == 1:
        print(c * 1000,"m\n")
    else:
        print(c / 1000,"km\n")

def weight():
    print("\nWhat do you want to convert\n"
          "for kilograms to gram - 1\n"
          "for gram to kilograms - 2\n")
    b = int(input("Enter your choice: "))
    c = int(input("Enter your value to convert = "))
    if b == 1:
        print(c * 1000,"g\n")
    else:
        print(c / 1000,"kg\n")

def temperature():
    print("\nWhat do you want to convert\n"
          "for Celsius to Fahrenheit - 1\n"
          "for Fahrenheit to Celsius  - 2\n")
    b = int(input("Enter your choice: "))
    c = float(input("Enter your value to convert = "))
    if b == 1:
        print((c*1.8)+32,"°F\n")
    else:

        print((c/1.8)-32,"°C\n")

def time():
    print("\nWhat do you want to convert\n"
          "from hours to minutes - 1\n"
          "from hours to seconds - 2\n"
          "from minutes to hours - 3\n"
          "from minutes to seconds - 4\n"
          "from seconds to hours - 5\n"
          "from seconds to minutes - 6\n")
    b = int(input("Enter your choice: "))
    c = int(input("Enter your value to convert = "))
    if b == 1:
        print(c * 60,"min\n")
    elif b == 2:
        print(c * 3600,"sec\n")
    elif b == 3:
        print(c / 60,"hr\n")
    elif b == 4:
        print(c * 60,"sec\n")
    elif b == 5:
        print(c / 3600,"hr\n")
    elif b == 6:
        print(c / 60,"min\n")
    else:
        print("Invalid Input\n")

print("_____Unit Converter Program_____")


options = {
    1: length,
    2: weight,
    3: temperature,
    4: time
}


while True:
    # Get user input
    try:
        a = int(input("For Length Conversion:      1\n"
                      "For Weight Conversion:      2\n"
                      "For Temperature Conversion: 3\n"
                      "For Time Conversion:        4\n"
                      "To Exit the Program :       0\n"
                      "Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    if a == 0:
        print("Exiting...\n")
        break
    elif a in options:
        options[a]()
    else:
        print("Invalid Input\n")



# a = int(input("For Length Conversion: 1\n"
#           "For Weight Conversion: 2\n"
#           "For Temperature Conversion: 3\n"
#           "For Time Conversion: 4\n"
#           "To Exit the Program : 0\n"
#           "Enter your choice: "))

# if a == 1:
#     length()
# elif a == 2:
#     weight()
# elif a == 3:
#     temperature()
# elif a == 4:
#     time()
# else:
#     print("Invalid Input")