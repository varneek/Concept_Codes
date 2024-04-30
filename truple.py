#it is not changeable and only index and count function will work on tuple
values=(10,23,12,43,34)
print(values)
print(values[0])
#unpacking:- it will assin elements in variables 
data=(10,20,30)
(x,y,z)=data
print(data)
# * this will amke list after the element we put  
(x,y,*z)=values
print(values)
# in this condition x will be first number and z will be last and in between numbers they will become list and assin to y 
(x,*y,z)=values
print(values)
