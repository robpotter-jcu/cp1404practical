"""
Shop calculator program to provide total price of items including discount if applicable.
"""

total_price = 0
number_of_items = int(input("Enter number of items: "))
while number_of_items <= 0:
    print("Invalid number of items")
    number_of_items = int(input("Enter number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Enter price of item: "))
    total_price = total_price + price_of_item
if total_price > 100:
    total_price = total_price * 0.9
print("Total price of {} items is ${:.2f}".format(number_of_items, total_price))
