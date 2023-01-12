#types of variables
#threre are 2 tpes of variable
#1.instance variable  (non static variable) we cant call by class name but by object variable
#2.static variable (class level var) we can access by class name  as well as object var 

class car:
    color='Black' #static/class level varaiable
    def __init__(self):
        self.name='BMW'   #instance variables
    
        self.year='2021'  #instance variables

c1=car()
print(c1.name)
print(c1.year)
print(c1.color)
print(car.color)  #accessing class var with class name

c1.color='red'   
print(c1.color)  #red --color changed in object only  not in class 
print(car.color)  #black--color var in class is not changed

car.color='white'
print(c1.color)   #it takes color from already created(previous) object,so already created one having 'Black' only
print(car.color)  # color in class is changed

car.color='blue'  # static var  value changed created new object 
c2=car()     # color var in class is changed from black to blue  and re created object so both color vars will give o/p as blue
print(c2.color)
print(car.color)


       