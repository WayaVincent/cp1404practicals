"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
"""


number_of_items = int(input("Please enter the number of items you would like to purchase: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Please enter the number of items you would like to purchase: "))
total = 0
for i in range (1, number_of_items+1, 1):
    item_price = float(input(f"Price of item {i}: $"))
    total = total + item_price
    print()
if total > 100:
    total = total*0.9
print(f"Customer total is ${total:.2f}")
print()
