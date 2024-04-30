#real time use of inheritance
class person():
    def __init__(self):
        self.id=input('enter id:-')
        self.name=input('enter name:-')
        self.phone=input('enter phone:-')
        self.qualification=input('enter qualification:-')
        self.experince=input('enter experince:-')
        self.email=input('enter email:-')
        self.address=input('enter address:-')
        self.gender=input('enter gender:-')
class employee(person):
    def __init__(self):
        super().__init__()
        self.bs=input('enter bs:-')
        self.ta=input('enter ta:-')
        self.hra=input('enter hra:-')
    def show(self):
        print(self.id,self.name,self.phone,self.qualification,self.experince,self.email,self.address,self.gender,self.bs,self.ta,self.hra)
class admin(person):
    def __init__(self):
        super().__init__()
        self.salary=input('enter salary:-')
        self.role=input('enter role:-')
    def show(self):
        print(self.id,self.name,self.phone,self.qualification,self.experince,self.email,self.address,self.gender,self.salary,self.role)
print('enter 1 to enter detail of employee')
print('enter 2 to enter detail of admin')
n=int(input('enter your choice:-'))

if n==1:
    obj=employee()
    obj.show()
if n==2:
    obj=admin()
    obj.show()