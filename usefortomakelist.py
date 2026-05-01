marks = []

for i in range(5):
    num = int(input(f"Enter mark {i+1}: "))
    marks.append(num)

avg = sum(marks) / len(marks)
print("Average:", avg)

if avg >= 80:
    print("Grade: A")
elif avg >= 70:
    print("Grade: B")
elif avg >= 60:
    print("Grade: C")
elif avg >= 50:
    print("Grade: D")
else:
    print("Grade: F")