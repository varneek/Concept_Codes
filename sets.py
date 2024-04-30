#sets:-it doesn't allow dublicates, it not have index,  it is unodered,  it is changeable
s1={10,23,34,20,35}
s2={23,56,54,21,13}
print('s1 values=',s1)
print('s2 values=',s2)
#diffrence function:- it will find diffrence between 2 sets
s3=s1.difference(s2)
print('difference=',s3)
#diffrance_update :-it will update orignal sets 
#intersection:-it will find same number from both sets 
s3=s1.intersection(s2)
print('intersection=',s3)
#intersection_update:- it will update orignal 
#union:-it will combine two sets and give result in 3 set
s3=s1.union(s2)
print('union=',s3)
#add:- it will add new elements in set on random positions 
s1.add(56)
s2.add(20)
print('new elemnts in set s1=',s1)
print('new elemnts in set s2=',s2)
#remove:- it will remove any element we pass
s1.remove(10)
s2.remove(21)
print('removed elemnts in set s1=',s1) 
print('removed elemnts in set s2=',s2)