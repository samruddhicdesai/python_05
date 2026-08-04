color = input("Enter the color = ")

match color:
    case "red":
        print("STOP")
    case "yellow":
        print("GET READY")
    case "green":
        print("GO")
    case _:
        print("Invalid color")
    