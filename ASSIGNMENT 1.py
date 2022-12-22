## Question 1 ##
a = int(input("Enter the First Number: "))
b = int(input("Enter The Second Number: "))
c = int(input("Enter the Third Number: "))
average = (a+b+c)/3
print("Average of the Three Numbers is", average)


## Question 2 ##
a=int(input("Enter your Annual Income: "))
b=int(input("Enter number of dependents: "))
taxable_income=a-10000-(3000*b)
tax=taxable_income*20/100
print("Total tax is Rs.",tax,"/-")

# # QUESTION: 3 # #
s=int(input("Enter the number of seconds: "))
m=s//60
s=s%60
print(m,"minutes",s,"seconds")

# # QUESTION: 4 # #
a=int(25)
b=int('25')
c=int(25.0)
result=str(a+b+c)
print(result)
print(type(result))

# # QUESTION: 5 # #
from math import *
for i in range (0,360,15):
    print(i,'----',round(sin(i),4), round(cos(i),4))