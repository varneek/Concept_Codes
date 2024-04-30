#encapsulation:- it is a wraping of variables and functions into a single unit and that single unit is class
#advantages:- data hideing 
#__name:- from double underscore data will get private
class student:
    def __init__(self,id,name):
        self.__id=id
        self.__name=name
    def show(self):
        print(self.__id,self.__name)
n=int(input('enter choice:-'))
if n==1:
    s=student(101,'mohan')
    s.show()
#setter and getter:-setter means to collect information and getter means we will get that information
class students:
    def setid(self,id):
        self.__id=id
    def setname(self,name):
        self.__name=name
    def getid(self):
        return self.__id
    def getname(self):
        return self.__name
if n==2:
    s1=students()
    s1.setid(101)
    s1.setname('ram')
    print(s.getid())
    print(s.getname())
#_name:-one under score will make protected 