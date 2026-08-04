correct_pin = "4424"

while True:
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Login Successful")
        break
    else:
        print("Wrong PIN")