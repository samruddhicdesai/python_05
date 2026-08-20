def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before Function")
        func(*args, **kwargs)
        print("After Function")
    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("SAM")