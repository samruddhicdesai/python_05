try:
    num = int(input("enter a number: "))
    result = 10/num
except(ZeroDivisionError , ValueError) as e:
    print(f"An error occured : {e}")