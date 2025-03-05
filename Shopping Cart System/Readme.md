# Shopping Cart System


## Overview
This is a simple Python-based shopping cart program designed to help users add items to their cart, specify quantities, and calculate the total cost. The program also generates a unique bill number and displays a formatted bill summary using ANSI escape codes for better visibility.

## Features
- Allows users to add multiple food items to their cart.
- Accepts user input for item name, quantity, and price.
- Calculates total cost based on item quantity and price.
- Displays a formatted bill summary with itemized details.
- Generates a unique bill number for each transaction.
- Uses ANSI escape codes for enhanced terminal display.

## Requirements
- Python
- random module

## Installation
1. Clone or download this repository.
2. Ensure you have Python installed on your system.
3. Run the script using the command:
   ```sh
       python SC_Adv.py
   ```

## Usage
1. Run the program.
2. Enter the name of the item you wish to buy.
3. Specify the quantity of the item.
4. Enter the price per unit.
5. The program will calculate the total price for the item and display the details.
6. Repeat the process for more items.
7. To finalize and generate the bill, enter 'q' when prompted for an item name.
8. The final bill will display all purchased items along with a unique bill number.

## Example
```
Enter your item name to Buy (..To exit press 'q')
 : Apple
Enter quantity of Apple you wish to purchase
 : 2
Enter the price (Rs) of Apple
 : 50

 Item - Apple
 Quantity - 2
 Total Price - 100 Rs

Enter your item name to Buy (..To exit press 'q')
 : q

Bill Number:  1234
____________ Your  Cart _____________
Food           |Quantity  |Price     
------------------------------------
Apple          |2         |100       
------------------------------------
      Your total is: Rs 100

   Thank you for shopping with us!   
```
