#null statement:- it will be used in function if you don't know what to write  in it then write pass keyword in it. from this we will know we need to code in it later
#it is just place holder for the code which is to be implimented in future
def none(a,b):
    pass 
#lambda function:- it will be used only in one line code in which return is used
add=lambda a,b: a+b
print(add(int(input('enter number to add:-')),int(input('enter number to add'))))
#conditional operator in python:-
#c=a if a>b else b
max=lambda a,b:a if a>b else b 
print(max(int(input('enter number:-')),int(input('enter number'))))