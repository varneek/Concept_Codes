#fabonic series 0 1 1 2 3 5 8------n
prev=0
next=1
n=int(input('enter till how much fabonic number you want:-'))
print(prev)
print(next)
for x in range(2,n):
    sum=prev+next
    print(sum)
    prev=next
    next=sum

