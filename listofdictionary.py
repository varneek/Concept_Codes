#list od dictionary:- it can store multiple dictinary
students=[{'id':101,'name':'raju','phone':8181,'marks':78},{'id':102,'name':'kaju','phone':9191,'marks':70}]
data={'id':103,'name':'kaj','phone':5191,'marks':78}
print(students[0])
print(students[1]['id'])
print(students)
#update:- it will add new key and value
data['email']='abc@gmail.com'
print(data['email'])
#pop:-delete and show
k=data.pop('id')
print(k," ",data)
#keys:- it will give keys of dictionary
f=data.keys()
print(f)
