try:
    num = int(input("Enter number : "))
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("You can't divide y zero!")
except ValueError:
    print("Invalid input ! please enter a number.")