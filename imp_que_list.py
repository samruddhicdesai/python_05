numbers = []
for i in range(10):
    nums = int(input("Enter numbers : "))
    numbers.append(nums)
print("Original list :",numbers)
numbers.sort()
print("Sorted list : ",numbers)
print("Largest number : ",max(numbers))
print("smallest number :",min(numbers))
print("Total : ",sum(numbers))
print("Average : ",sum(numbers)/10)