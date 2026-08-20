
def decorator(name):
    def wrapper():
        print("Starting...")
        name()
        print("Ending....")
    return wrapper

@decorator
def name():
    print("SAM")

name()
