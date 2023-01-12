#function are group of statements tat perform perticular task
#functions can be built in and user defined

#syntax of function
#def functionName(arg):
      #function body
 
 #functionName(arvalue)   #function calling

def greet():
    print("hi")
    print("hello")

greet()

def add(a,b):
    print(a+b)

add(4,5)   

def average(x,y):
     z= (x+y)/2
     print("average is%0.0f"%z)

average(3,6)
average(8,4)



def add(x,y):
    c=x+y
    return c  

print(add(7,9))      

def average(x,y):
    z=add(x,y)
    w=z/2  #or we can directly write w=(x+y)/2
    return w

print(average(4,8))   

#functionscan return multiple values
def calc(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    return a,b,c,d       #--it returns all values in a tuple type
result=calc(10,5) 
for i in result:         #iteration over tuple, 
    print(i)
    #or we can write
for i in calc(10,5)  :   #iterating directly from returning values
    print(i)  


print(average(8,2))
print(average(4,2))

#practice qtns
#1. function to multipy 2 numbers
def product(a,b):
    print(a*b)
product (4,5)  

#2.function to find area of circle.formla  :area=pi*r**2

def areaOfCircle(r):

 pi=22/7
 area=pi*r**2
 print("area of circle is:",area)

areaOfCircle(3)
#3.function to find square of a number
def square(x):
    sqr=x**2
    print("square is",sqr)
square(4)
#4.print numbers from 1 - 15
x=1
while(x<=15):
    print(x)
    x=x+1










