#Creativity: I added formatting to make the item names
# and prices line up neatly when the cart is displayed.

item_names = []
item_prices = []

print("Welcome to the Shopping Cart Program!")

user_choice = 0

while user_choice != 5:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    user_choice = int(input("Please enter an action: "))

    if user_choice == 1:
        new_item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{new_item}'? "))

        item_names.append(new_item)
        item_prices.append(price)

        print(f"'{new_item}' has been added to the cart.")

    elif user_choice == 2:
        print("\nThe contents of the shopping cartare:")

        if len(item_names) == 0:
            print("Your cart is currently empty.")
        else:
            for i in range(len(item_names)):
                print(f"{i + 1}. {item_names[i]:<18} - ${item_prices[i]:.2f}")

    elif user_choice == 3:
        if len(item_names) == 0:
            print("Your cart is empty. There is nothing to remove.")
        else:
            print("\nThe contents of the shopping cart are")

            for i in range(len(item_names)):
                print(f"{i + 1}. {item_names[i]:<18} - ${item_prices[i]:.2f}")

            remove_index = int(input("Which item would you like to remove? "))
            actual_index = remove_index - 1

            if actual_index >= 0 and actual_index < len(item_names):
                del item_names[actual_index]
                del item_prices[actual_index]
                print("Item removed.")
            else:
                print("Sorry that is not a valid item number.")

    elif user_choice == 4:
        total_sum = 0

        for price in item_prices:
            total_sum += price

        print(f"The total price of the items in your cart is ${total_sum:.2f}")

    elif user_choice == 5:
        print("Thank you. Goodbye!")

    else:
        print("That is not a valid menu option. You can try again")

