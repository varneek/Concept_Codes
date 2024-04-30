#it means:- many existance/forms
# it is a property of a functio to show diffrent diffrent behaviour at diffrent diffrent situation
# overloading or overrideing of function is the way to achive polymorphism
# python doesn't support overloading
# overloading:- class can have function with some name but diffrent arguments
# the diffrence in arguments maybe on the basis of 1) no. of arguments, 2) type of arguments, 3) both
# over rideing:-when a child class redefines parent calss function it is function overriding
#advantage:-a devloper not need to remember diffrent names of function for diffrent functionality
#example of over rideing:-
class car:
    def run(self):
        print('car is running at 40 kmph')
class sportscar(car):
    def run(self):
        print('car is running at 240 kmph')
bmw=sportscar()
bmw.run()
alto=car()
alto.run()