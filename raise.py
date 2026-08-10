def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older")
    return "Access granted"

print(check_age(4))