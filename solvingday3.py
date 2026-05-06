"""
Take a number and find the sum of its digits.

👉 Example:
Input: 123
Output: 6 (1+2+3)
"""


num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num / 10

print("Sum of digits:", sum)



'This method works well, but if the user enters something like -123, it will give an error because of '-'.'

num = input("Enter a number: ")
total = 0

for i in num:
    if i.isdigit():
        total += int(i)

print("Sum of digits:", total)


'-------------------------one line code-------------------'
num = 235
print(sum(int(i) for i in str(num)))


"""
Take a number and check if it is a palindrome (same forward and backward).
👉 Example:
Input: 121 → Output: Palindrome
Input: 123 → Output: Not Palindrome
"""


num = input("Enter a number: ")
reversenum = 0
for i in num:
    reversenum = num[:: -1]

if num == reversenum:
    print("Output: Palindrome")
else:
    print("Output: Not Palindrome")

    
    
"""
Take a number and find its factorial.
👉 Example:
Input: 5
Output: 120 (5 × 4 × 3 × 2 × 1)
"""

num = int(input("Enter a number: "))
fact = 1
for i in range(1,num+1):
    fact = fact*i

print("its factorial: ", fact)




"""
Take n numbers from the user and find the second largest number.
👉 Example:
Input: 10, 20, 5, 8
Output: 10
"""
n = int(input("how many numbers you want? "))
nums =[]
for i in range(n):
    num = int(input("enter number: "))
    nums.append(num)

second_largest = 0
largest = 0
for i in nums:
  if i > largest:
    second_largest = largest
    largest = i

print (second_largest)
