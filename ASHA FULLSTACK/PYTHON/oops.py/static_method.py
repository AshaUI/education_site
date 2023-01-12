#define static method - this meth dosnt hav any arg 
#create a class and count the no of objects created for the class
class ObjectCounter:
    numberOfObjects=0   #counting variable
    def __init__(self):
        ObjectCounter.numberOfObjects+=1  #as numberOfObjects is class level, calling it with class name,
                                         #wen obj is created ,count will be automatically incremented,no need of loops
    @staticmethod
    def displayCount():    
        print(ObjectCounter.numberOfObjects)
#creating 3 objects to disply count 3
o1=ObjectCounter()   
o2=ObjectCounter()
o3=ObjectCounter()
o1.displayCount()   #both line 15 and 16 will give same o/p
ObjectCounter.displayCount()   #just calling method with class name to give total count,print is already in tne method so here no need    
