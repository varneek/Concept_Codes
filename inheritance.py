#it is the capability of a class to gain the properties of some another class 
#synatx:- 
class a:
    def __init__(self):
        self.x=10
        self.y=20
    def show(self):
        print('hello')
class b(a):  #this will inherit calss a in calss b
    pass
class c(a):
    def __init__(self):
        #super().__init__()     we can use this to call parent class 
        a.__init__(self) # need to call parent class in init function
        self.z=30
obj=c()
print(obj.x,obj.y,obj.z)
obj.show()