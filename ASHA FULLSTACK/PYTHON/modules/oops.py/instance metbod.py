#instance method
#define instance method to calculate average ratings of course

class Course:
    def __init__(self,name,ratings) : #parametrised constructor,we should pass values through objct
        self.name=name
        self.ratings=ratings

    def average(self) :   #instance method which is having 'self' as arg, 'self' is nothing but pointing to obj
        average=sum(self.ratings)/len(self.ratings)    
        print("average ratings of",self.name,"is",average)

c1=Course('PYTHON',[3,3,3,3,3])  #passing paramtrs as constructor is paramtrisd
c1.average()        
c2=Course('js',[4,4,4,4,4])
c2.average()

