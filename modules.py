# from this we can call functions from diffrent modules
#1)import prime :-it will import every function in prime we made  
#2)import prime as p :- from this we can use prime as p.function name insted of prime.function name and it is called "aliasing"
#3)from prime import sum,sub:- it will be used to call specific function from any file and to run it jus write functionname(arg) ex: x=sum(2,3)
#4)from prime import * :- it will call all the function and its syntax will be just like x=sum(2,3)
#5) there are some inbuilt functions which we can use and to fin it search on google which moduel it is store and its name like we have math inbuild moduels 
from prime import *
x=sum(int(input('enter the numers to add:-')),int(input('enter the numers to add:-')))
print(x)
import math as m 
x=m.pow(int(input('enter the number:-')),int(input('enter the numer to find numbers power which u want:-')))
print(x)
import time 
#it will have all time functions
#example:- time.sleep,year,time,ctime,mon,mday,localtime
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
        time.sleep(0.5)
    print("")
import random
x=random.randint(1,100)
print(x)