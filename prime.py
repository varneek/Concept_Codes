#find prime no. or not
def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c=1
            return 'not prime'
    if c==0:
        return 'prime'
def sum(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def multi(a,b):
    c=a*b
    return c
def div(a,b):
    c=a//b
    return c