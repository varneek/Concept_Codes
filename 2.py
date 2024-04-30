#binary search
nums=[]
c=0
for i in range(0,6):
    n=int(input('enter the elements='))
    elements=nums.append(n)
target=int(input('enter the target='))
nums.sort()
for i in range(0,6):
    if nums[i]==target:
        c=1
        print(i)
if c==0:
    print('-1')
    
        