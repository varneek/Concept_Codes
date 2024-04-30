#abstraction:- it means showing only esential features by hideing background details
# a function without a defination is an abstract function
# a calss contain at least one abstract function is an abstract calss
# syntax:- 
from abc import ABC,abstractmethod
class fruit(ABC):
    #use comment
    @abstractmethod
    def getprice(self):
        pass
#when a class inherits an abstract calss then child class must override abstract functions of parent class otherwise child will also become abstract
# we can not creat object of an abstract class 
class kaddu(fruit):
    def getprice(self):
        return 130
a=kaddu()
print(a.getprice())