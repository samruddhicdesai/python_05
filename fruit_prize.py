fruit = input("Enter the Fruit : ")
match fruit:
      case "apple":
           print("120/kg")
      case "mango":
            print("200/kg")
      case "banana":
            print("50/dozen")
      case _:
            print("Fruit is not available") 