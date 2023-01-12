#inner class --a class defined inside another class***(HOW TO ACCESS OUTER CLASS VAR TO INNER CLASS)
#create a class Car and inner class Engine

class Car:   #outer class
    def __init__(self,make,year):
        self.make=make
        self.year=year
   
    class Engine:  #inner class,  indentation should match with above def 
        def __init__(self,number) :
            self.number=number

        def start(self)  :  #instance mmethod having self in ()
            print("engine started")

        class Vehicle:      #another inner class,indentation should match with above def, other wise will give err
            def __init__(self,color,type):
                self.color=color 
                self.type=type
                print("color of vehicle is:",self.color)

            def fuel(self) :   #instance method with 'self ' arg
             print("fuel of vehicle is",self.type)  




c=Car("bmw",2018)          #creating outer class obj with passing args
e=c. Engine(123)           #creating inner class obj(e) with the help of outer class obj(c)
e.start()
v=e.Vehicle('black','petrol') #creating 2nd inner class obj(v) with help of above class obj(e)
v.fuel()                    #calling fuel() with obj var,no need of print stmnt as already printing in fuel meth



     