#instance method
#define instance method to calculate average ratings of course

class Course:
    def __init__(self,name,ratings) :
        self.name=name
        self.ratings=ratings

    def average(self) :
        average=sum(self.ratings)/len(self.ratings)    
        print("average ratings of",self.name,"is",average)

c1=Course('PYTHON',[3,3,3,3,3])
c1.average()        
c2=Course('js',[4,4,4,4,4])
c2.average()

#practice qtns
#1.types of variables
#2.types of methods
#3.calculate the average of employee salary