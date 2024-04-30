#generator function:- it will define as normal function *yeild* will define it is generator
def genratevalue():
    yield 10 
    yield 20
obj=genratevalue() #-> when we call generator we will get object
data=next(obj)  #-> next will go next and then give next value in yield
print(data) 
data=next(obj)
print(data)     
#---------------------------------------------------------------&&----------------------------------------------------------------------------
def generate(a,b):
    for x in range(a,b+1):
        if x%2==0:
            yield x
    if a>=b:
        yield 'starting number should be smaller then ending number'
try:
    obj=generate(int(input('enter the number from were you want to start:-')),int(input('enter the number from were you want to end:-')))
except ValueError:
    print('only numbers can be entered')
for y in obj:
    print(y,end=",")

