#enter three no. and find greatest
x=int(input("enter 1st no."))
y=int(input("enter 2nd no."))
z=int(input("enter 3rd no."))
if x>=y and x>=z:
    print('1st is greatest no.',x)
elif y>=x and y>=z:
    print('2nd is greatest no.',y)
elif z>=x and z>=y:
    print('3rd is greatest no.',z)
