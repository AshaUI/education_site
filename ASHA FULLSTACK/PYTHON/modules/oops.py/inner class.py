#inner class --a class defined inside another class
#create a class Car and innerclass Engine

class Car:   #outer class
    def __init__(self,make,year):
        self.make=make
        self.year=year

    class Engine:  #inner class  , indentation should math with init constructor of aboveclss, othr wise wll giv err
        def __init__(self,number) :
            self.number=number

        def start(self)  :  #instance mmethod having self in ()
            print("engine started")

        class Vehicle:   #another inner class,indentation should math with init constructor of aboveclss, othr wise wll giv err
            def __init__(self,color,type):
                self.color=color 
                self.type=type
                print("color of vehicle is:",self.color)

            def fuel(self) :   #instance  method
             print("fuel of vehicle is",self.type)  




c=Car("bmw",2018)               #obj creation of outer class as usual
e=c. Engine(123)                #obj(e) creation of inner class with help of outer class obj(c)  
e.start()                       #invoking /calling  inner class method with obj var
v=e.Vehicle('black','petrol')   #creating (v)  object of 2 nd inner class with above obj(e)(2nd inner clss)
v.fuel()                        #passing values bcz constrctr is paramtrsd

#  class metod explntn?

     