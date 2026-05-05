"""Write a program that:

Takes a list of numbers
Prints only the even numbers
"""

numbers = []

try:
    n = int(input("Enter how many numbers you want to put in a list: "))
    
    for i in range(n):
        try:
            inputnum = int(input(f"Enter input {i+1}: "))
            if inputnum % 2 == 0:
                numbers.append(inputnum)
        except ValueError:
            print("Invalid number!")

    print("Even numbers are:", numbers)

except ValueError:
    print("Invalid number for list size!")




"""
Write a program that:

Takes a string from the user
Counts how many vowels (a, e, i, o, u) are in it
"""

count = 0

txt = input("Enter a string: ")

for ch in txt:
    if ch.lower() in "aeiou":
        count += 1

print(f"There are {count} vowels")








"""
Write a program that:

Takes a number from the user
Prints its multiplication table up to 10
"""

try:
    num = int(input("Enter a number: "))
    for i in range(1,11):
        print(f"{num} * {i} = {num *(i)}")
except ValueError:
    print("Error Value")

 


"""     
Write a program that:
Takes a number (like 1234)
Prints it in reverse (4321)
"""

num = input("Enter a number: ")
reverse = num[::-1]
print("Reversed number is:", reverse)






"""
Write a program that:
Takes a list of numbers
Finds and prints the smallest number

"""
num = []
n = int(input("How many values do you want? "))

for i in range(n):
    value = int(input("Enter a number: "))
    num.append(value)

largest = num[0]

for i in num:
    if i > largest:
        largest = i

print("The largest number is:", largest)