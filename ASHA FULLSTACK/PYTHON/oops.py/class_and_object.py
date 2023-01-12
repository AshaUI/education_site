#OBject oriented programming
#every thing in python is made up of objects
#object is an instance of class

 
 #trere are 4 principles or concepts
 #1.encapsulation
#2.inheritance
#3.polymorphism
#4.abstraction

#-------------------------------------------------------------------------------------------------------------------------
#class is a sketch/blueprint/design for object
#create a class called product it will have attribute -name,description,price

class Product:
    def __init__(self) :      #__init__ is built in constructor method
        self.name="iphone"    #'self' points to current object creaion
        self.description='its awesome'
        self.price=80000

 #out of class  ,,non parametrrized constructor
 #to access fields
p1=Product()      #creating object that invokes constuctor
print(p1.name)  
print(p1.description)
print(p1.price) 

p2=Product()  #'self will be 'p2' here
print(p1.name)  
print(p1.description)
print(p1.price) 

#------------------------------------------------------------------------------------------------------------------------------
class Emplyee:
    def __init__(self) :      #__init__ is built in constructor method
        self.name="sam"    #'self' points to current object creaion
        self.id=171510
        self.salary=80000


e1=Emplyee()     
print("nae of employee:",e1.name)  
print("id of employee",e1.id)
print("salary of emplyee:",e1.salary)
