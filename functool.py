from functools import wraps

def decorator(fuction):
    @wraps(function)
    def wrapper(*args,**kwargs):
        return function(*args,**kwargs)

    return wrapper