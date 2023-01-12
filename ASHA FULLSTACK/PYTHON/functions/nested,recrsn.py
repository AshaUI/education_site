#function passed as parameter to another function
def display(fun):
    return 'hi'+ fun
def name() :
    return 'sam'  
def show():
    return 'how are you'  
print(display(name()))   

print(display(show()))
#assigning function to a variable
a=11
def display():
    a=12
    print(a)
    print(globals()['a'])
print(a)   
z=display
z()


#nested function --function inside another function
def outer_function(arg):
    def inner_function():
        return 'hello'+arg   #arg is arg of outer fun we can give arg in side inner fun too , but wen we are calling we should defntly call with paramter value
    return inner_function()    

print(outer_function('tina'))
#inner fun with argument-------
def outer_function(arg):
    def inner_function(fun):
        return 'hello'+arg +fun  #arg is arg of outer fun we can give arg in side inner fun too , but wen we are calling we should defntly call with paramter value
    return inner_function('how are you')    

print(outer_function('tina'))

#no arg in outer and inner
def outer_function():
    def inner_function():
        return 'hello'   
    return inner_function()    

print(outer_function())

#passing sequence to the fun
def myfunc(lst):
    for i in lst:
        print(i)

lst=[1,2,3,4]  
myfunc(lst)  

#for printing only even num from list
def myfunc(lst):
    for i in lst:
        if i%2==0:
         print(i)

lst=[1,2,3,4]  
myfunc(lst) 
 
#recursion is process of  functio calling itself
'''factorial is best example of function recursion
factorial(3)=3*2*1
factorial(3)=3*factorial(2)
factorial(2)=2*factorial(1)
factorial(1)=1*factorial(0)
factorial(0)=1
'''
#factorial is user defind function it is not predefined func

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)    

print(factorial(3))

#changing name of funt from factorial to fact
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)     #calling fun itself

print(fact(3))

#practice qtns
#1.function passed as parameter
def avr(sum):
    return sum/2
def add(a,b):
     return  a+b
print(avr(add(6,8)))

#2.nested function
def info() :
    def name()  :
        def designtn() :
            return ' Full stack developer'
        return "Asha"+ designtn()    
    return '1.'+ name()
    
print(info())

#3.pass tuple to function and print only odd numbers
def mytpl(tpl):
    for i in tpl:
        if i%2!=0:
            print(i)

tpl1=(12,23,34,45,5,6,67,78,89)
mytpl(tpl1)


#4.recurssive function

def display(num):
    if num == 0:
        return 
    display(num-1)
    print(num)

display(3)




