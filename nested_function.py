def outer():
    def inner():
        print("Inside Inner")
    inner()

outer()