choice = int(input("Enter your choice = "))
match choice:
    case 1:
        print("Balance")
    case 2:
        print("Deposit")
    case 3:
        print("Withdraw")
    case _:
        print("Invalid")