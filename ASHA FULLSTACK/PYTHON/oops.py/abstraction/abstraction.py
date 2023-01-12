#abstraction hiding info, just focussing on essential data
#we make class as abstract, abstract class will have abstract methods 
#abstract method will not have any implementations
#abstract metohds will notb be instantiate keeping methd empty we use "pass"
#only parent class can be abtract
#abstract method should be implemeted in child class
 

from abc import ABC,abstractmethod   #if we dont import it will give error
'''
class BMW(ABC):#it defines this class is abstract class
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def strat(self):
        print("starting the BMW car")

    def stop(self) :
        print("stoping the BMW car")    
    @abstractmethod
    def drive(self):     #abstract method with no implementation, implementing in child class
        pass       

class Threeseries(BMW):
    def __init__(self,color,make,model,year) :
       BMW.__init__(self,make,model,year)
       self.color=color  

    def start(self):
        print("starting the Threeseries car")

    def stop(self) :
        print("stoping the Threeseries car") 

    def drive(self):
        print("abstract class implemented here ,threeseries drove")    


ts=Threeseries('black','BMW','328i',2018)     
ts.start()
ts.stop()
ts.drive()   
'''
#interface  all methods of abstract class will be abstract methods

class BMW(ABC):#it defines this class is abstract class
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self) :
        pass    
    @abstractmethod
    def drive(self):     #abstract method with no implementation, implementing in child class
        pass       

class Threeseries(BMW):
    def __init__(self,color,make,model,year) :
       BMW.__init__(self,make,model,year)
       self.color=color  

    def start(self):
        print("starting the Threeseries car")

    def stop(self) :
        print("stoping the Threeseries car") 

    def drive(self):
        print("abstract class implemented here ,threeseries drove")    


ts=Threeseries('black','BMW','328i',2018)     
ts.start()
ts.stop()
ts.drive()

#practice qtns

