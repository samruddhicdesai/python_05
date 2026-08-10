def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older")
    return "access granted"

try:
    print(check_age(1))

except ValueError as e:
    print("Error :",e)