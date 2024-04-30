#1) single inheritance:- 1 parent 1 child 
#2) multi level inheritance:- chain system ex - A->B->C->D /parent child going on
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
#3) hierarchical:- 1 parent multiple childeren 
# ex- A parent of B C and D 
# 4) multiple:- it will inherit multiple class 
#  ex- A B and C is parent of D
# syntax:- 
class a:
    def __init__(self):
        self.x=10
class b:
    def __init__(self):
        self.y=20
class c(a,b):
    def __init__(self):
        a.__init__(self)
        b.__init__(self)
    def show(self):
        print(self.x,self.y)
obj=c()
obj.show()
#5) hybrid:- mixture of two classes 
# not fixed structure ex -  A parent of B and C and B and C are parent of D
