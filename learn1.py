n = int(input("How many subjects? "))
marks = []

for i in range(n):
    while True:
        num = int(input(f"Enter mark {i+1}: "))
        
        if 0 <= num <= 100:
            marks.append(num)
            break
        else:
            print("Invalid input! Enter marks between 0 and 100.")
            
avg = sum(marks) / n
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