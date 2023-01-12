#polymorphism is defined as
#  POLY:many
#MORPHISM:forms/shapes/behavior

#polymorphism refers to different behaviours of object

#"Duck" typing refers to dynamically passing parameters

class Duck:
    def talk(self):
        print("quack quack")
class Human:
    def talk(self):
        print("hello")  
class Cat:
    def talk(self):
        print("meow meow") 

def CALLtalk(obj):   #defining  method outside classes  with  obj as argument 
    obj.talk()


d1=Duck()
CALLtalk(d1)  #we are calling normal method and giving obj as argument, it will invoke CALLtalk(obj) and places d as arg
              #it callas  d.talk() from Duck obj
h1=Human()    
CALLtalk(h1)#we are calling normal method and giving obj as argument, it will invoke CALLtalk(obj) and places d as arg
              #it callas  h.talk() from HUman obj
c1=Cat()
CALLtalk(c1)#we are calling normal method and giving obj as argument, it will invoke CALLtalk(obj) and places d as arg
              #it callas  c.talk() from Cat obj


#deppendency injection using Duck typing
# it is  injecting object of one class in to anothr class-----top to bottom flow
# 
class Flight:
    def __init__(self,engine) :#engine is nothing but obj var argument through wich we pass obj var to access class methods
        self.engine=engine

    def startengine(self) :
        self.engine.start()
    def stopengine(self) :
        self.engine.stop()   

class AirbusEngine:
    def start(self):
        print("AirbusEngine started")
    def stop(self):
        print("AirbusEngine stopped") 
class BoeningEngine:
    def start(self):
        print("BoeningEngine started")
    def stop(self):
        print("BoeningEngine stopped") 



#we are calling start() of two different classes from another calss obj(f),
# tat class should have a parameter through which we pass obj as argument,nthng but flight class has "engine" paramtr to pass ai and be as argumnt so,
#so tht by using obj para(ae),we call tat AirbusEngine class  methods  
ae= AirbusEngine()   
f= Flight(ae) #as  Flight class has arg(engine) we are sending ae obj to call strt methd from AirbusEngine class by self.ae.start()
f. startengine()
f.stopengine()

be=BoeningEngine()
f1= Flight(be)  #as  Flight class has arg(engine) we are sending be obj to call strt methd from AirbusEngine class
f1.startengine()
f1.stopengine()  #we are calling stop() of both classes by using common method(stopengine()) of flight class


#operator overloading  is operator is overloaded to perform multiple operation
''' + is used to concatinate string
    + is used to join two lists
    + is used to add numbers'''

x="FSD means"   
y="Full stack development"
print(x+y)

l1=[1,2,3,"python",5]
l2=[6,7,8,"js",10]
print(l1+l2)

x=10
y=20
print(x+y)

#practise qtnd
#dependency injection
#2.duck typing
#3.operator overloading














