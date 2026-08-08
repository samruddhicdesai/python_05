cart = []

while True:
    print("\n 1. Add item")
    print("2. Remove item")
    print("3. show cart")
    print("4. Exit")

    choice = int(input("Enter the choice : "))

    if choice == 1:
        item = input("Enter item : ")
        cart.append(item)
        print("item added")
    elif choice == 2:
        item = input("Enter item to remove : ")
        if item in cart:
            cart.remove(item)
            print("item removed")
        else:
            print("item not found")

    elif choice == 3:
        print("cart = ",cart)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")