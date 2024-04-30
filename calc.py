#simple calculater 
from ast import For


print("press 1 for addition")
print("press 2 for substract")
print("press 3 for multiplication")
print("press 4 for division")
n=int(input("enter number:-"))
a=int(input("enter the first number for caluclation:-"))
b=int(input("enter the second number for caluclation:-"))
if n==1:
    c=a+b
    print('the sum of both number=',c)
elif n==2:
    c=a-b
    print('the sub of both number=',c)
elif n==3:
    c=a*b
    print('the multiplication of both number=',c)
elif n==4:
    c=a/b
    print('the division of both number=',c)
else:
    print('invalid input')
