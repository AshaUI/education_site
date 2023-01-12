#method overriding
#parent class and chilclass will have same and exact method name
class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.mpdel=model
        self.year=year

    def start(self):
            print("starting the car")
    def stop(self):
            print("stoping the car")

class Threeseries(BMW):
 def __init__(self,color,make,model,year):
   BMW.__init__(self,make,model,year)  #inheriting parent class constructor/attributes
   self.color=color   
 def start(self):
            print("button start")
 def stop(self):
            print("button stop")

 def display(self):
    print(self.color)   
class Fiveseries(BMW):
    def __init__(self,wheels,make,model,year):
        BMW.__init__(self,make,model,year)
        self.wheels=wheels

    def display2(self):
        print(self.wheels)
    def start(self):
            print("button four start")
    def stop(self):
            print("button  four stop")
    


ts=Threeseries('black','BMW','3HI6',2018) 
ts.start()
ts.stop()
ts.display()   
fs= Fiveseries('4wheeler','BMW','3HI6',2018)
fs.display2()
fs.start()
fs.stop()

#prevent method overriding
#super() keyword is used to invoke parent class constructor and parent class method bcz by using overriding we cannot access parent class method of same name  
# #wen we need  to execute child class method as well as super class method we have to call parent class method with super()

class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.mpdel=model
        self.year=year

    def start(self):
            print("starting the car")
    def stop(self):
            print("stoping the car")

class Threeseries(BMW):
 def __init__(self,color,make,model,year):
   super().__init__(make,model,year)  #inheriting parent class constructor/attributes
   self.color=color   
 def start(self):
    super().start()  #we are calling superclass() start method by using super keyword
    print("button start")
 def stop(self):
    super().stop()
    print("button stop")

 def display(self):
    print(self.color)   

    


ts=Threeseries('black','BMW','3HI6',2018) 
ts.start()
ts.stop()
ts.display()   

#practice qtns
#inheriting functionality 
#2.method overriding 
#3.preventing method overriding 
