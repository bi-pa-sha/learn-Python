"""
A number is called an Armstrong number if:
Sum of each digit raised to the power of total digits = original number

👉 Example:
153 → 1³ + 5³ + 3³ =153
Output: Armstrong Number

"""


num = int(input("Enter a number: "))

calnum = num
total = 0
digits = len(str(num))

for i in range(digits):
    a = calnum % 10
    calnum = calnum // 10
    total = total + (a ** digits)

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number!")







#Take n numbers from the user and sort them manually using loops.
#👉 Example: Input: 5 2 8 1         Output: 1 2 5 8


n = int(input("Enter the value of n :"))

numbers =[]
for i in range(n):
    num = int(input(f"Enter {i+1} no number: "))
    numbers.append(num)

sortnumbers =[]

while len(numbers)>0:

    smallest = numbers[0]
    
    for i in numbers:
        if i < smallest:
            smallest =i
    
    sortnumbers.append(smallest)
    numbers.remove(smallest)

print(sortnumbers)








#Take a list and rotate it to the right by 1 position.
#👉 Example: Input: [1, 2, 3, 4]            Output: [4, 1, 2, 3]


n = int(input("Enter the value of n: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter {i+1} no number: "))
    numbers.append(num)

newlist = []
newlist.append(numbers[-1])

for i in range(len(numbers)-1):
    newlist.append(numbers[i])

print(newlist)






"""
Your task is to process some data. You are given 3 integers a , b , c and a string s. Output result of a+b+c and string s with a half-width break.

Input: 
1
2 3
hello

Output:
6 hello
"""

a = int(input())
b, c = map(int, input().split())
s = input()
print(a + b + c, s)

