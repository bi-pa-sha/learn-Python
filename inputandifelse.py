ban = int (input ("Enter your Bangla number:"))
eng = int (input ("Enter your English number:"))
math = int (input ("Enter your Math number:"))
sci = int (input ("Enter your Science number:"))
gk = int (input ("Enter your General Knowladge number:"))

if (0 <= ban <= 100 and 0 <= eng <= 100 and 
    0 <= math <= 100 and 0 <= sci <= 100 and 
    0 <= gk <= 100):
    avg = (ban + eng + math + sci + gk )/5
    print( " The Average number is" , avg)
else:
    print("Invalid marks")
    
if 80 <= avg <= 100 :
    print ("The grade is A")
elif 70 <= avg < 80 :
    print ("The grade is B")

elif 60 <= avg < 70  :
    print ("The grade is C")

elif 50 <= avg < 60 :
    print ("The grade is D")

elif 0 <= avg < 50 :
    print ("The grade is F")
     
else:
    print ("The grade is invalid")