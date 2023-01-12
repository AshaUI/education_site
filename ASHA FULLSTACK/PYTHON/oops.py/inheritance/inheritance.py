#inheritance is aprocess of inheriting or deriving child class with attributes and properties 
# from already existed parent class
#it signifies parent-child relatioon 
#it signifies Is-A relation 
#parent class is a class that is inherited , also known as base-super class
#child class is a class that is inheriting

class BMW:     #parent/base/super class 
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
                        
                        #syntax of chld clss "class ChildClassName(ParentClssNmae)"                     
class ThreeSeries(BMW): #child class ,(BMW) represent as parent of ThreeSeries
    def __init__(self,cruiseControl,make,model,year):
        BMW.__init__(self,make,model,year)  #inheriting parent class constructor/attributes
        self.cruiseControl=cruiseControl   #own attribute of ThreeSeries
 
class Fourseries(BMW)    :          #2nd child class ,(BMW) represent as parent of FourSeries
    def __init__(self,color,make,model,year):
        BMW.__init__(self,make,model,year)
        self.color=color


ts=ThreeSeries(True,'BMW','328i',2018)  #we should  create obj for child only,
                                        #once we crete obj for child we can automatically access parent class attributes with child obj var(ts)
print(ts.cruiseControl)
print(ts.make)  
print(ts.model)
print(ts.year)

fs=Fourseries('black','BMW','325i',2022) #we should  create obj for child only,
                                         #once we create obj for child we can automatically access parent class attributes with child obj var(fs)
                                         #if we create obj for parent we can only access parent fields/atribts cannot acces childs, 
print(fs.make)
print(fs.model)
print(fs.year)
print(fs.color)












#practice Questions
#1.Encapsulation
#2.Inheriting attributes

