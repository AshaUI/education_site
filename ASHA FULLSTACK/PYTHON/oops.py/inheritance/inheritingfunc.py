#inheriting function from parent class
#child class will inherit parent class method

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

 def display(self):
    print(self.color)   
class Fiveseries(BMW):
    def __init__(self,wheels,make,model,year):
        BMW.__init__(self,make,model,year)
        self.wheels=wheels

    def display2(self):
        print(self.wheels)


ts=Threeseries('black','BMW','3HI6',2018) 
ts.start()
ts.stop()
ts.display()   
fs= Fiveseries('4wheeler','BMW','3HI6',2018)
fs.display2()
