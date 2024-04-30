#structure oriented:- main focus is on functions it is also known as produce oriented
#oops(object oriented pogramming):- main focus will be on object
#object:- an object is a real world entity that has property and show behaviour
# a class is a desine or a blueprint for any object
class students:
    id=10
    name='mohit'
    number='919191'
    marks=78
    def study(self):
        print('student is studying')
s1=students()   # this will make obj of class
print('id=',s1.id,'name=',s1.name,"number=",s1.number,'marks=',s1.marks)
s1.study()
#self:- it will always asgin object into self, it will represent object of the calss 
