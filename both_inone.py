def student(name,*marks,**details):
    print("Nmame:",name)
    print("Marks:",marks)
    print("Other details:",details)

student(
    "sam",
    80,
    90,89,
    branch = "CSE",
    roll_no = 12
)