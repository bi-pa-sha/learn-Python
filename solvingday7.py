#Print the first n numbers of the Fibonacci series.
n = int(input("Enter the number of terms: "))
s1=0
s2 =1
print(s1, end=" ")
print(s2, end=" ")
for i in range(2,n):
    s3= s1+s2
    print(s3, end=" ")
    s1=s2
    s2=s3




# Write a program to check whether a number is prime or not
n = int(input("Enter a Number: "))

if n < 2:
    print(f"{n} is not a valid number for prime checking")

elif n == 2:
    print(f"{n} is a prime number")

else:
    prime = True

    for i in range(2, n // 2):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")



#Create a simple password checker.
# A password is strong if: length is at least 8, contains one uppercase letter, lowercase letter, digit
password = input("Enter Password: ")

has_upper = False
has_lower = False
has_digit = False

for ch in password:

    if ch.isupper():
        has_upper = True

    elif ch.islower():
        has_lower = True

    elif ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Password is strong")

else:
    print("Password is weak")





#Reverse a Number
n = int(input("Enter a Number: "))
m = str(n)
print(m[::-1])




#Count Words in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Total words:", len(words))