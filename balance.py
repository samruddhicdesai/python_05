balance = 10000

deposit = int(input("Enter deposit amount: "))
balance += deposit

withdraw = int(input("Enter withdrawal amount: "))
balance -= withdraw

print("Current Balance =", balance)