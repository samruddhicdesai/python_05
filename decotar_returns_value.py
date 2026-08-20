def decorator(add):
    def wrapper(*args,**kwargs):
        print("Running")
        result = add(*args,**kwargs)
        print("Done")
        return result
    return wrapper

@decorator
def add(a,b):
    return a+b

result = add(10,20)
print(result)