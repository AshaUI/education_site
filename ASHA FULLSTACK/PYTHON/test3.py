#1.in the given list retriew only odd numbers using small anonymous function
def odd(lst):
    for i in lst:
        if i%2!=0:
            print(i)

lst1=[3,5,6,7,8,9,34,45,56,67] 
odd(lst1)
#2.multiple inheritance
class Univ:
    def __init__(self,Uname):
        self.Uname=Uname
        print("Univ class")
    def Uinfo(self) :
        print("student belongs to university of:",self.Uname)  
class College:
    def __init__(self,Cname):
        self.Cname=Cname
        print("College class")
    def Cinfo(self):
        print("student is studying in college of code",self.Cname) 

class Student(Univ,College):
    def __init__(self,Sname,Uname,Cname):
        Univ.__init__(self,Uname)
        College.__init__(self,Cname)
        self.Sname=Sname
        print("student class")
    def Sinfo(self):
        print("student name is:",self.Sname)

s1=Student("Aisha","JNTUK","KITS")
s1.Uinfo()
s1.Cinfo()
s1.Sinfo()

#3.method overriding

class Parent:
    def asserts(self):
        print("plane land of 500sqft")
    
    def futureplan(self):
        print("cunstruct a house")
class Child(Parent):
    def asserts(self):
        print("constructed duplex house in 500sqft")
    def futureplan(self):
        print("invest more on lands and business")   

class Child2(Parent) :
    def asserts(self):
       print("construct another floore on top")

    def futureplan(self):
        print("sell the house and settle in USA")   
c1=Child()
c1.asserts()
c1.futureplan()
c1=Child2()
c1.asserts()
c1.futureplan()


#4.write a pythn program to check if a string is palindrome
x=input("enter  a string:")
y=x[::-1]
if y==x:
    print("entered string is palindrome")
else:
    print("entered string is  not palindrome")    

#5.write a python program to sort a list of touples using Lamda

#sort() accending order

result=lambda lst:lst.sort()

lst1=[(1,2,3),(4,5,6),(7,8,9),(11,22,33)]
print(result(lst1))



lst.sort(reverse=True)
print(lst)

#6.write a python program to find wether a given string starts with a given charecter using lambda.

result=lambda s,c:'yes' if s[0]==c else 'no'

s=input("enter a string:")
c=input("enter char:")
print(result(s,c))   #function calling with two parameters


'''def str(s,c):
    if s[0]==c:
        print("yes")
    else:
        print("no")  

s=input("enter string:")
c=input("enter charecter:")
str(s,c)        '''

    



#7.write a python program to swap two numbers
x,y=[int(i) for i in input("enter x nad y:").split()]
a=x
x=y
y=a
print("x value is",x)
print("y value is",y)
#8.write a python program to handle assertion error for number divisible by 5
try:
    number=int(input("enetr a number:"))
    assert number%5==0,"you hav eentered invalid input "
    print("after assertion")

except AssertionError as msg:
  print(msg)
  print("after assertion")

#9.write pyhton program to copy an image from on file to another
f=open('mypic.jpg','rb')
f1=open('mypiccopy.jpg','wb')
for i in f:
 print(f1.write(i))
#write a funtion to find area of circle
import math
def areaOfcircle(r):
    pi=22/7
    a=pi*(r**2)
    print(a)
x=int(input("enter radius:"))
areaOfcircle(x)

