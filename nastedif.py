#use of nested if
x=int(input("enter 1st no."))
y=int(input("enter 2nd no."))
z=int(input("enter 3rd no."))
if x>y:
    if x>z:
        print('1st is greatest:-',x)
    else:
        print('3rd is greatest:-'.z)
else:
    if y>z:
        print('2nd is greatest:-',y)
    else:
        print('3rd is greatest:-',z)