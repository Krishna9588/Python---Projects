#shopping cart program
# simple understanding for the complex project
import random
foods = []
quantity = []
prices = []
total = 0
bill_width = 52
while True:
    food = input("Enter your" + "\033[1;91m item name\033[0m" + " to Buy"
                 "\033[3;33m (..To exit press 'q')\n \033[0m: ")
    if food.lower() == 'q':
        # Start Space
        print(f"\033[1;4;31;107m{' ':<37}\033[0m")
        q = "\033[1;31;107m   Thank you for shopping with us!   \033[0m"
        print(q.center(bill_width))
        break
    else:
        foods.append(food)
        qty = int(input("Enter"+ "\033[1;91m quantity of \033[0m" + f"\033[1;93m{food}\033[0m" + " you wish to purchase\n : "))
        while True:
            if qty == 1 :
                quantity.append(qty)
                price = float(input("Enter the" + " \033[1;91m price (Rs)\033[0m of "+ f"\033[1;93m{food}\n\033[0m : "))
                prices.append(price)
                print(f"\033[1;93m Item - {food}\n"
                      f" Quantity - {qty}\n"
                      f" Total Price - {int(price)} Rs\033[0m")
                break
            elif qty <= 0:
                print("\033[1;107;31m--Invalid quantity!--\033[0m")
                foods.remove(food)
                break
            else:
                quantity.append(qty)
                price = float(input("Enter the" + " \033[1;91m price (Rs)\033[0m of "+ f"\033[1;93m{food}\n\033[0m : "))
                f_price = price*qty
                prices.append(f_price)
                print(f"\033[1;93m Item - {food}\n"
                      f" Quantity - {qty}\n"
                      f" Total Price - {int(f_price)} Rs\033[0m")
                break


# Bill Number.
bill_number = random.randint(1000, 9999)
print(f"\033[1;31;107m{'Bill Number: ':30}{bill_number:<7}\033[0m")
# Header of Bill.
header = "\033[1;31;107m____________ Your  Cart _____________\033[0m"
print(header.center(bill_width))
#Bill Column Header.
print(f"\033[1;31;107m{'Food':<15}|{'Quantity':<10}|{'Price':<10}\033[0m")
# Elements of cart.
for food, qty, price in zip(foods, quantity, prices):
    print(f"\033[1;31;107m{food:<15}|{qty:<10}|{int(price):<10}\033[0m")
# Counting and printing Total amount of cart.
for price in prices:
    total += price
print(f"\033[1;31;107m{'      Your total is: Rs ':<24}{int(total):<13}\033[0m")
#End Space
print(f"\033[1;4;31;107m{' ':<37}\033[0m")