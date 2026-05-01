marks = []
for d in range (5):
    if d == 1:
        num = int (input ("Enter Bangla marks "))
        marks.append(num)
    elif d == 2:
        num = int (input ("Enter english marks "))
        marks.append(num)
    elif d == 3:
        num = int (input ("Enter Math marks "))
        marks.append(num)
    else:
        num = int (input ("Enter marks "))
        marks.append(num)

print(marks)

avg = sum(marks)/5
print(avg)