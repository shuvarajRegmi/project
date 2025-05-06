menu={
    'pizza':250,
    'pasta':150,
    'Burger':195,
    'coffee':85,
}
print("Welcome to KFC")
print("pizza:Rs.250\npasta:Rs.150\nBurger:Rs.195\ncoffee:Rs.85 ")
order_total=0
item_1=input("Enter the name of the item:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"order item {item_1} is not available yet!")
another_order=input("Do you want to add another item ?(yes/no)")
if another_order=="yes":
    item_2=input("enter the name of second item:")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"order item {item_2} is not available! ")
print(f"The total amount of item is {order_total}")
    
    