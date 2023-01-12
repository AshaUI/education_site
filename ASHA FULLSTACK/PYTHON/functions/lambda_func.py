#lambda function are small anonymous func that will not have any name
#synatx of lambda function 
#--syntx--      variable=lambda argument_list:expression          -----------------------              
#lambda functions can have any no of arguments ,but only one expression
def result(x):
    return x*x
print(result(2))
#we can write abouve fun in the form of lambda
l=lambda x:x*x
print(l(2))
def cube(x):
    return x**3

print(cube(3))    
#we can write above prog in lambda fun
l=lambda x:x**3
print(l(3))


#lambda fun to add two variabls
x=lambda a,b :a+b
print(x(6,7))
#lamda fun methods
#filters method:it filters the sequence elements deppending on some logic or condition
#---syntax----variable=filter(function,iterable)--------------

#filtering only even no s from list
lst=[1,2,3,8,9,10]
result=filter(lambda x:x%2==0,lst)  #it will only print address, to print elements we need to add list() before filter
print(result)
lst=[1,2,3,8,9,10]
result=list(filter(lambda x:x%2==0,lst))  
print(result)

lst=[1,2,3,4,5,6,7,8,9,10]
result=list(filter(lambda x:x%5==0,lst))  
print(result)


#map() maps out the sequence elements depending some logic and condition different from filtering
#  map(function,iterable)
#doubling all elements in lst
lst=[1,2,3,4,5]
result=list(map(lambda x:x*2,lst))  
print(result)
#adding 3 to all elemnts of list
lst=[1,2,3,4,5] 
result=list(map(lambda x:x+3,lst))  
print(result)


#reduce() will reduce  the sequence elements depending some logic and condition 
#reduce(lambda,iterable)
#import reduce() using 
#from funtools import reduce
from functools import reduce
#reducing entire list to single elements by adding all elements
lst=[5,10,15,20]  #[15,15,20]-->[30,20]-->fin res  50
result=reduce(lambda x,y:x+y,lst)   #x and y are first 2 elements once added, res will be x and next elemnt will be y
print(result)

#reducing entire list to single elements by multiplying all elements
lst=[1,2,3,4]  #[2,3,4]-->[6,4]-->24 is final result
result=reduce(lambda x,y:x*y,lst)
print(result)

#-------------practce qtns
#write lambda funtion to add three elements
l=lambda x,y,z:x+y+z
print(l(4,5,6))

#write lambda funtion to multiply two elements
l=lambda x,z:x*z
print(l(5,7))

#inthe given list print only odd numbers
lst=[2,4,6,8,10]
f=list(filter(lambda i:i%2!=0,lst) )
print(f)
 #to the above list map the square of numbers itself
m=list(map(lambda x:x*x,lst))
print(m)
 # #reduce the list
l=[1,2,3]  
r=reduce(lambda x,y:x*y,l)
print(r)



