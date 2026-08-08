numbers = []
for i in range(5):
    num = int(input("Enter the number : "))
    numbers.append(num)
print("Lists is ",numbers)
print("Smallest number is ",min(numbers))
print("Largest number is ",max(numbers))
numbers.reverse()
print("Reversed is ",numbers)
