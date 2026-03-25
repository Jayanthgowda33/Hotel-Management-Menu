#Define the menu of restaurant
menu = {
    'Pizza':40,
    'pasta':50,
    'Burger':70,
    'Salad' :70,
    'Coffee':80,
}
print(menu)

#Greet
print("Welcome to our Jayanth restaurant!")
print(" Pizza: Rs40\n, Pasta:Rs50\n, Burger:Rs70\n, Salad:Rs70\n , Coffee:Rs80\n")

order_total = 0
item_1 = input("Enter the first item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order. Current total: Rs{order_total}")
else:
    print(f"Sorry, we don't have {item_1} on the menu.")

    another_item = input("Do you want to order another item? (yes/no): ")
if another_item.lower() == 'yes':
    item_2 = input("Enter the second item you want to order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} added to your order. Current total: Rs{order_total}")
    else:
        print(f"Sorry, we don't have {item_2} on the menu.")