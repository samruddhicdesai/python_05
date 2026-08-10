try:
    num = int(input("Enter number: "))
    result = 100/num
except ValueError:
    print("Please enter the number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result : ",result)
finally:
    print("program finished")