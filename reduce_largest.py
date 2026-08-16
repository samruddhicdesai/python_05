from functools import reduce

numbers = [1,4,3,63,34,73]

result = reduce(lambda a,b: a if a>b else b,numbers)

print(result)