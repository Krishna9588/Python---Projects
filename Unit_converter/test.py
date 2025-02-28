def length():
    # Function to handle length
    pass

def weight():
    # Function to handle weight
    pass

def temperature():
    # Function to handle temperature
    pass

def time():
    # Function to handle time
    return 0

# Dictionary to map options to functions
options = {
    1: length,
    2: weight,
    3: temperature,
    4: time
}

while True:
    # Get user input
    try:
        a = int(input("Enter your choice (1: Length, 2: Weight, 3: Temperature, 4: Time, 0: Exit): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if a == 0:
        print("Exiting...")
        break
    elif a in options:
        options[a]()
    else:
        print("Invalid Input")
