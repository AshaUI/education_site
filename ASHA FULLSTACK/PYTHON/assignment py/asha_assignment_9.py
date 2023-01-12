'''1.Write a Python program to find the Area of Triangle.
   semi-perimeter : s=(a+b+c)/2
  (formula to find area of traingle  is area = (s*(s-a)*(s-b)*(s-c))**0.5)'''
a,b,c=[int(x) for x in input("enter 3 values:").split()]
s=(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of1 trianle is:",area)
'''2.Write a Pyhton program to capture employee details like emp_id,emp_name and emp_salary
  and display them.'''
id=input("enter employ id: ")
name=input("enter Name : ")
salary=int(input("enter Salary id: ") )
print("emplyee name : {0} \n emplyee id : {1}\n {0} salary is : {2}".format(  name,id,salary))
  
#3.Write a program to calculate the average of three numbers taking user input.
x,y,z=[int(x) for x in input("enter 3 numbers:").split()]
print("average is:",(x+y+z)/3)

'''4.Write a program to calculate the compound Interest.
   CI=P(1+R/100)^t'''

def compoundInterest(p,r,t):
  #ci=p(1+r/100)^t
 ci=p*(pow((1+r/100),t))
 print("compound interest of total amount is:",ci)

compoundInterest(1000,2,1) 
   
#5.Write a program to represent integer 20 into binary,hexadecimal and octal.
dec=20
print("20 in binary format",bin(dec))
print("20 in hex format",hex(dec))
print("20 in oct format",oct(dec))
#6.Write a program to calculate square root of a number. (square root = number ** 0.5)
#7.Write a program to calculate Simple Interest by taking user input

p=int(input("eneter principle amount:"))  
r=float(input("enter rate of interest:"))
t=int(input("enter time period:"))
si=(p*t*r)/100
print("SIMPLE INTEREST IS:",si)
#8.Write a program to calculate the Area of circle using math module
from math import pi
def areaOfCircle(r):
  print("area of circle is:",pi*r**2)

areaOfCircle(5)  
#6.Perfrom bitwise operations on 20 and 25.
a=20
b=25
#bitwise and---&
print("a&b  is:",a&b)
#bitwise or-|
print("a|b  is:",a|b)
#bitwise ex-or---^
print("a^b  is:",a^b)
#right shift-->>
print("a>>3bits is:",a>>3)
print("b>>2 bits  is:",b>>2)

#left shift--<<
print("a<<3bits is:",a<<3)
print("b<<2 bits  is:",b<<2)

#7.Demonstarte the use of identity operators with an example
x=[1,2,3]
y=[1,2,3]
print(x is y) # it gives flase bcs it just checks memory locations
z=x   # assigning memory locations of x to z as list is mutable
print(x is z)
a=10
b=12
print(a is b)
c=b
print(b is c)

#8.Perform logical operations and comparison operations on 50,55.
x=50
y=55
print(x<=50 and y==55)  
print(x==50 and y!=55)  
print(x==50 or y==60) 
print(x<=50 or y==50)     
print(not(x==50 or y==55)) 
print(x==55)
print(y>=55)
print(x!=55)
#9.Demonstrate the following with example
#1.reading an expression
x=10
y=90
a=input("enter an expression ex x+y  :")
b=eval(a)
print(b)

#raeding multiple inputs

l1=[int(x) for x in input("ente  int values :").split()]   #mulitpke int inputs frm user
print(l1)

#lst=[float(x) for x in input("ente  float vals:").split()]  #mulitpke float inputs frm user
#print(lst)

str=[x  for x in input("enter multiple strings:").split()]  #mulitpke str inputs frm user
print(str)
x,y=[int(x) for x in input("enter values:").split()]
print(x*y)

#2.reading char
ch=[x for x in input("enter charecters:").split()]
print(ch)
#3.reaading multiple inputs
#4.use of format method
print("i am {},and I  have joined {} course at {} institute".format('ASHA',"FULL STACK DEVLOPMENT",'LEVELUP'))