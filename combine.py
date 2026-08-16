from functools import reduce

numbers = [1,2,3,4,5,32,12,45,65]

even = filter(lambda x:x%2==0,numbers)

square = map(lambda x:x**2,numbers)

total = reduce(lambda a,b:a+b,numbers)
print(total)