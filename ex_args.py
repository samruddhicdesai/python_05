def add(*args):
    total = 0

    for numbers in args:
        total += numbers

    return total
print(add(1,2,3,4,5))