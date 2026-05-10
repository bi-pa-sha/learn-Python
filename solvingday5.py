
# Take n numbers from the user and create a new list without duplicates.
#👉 Example: Input: 1 2 2 3 4 4 5 Output: [1, 2, 3, 4, 5]


n = int(input("Enter the value of n: "))

numbers = []

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Original list:", numbers)

unique_numbers = []

for i in numbers:
    if i not in unique_numbers:
        unique_numbers.append(i)

print("List without duplicates:", unique_numbers)






#Take n numbers from the user and calculate the average.

n = int(input("Enter the value of n: "))

numbers = []

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = 0
avg = 0

for i in numbers:
    total += i

avg = total/n
print("The average is = ", avg)






#Take n numbers from the user and print both the largest and smallest numbers.

n = int(input("Enter the value of n: "))

numbers = []

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("The smallest number is:", smallest)
print("The largest number is:", largest)






#Take two lists from the user and print the common elements.

n1 = int(input("Enter the value of n in list 1: "))

first_list = []

for i in range(n1):
    num = int(input("Enter a number: "))
    first_list.append(num)

n2 = int(input("Enter the value of n in list 2: "))

second_list = []

for i in range(n2):
    num = int(input("Enter a number: "))
    second_list.append(num)

common_elements = []

for i in first_list:
    if i in second_list:
        common_elements.append(i)

print("The common elements are:", common_elements)