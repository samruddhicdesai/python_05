total = 0
for i in range(1,6):
    marks = int (input(f"Enter the marks {i} = "))
    total += marks

average = total/5
print("Total = ",total)
print("Average = ",average)