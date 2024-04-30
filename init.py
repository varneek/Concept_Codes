#__init__ :- it is magic functuion and also known as constructor
#magic is always used as:- __name__ it will called magic variable
class student:
    def __init__(self):
        print('hello')
#from init we not need to call the function just call class
# *s1=student()*
class students:
    def __init__(self,id,name,marks,number):
        self.id=id
        self.name=name
        self.marks=marks
        self.number=number
# to not need to print again and again we will make another function and we will call it and it will be easy to use 
    def show(self):
        print(self.id,self.name,self.marks,self.number)
s1=students(101,'manoj',96,'9911')
s2=students(102,'manu',66,'9921')
s1.show()
s2.show()
#we can make list of objects and use them like *student[0].show()* for i in students: i.show()