#Take a number from the user and check whether it is prime or not.

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number")

elif num == 2:
    print(f"{num} is a prime number")

else:
    for i in range(2, num):

        if num % i == 0:
            print(f"{num} is not a prime number")
            break

        elif num == i + 1:
            print(f"{num} is a prime number")
        

#------------------------------------------------Another way-------------------------------------------------

num = int(input("Enter a number: "))

if num > 1:

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number")
        print(i)
    else:
        print(f"{num} is not a prime number")
        print(i)

else:
    print(f"{num} is not a prime number")


  
#Take a sentence and count: uppercase letters and lowercase letters


text = input("Enter a sentence: ")

upcount = 0
lowcount = 0

for i in text:

    if i.isupper():
        upcount += 1

    elif i.islower():
        lowcount += 1

print("Uppercase:", upcount)
print("Lowercase:", lowcount)


"""
Ask the user for a password repeatedly until they enter: python123
             If wrong: Wrong password
             If correct: Access granted
"""

while True:
    password = input("Enter Password: ")
    if password == "python123":
        print("Access granted")
        break
    else:
        print("Wrong password")






"""
Print this pattern using loops:

*
**
***
****
*****

"""

n = int(input("Enter n: "))
star = ""
for i in range(n):
    star = star + "*"
    print(star)

'-----------------------------------------------------------------Another way-------------------------------------------------'

n = int(input("Enter n: "))
for i in range(1, n + 1):
    print("*" * i)




# Take n numbers from the user and find the second largest number. 
# If all numbers are the same: No second largest number

numbers = []

n = int(input("Enter n: "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = numbers[0]
second_largest = numbers[0]

for i in numbers:

    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest and i != largest:
        second_largest = i

if largest == second_largest:
    print("No second largest number")

else:
    print("Second largest number is:", second_largest)