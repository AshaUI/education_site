#1.using the reduce function find out the sum of all elements in a list:
from functools import reduce 

lst = [5,10,15,20]
s=reduce(lambda a,b:a+b,lst)
print(s)
#2. Write lambda to calculate the sum of two numbers.
s2=lambda x,y:x+y
print(s2(55,45))

#3.create a lambda that will return 'yes' if the given number is even and No if the given number is odd
n=lambda a:'yes' if a%2==0 else 'no' 
print(n(4))
print(n(9))
#4.retrieve odd numbers from given list of numbers using suitable lambda function.
lst1=[10,2,3,5,7,13,4,8]
odd=list(filter(lambda x:x%2!=0,lst1))
print(odd)
#5.given list of numbers using suitable function add 1 to each element.
l1=[2,4,5,6]
final=list(map(lambda x:x+1,l1))
print(final)
#6.write a program to demostrate use of function argument types.
 

#****position argument***
def student(subject,marks):
    print("subject name  is:",subject)
    print("marks are:",marks)

student('js',88)   
student(70,'python')  #it is illogical so we can change positions of variable 

student(subject='python',marks=70)

#default arguments
def  avg(a=10,b=20,c=40):
    c=(a+b+c)/3
    print(c)

avg(a=30) #it is taking 20 for b  and c=40 by defaultly even if we dont give

# variable length argument

def multiply(a,*b):  #b hold multiple values ,*args
    c=a
    for i in b:
     c=c*i
     print(c)  
multiply(2,3,2,3,4,10)  #fun calling

# key variable length argum
def iphone(model,**info):  
    print(model)
    print(info)
   # iphone('14 pro max',48,'1TB',140000) it gives values but not recognised specification
    for i,j in info.items():
        print(i,j)

iphone('14 pro max',cam=48,storage='1TB',Price=140000) #calling above function

 

#7.Demonstrate with an example how functions can be passed as parameter to another function.
def call1():
    return "hi"
def call2(x):  #passing para meter to func
    print(x)
    print("hello")    

call2(call1() )  #passing fun as parameter to call2 methd
#----------------------------------------------------------------
def add(x,y):
    return x+y

def avg(z) :
  print("average of two numbrs is:" ,z/2) 
   
x,y=[int(x) for x in input("enter two values:").split()]

avg(add(x,y))  #calling avg().......passing add()as parameter to avg()






    

   
