def greet():
    print("Hello")

def decorator(greet):
    def wrapper():
        print("Before Function")
        greet()
        print("After Function")

    return wrapper

new_greet = decorator(greet)

new_greet()