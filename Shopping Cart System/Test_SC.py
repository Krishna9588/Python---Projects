#shopping cart program
# simple understanding for the complex project

foods = []
prices = []
total = 0

while True:
    food = input("Enter your food item to Buy"
                 " (To exit press 'q')\n : ")
    if food.lower() == 'q':
        print("Thank you for shopping with us!")
        break
    else:
        foods.append(food)
        price = float(input(f"Enter the price (Rs) of a {food}\n : "))
        prices.append(price)

print("----- Your Cart -----")
for food in foods:
    print(food, end=",ri ")

for price in prices:
    total += price

print(f"\nYour total  is: {total} Rs")

