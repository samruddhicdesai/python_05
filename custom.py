class InvalidAgeError(Exception):
    pass

def Verify(age):
    if age < 18:
        raise InvalidAgeError("Age must be greater then 18")

    return "welcome"


try:
    print(Verify(8))

except InvalidAgeError as e:
    print("Error : ",e)

