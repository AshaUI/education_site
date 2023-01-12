#1.Write a function to add two numbers using return function.
def add(a,b):
    return a+b

print(add(13,15))

'''2.Write a program to illustrate functions by taking default parameter as designation = Software Engineer.
call the function and display "Iam working as Software Engineer" (call 3 times everytime changing the designation such as Data Scientist,
data analyst,python developer)'''


def employee(designation= 'Software Engineer'):
    print("i am working as ",designation)

   
employee(designation= "data analyst")
employee(designation= "python developer")
#3.write a program to demostrate use of function argument types.
#actual arg are of 4 types
#position arguments
#default arguments
#var length arg
#keyword variable length orgument

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
     print(c)  #print inside for will print all iteraion values,,print() out side loop will print final value

multiply(2,3,2,3,4,10)  #fun calling

# key variable length argum
def iphone(model,**info):  # **data is holding multiple values regarding persn along with key values
    print(model)
    print(info)
   # iphone('14 pro max',48,'1TB',140000) it gives values but not recognised specification
    for i,j in info.items():
        print(i,j)

iphone('14 pro max',cam=48,storage='1TB',Price=140000) #calling above function

 
#5.Write a Python function to sum all the numbers in a list.
lst=[22,23,42,25,26,27,28,29]
sum=0
for i in lst:
    sum=sum+i
    print(sum)  
print(sum)
#----------------------
from functools import reduce
res=reduce((lambda x,y:x+y),lst)
print("sum of all list elements by using reduce fun:",res)



