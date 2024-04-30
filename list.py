#collections:-1) list
data=[12,532,2.234,'hello']
print(data[0])
for i in range(0,len(data)):
    print(data[i])
for a in range(0,-1*(len(data)+1),-1):
    print(data[a])
#list in list
values=[[10,20,30],[40,50,60],[70,80,90]]
for x in values:
    for y in x:
        print(y,end=' ')
    print('')