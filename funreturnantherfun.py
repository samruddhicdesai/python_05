def outer():
    def inner():
        print("Hello")

    return inner

x = outer()
x()