""" 
Problem 1: Even or Odd

Write a Python program that:

Takes a number from the user
Prints whether the number is even or odd
"""

try:
    num = int(input("Enter a Number: "))

    if num%2==0:
        print("The number {num} is even")
    else:
        print("The number {num} is odd")

except:
    print("Invalid Number")



"""
Write a program that:

Takes numbers from the user continuously
Stops when the user enters 0
Prints the total sum
"""

total =0
while True:
    try:
        num = int(input("Enter Number: "))
        if num==0:
            print("Sum is: ", total)
            break
        else:
            total += num
    except:
        print("Invalid Number")



"""
Takes 3 numbers as input
Prints the largest number
"""

num = []
try:
     for i in range(3):
          x = int(input(f"Enter number {i+1} "))   
          num.append(x)
except:
    print("invalid Number!")

if num[0]>num[1] & num[0]>num[2]:
    print(f"The largest numner is {num[0]}")
elif num[1]>num[0] & num[1]>num[2]:
    print(f"The largest numner is {num[1]}")
else:
    print(f"The largest numner is {num[2]}")
    


"""
Write a program that:

Takes two numbers and an operator (+, -, *, /)
Performs the calculation
Prints the result
"""

try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
except:
    print("Invalid Number!")

operator = input("Enter operator (+, -, *, /: ")

if operator =="+":
    print (f"The sum of these number is = {num1 +num2}")
elif operator =="-":
    print (f"The minus of these number is = {num1 - num2}")
elif operator =="*":
    print (f"The multification of these number is = {num1 * num2}")
elif operator =="/":
    print (f"The divison of these number is = {num1/num2}")
else:
    print("invalid operator")


"""
Problem 5 (Slightly Challenging): Count Digits

Write a program that:

Takes a number (like 12345)
Counts how many digits it has
Prints the count
"""
try:
    num5 = int(input("Enter number 1: "))
except:
    print("Invalid Number!")
print(f"The length of the number is: {len(str(num5))}")