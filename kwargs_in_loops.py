def student(**kwargs):
    for key, value in kwargs.items():
        print(key,"=",value)

student(name="sam",age = 20)