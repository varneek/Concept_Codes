#1) the exception is an unexpected event that intrupts normal flow of pogramm 
#2) to continue rest of the pogramm in on alternate way is execption handeling
#try and except:- both are block like if and loops 
#try:
#  body -> write problem here
#except:
#  body -> handle problem here

try:
    x=int(input('enter number:-'))
    y=int(input('enter number:-'))
    z=x/y 
    print(z)
except ZeroDivisionError:
    print("can't divide by 0")
except ValueError as v:
    print('only numbers are allowed')
    print(v)
#exception has all the error in it we can use that to know which error we need to put 
#raise:- if we need to make our error then we will use raise 
#example:- 
def checkage(age):
    if age>=18:
        print('eligible')
    elif age>0:
        print('not eligible')
    else:
        raise Exception('negative age given')
try:
    checkage(int(input('enter age:-')))
except Exception as e:
    print(e)
#finally:- it will always execute not like except
try:
    print('hello')
    x=2
    y=0
    z=x/y
    print(z)
finally:
    print('bye')
#we can also use except with try and finally on the sequance of try,except,finally
