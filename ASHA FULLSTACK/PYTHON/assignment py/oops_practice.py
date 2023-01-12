#1.create a class  audi and find the average price of it
class Audi:
    def __init__(self,model,price1,price2):
        self.model=model
        self.price1=price1
        self.price2=price2
        
        print("average price of Audi is",(self.price1+self.price2)/2)
a=Audi("Q3",7000000,3500000)  
 #-------------------------------------------------------------------------------------------------------------------------    

#2.create a class school and inner class student and display student is studying
class School:
    def __init__(self,name):
        self.name=name
        print("student name is:",self.name)
    class Student:
        def __init__(self,id):
            self.id=id
            print("student id is:",self.id)

        def study(self):    
         print("student is studying ") 

s1=School("raj")
s2=s1.Student(102)
s2.study()

#------------------------------------------------------------------------------------------------------------
          
#3.create a base class and child class to show types of inheritance
#single level
class Phone:
    def __init__(self,memory,call):
        self.memory=memory
        self.call=call
    def games(self):
            print("games are available")
   
class Android(Phone):
    def __init__(self,camera,memory,call)  :
       Phone.__init__(self,memory,call) 
       self.camera=camera  

a=Android ("32mp",128,True) 
a.games()
print(a.camera)
print(a.memory)
print("can we call?",a.call)

#multi level
class Phone:
    def __init__(self,memory,call):
        self.memory=memory
        self.call=call
    def games(self):
            print("games are available")
   
class Android(Phone):
    def __init__(self,camera,memory,call)  :
       Phone.__init__(self,memory,call) 
       self.camera=camera
    def cam(self) :    
     print("android has filters in cam")
class Iphone(Android):
    def __init__(self,price,camera,memory,call):
     Android.__init__(self,camera,memory,call) 
     self.price=price
    def secure(self):
        print("iphone provides you security") 

I=Iphone(149900,"48mp",256,True)   
I.secure()
print("Iphone 14pro costs",I.price) 
print("Iphone 14pro camera",I.camera) 
print("Iphone 14pro has memory of",I.memory)
print("can we call?",I.call)
#multiple
class Phone:
   def games(self):
            print("games are available")
   
class Android:

 def cam(self) :    
     print("android has filters in cam")

class Iphone(Phone,Android):
    
    def secure(self):
        print("iphone provides you security")

i= Iphone()  
i.games()
i.cam()
i.secure()     

#-------------------------------------------------------------------------------------------------------------------

#4.create a parent class and child class to show method overriding
class Parent:
    def __init__(self,name):
        self.name=name
        print("this is parent class")
        print("student name is:",self.name)

    def attendance(self):
            print("teacher called with name")
class Child(Parent):
    def __init__(self,id,name):
      Parent.__init__(self,name) #invoking parent class by calling parent constructor 
      self.id=id 
      print("this is child class")
      print("student id is:",self.id)

    def attendance(self):  
     print("teacher called with id")

c=Child(101,"Raj") 
c.attendance()
#prevention of method overriding
class Parent:
    def __init__(self,name):
        self.name=name
        print("this is parent class")
        print("student name is:",self.name)

    def attendance(self):
            print("teacher called with name")
class Child(Parent):
    def __init__(self,id,name):
      super().__init__(name) #invoking parent class by calling parent constructor 
      self.id=id 
      print("this is child class")
      print("student id is:",self.id)

    def attendance(self):
      super().attendance()    
      print("teacher called with id")

c=Child(101,"Raj") 
c.attendance()
#----------------------------------------------------------------------------------------------------------------------
#5.create a class to find area and perimeter of circle
                 #area=pi*r**2
                 #perimeter=2*pi*r
from math import pi
class Circle:
    def __init__(self,r):
     self.r=r
     print("radius of circle is:",self.r)
    def area(self):
      area=pi*self.r**2
      print("area of circle is:",area)
    def perimeter(self) : 
     perimeter=2*pi*self.r
     print("perimeter of circle is:",perimeter)
c=Circle(2)
c.area()
c.perimeter()  
#------------------------------------------------------------------------------------------------------------------------   


#6.create a class to add and find average of number
class AvgAndAdd:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        c=self.a+self.b
        print("addition of numbrs:",c) 
    def avg(self):
        d=(self.a+self.b)/2   
        print("average of numbers:",d)

AA= AvgAndAdd (4,6)     
