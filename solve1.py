#get 9=6 and 6=9
n=int(input('enter no.'))
copy=n
f=0
c=1
while n>0:
    b=n%10
    if b==6:
        b=9
    d=c*b
    final=d+f
    f=final
    e=c*10
    c=e
    n=n//10
amount=final-copy
print('amount =',final,'-',copy,'=',amount)