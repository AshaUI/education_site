#17-11-22
#types of arguments
def add(a,b):  #a,b are formal arguments
    c=a+b
    print(c)
add(3,4)  #3,4 are actual argumnts

#actual arg are of 4 types
#1,position arguments
#2.default arguments
#3.var length arg
#4.keyword variable length orgument

#****position argument***
def person(name,age):
    print("name is",name)
    print("age is",age)

person('sam',30)   
person(40,'raj')  #it is illogical so we can change positions of variable 

person(age=40,name="raj")
#practice qtns
#write a functon to return multiplication of two numbers
def product(a,b):
    print("prod is:",a*b)
product(2,3)  
#position argument



#--------------------------------------------------------------------------------------------------------------------
#18-11-22
#default arguments
def  avg(a=10,b=20):
    c=(a+b)/2
    print(c)

avg(a=30) #it is taking 20 for b defaultly even if we dont give

#3 variable length argument
def sum(a,b,c,d,e,f):
    g=a+b+c+d+f
    print(g)
sum(3,4,5,6,7,8)   #for add mutliple numbers it would be tough to write co so we have sum(a,*b)    *b means it hold all the values from 2nd 

def sum(a,*b):  #b hold multiple values ,*args
    c=a
    for i in b:
     c=c+i
     print(c)  #print inside for will print all iteraion values,,print() out side loop will print final value

sum(3,4,5,6,7,8,9,10)  #fun calling


#4 keyword variable length argum
def person(name,**data):  # **data is holding multiple values regarding persn along with key values
    print(name)
    print(data)
    #person('sam',30,'hyd',98765)  it gives values but not recognised specification
    for i,j in data.items():
        print(i,j)

person('sam',age=30,city='hyd',mob=98765) #calling above function

#scope of vsriable
#global variable
#local variable

x=123  #global var
def display():
    y=456  #local var
    print(y)
    print(x)

print(x)  #first excu printing glob var
display()#next ex  aclling func

#accessing global and local var with same name
a=11  #global var
def display():
    a=22  #local variable
    print(a)
    print(globals()['a'])

print(a)  #global first executed
display()   


#practice qtns
#1,default arg
#2, var length arg
#3,keyword var length argument
#4.scope of variable
#5.accessing global  and local var with same name for float value




















