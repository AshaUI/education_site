#encapsulation--refers binding the code and data into single unit
#it refers to hide the attribute so that the objcts cannot access properties of class ,
#it provides security to our code
#we can access that secured/private code by 1.methods(display ,info,any userdefined metho) &
# 2. name mangling syntax -->    objvar._ClassNmame_attribute

#Basic prgrm 
class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id

s1=Student('sam',101)   
print(s1.name )
print(s1.id)    

#implementing encapsulation by making fields/varbles private by using (double underscore)"__" at the bigining of attribute name
'''class Student:
    def __init__(self,name,id):
        self.__name=name   # self.__name self.__id  are privtae now
        self.__id=id

s2=Student('sam',101)   
print(s2.__name )   #this will give error bcs we cannot access private fields directly  by their name
print(s2.__id)'''

#Accessing private fields by "Methods" and Name mangling syntax

#1.methods (method can be our own methds,we can use any method name)
class Student:
    def __init__(self,name,id):
        self.__name=name   # self.__name self.__id  are privtae now
        self.__id=id

    def display(self) :
        print(self.__name)  
        print(self.__id) 

s2=Student('sam',101)
s2.display()      #we are accessing or printing name and id by invoking dispaly method, 
#--------------------------------------------------------------------------------------------------------------
#2.name mangling syntax  ----->   objvar._ClassName__privateAtribtName
class Student:
    def __init__(self,name,id):
        self.__name1=name   # self.__name & self.__id  are private now
        self.__id1=id


s3=Student('ram',105)
print(s3._Student__name1)
print(s3._Student__id1)

#-------------------------------------------------------------------------------------------------------------------
# create an Employee class with name, salaray, id ANd implement encapsulation
#1.accesing private fields by method
class Employee:
    def __init__(self,name,id,salary):
        self.__name=name   # self.__name self.__id  are privtae now
        self.__id=id
        self.__salary=salary

    def info(self)  :  #instance method having self as agr
        print("employee name is:",self.__name)   
        print("employee name is:",self.__id)
        print("employee name is:",self.__salary)

e1=Employee('jhon',1234,50000)
e1.info()        

# and  by using name mangling syntax
class Employee:
    def __init__(self,name,id,salary):
        self.__name=name   # self.__name self.__id  are private now
        self.__id=id
        self.__salary=salary

e2=Employee("steve",175510,40000)
print(e2._Employee__name)
print(e2._Employee__id)
print(e2._Employee__salary)
        

