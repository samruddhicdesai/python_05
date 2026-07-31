num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition      :", num1 + num2)
print("Subtraction   :", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division      :", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Modulus       :", num1 % num2)
else:
    print("Division, Floor Division, and Modulus are not possible because the second number is 0.")

print("Power         :", num1 ** num2)