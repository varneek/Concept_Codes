#1 min and max
data=[20,10,30,43,25,33,20]
n=min(data)
m=max(data)
#2 sort:- it will sort the collection assending to decending deafult 
data.sort()
#if you want to sort decending to assending then:-
data.sort()
data.reverse()
#3 clear
value=[20,10,30,43,25,33]
value.clear()
#4 remove
data.remove(10)
print(data)
#5 append:-enter additnioal element at the last position
data.append(10)
#6 insert:-it will assign elements position and element in collection
data.insert(3,45)
#7 pop:-it will remove and return the element and write index no. to remove 
g=data.pop(3)
print(g)
#8 count:- it will show how many dublicate numbers we have in collection
h=data.count(20)
print(h)
#9 index:- it will give index number of element we want 
d=data.index(30)
print(d)
