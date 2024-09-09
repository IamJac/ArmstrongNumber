from array import *
from math import pow
def check_if_armstrong(number):
    number2=number
    number3=number
    data=array('i',[])
    while number>0:
        number2=number % 10
        data.append(number2)
        number=number//10
    n=int(0)
    for i in data:
        n=pow(i,len(data))+n
    if n==number3:
         print(number3," is an armstrong number")
    else:
        print(number3," is not an armstrong number")

num=int(input("Input a number to check if it is an armstrong number"))
check_if_armstrong(num)