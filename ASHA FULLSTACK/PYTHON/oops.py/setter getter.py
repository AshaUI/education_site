#setter and #getter methods
#getter methods are used to get /return the values ,also known as accessor methods
#setter method are used to set /modify the values ,also known as mutator methos

#create a class Programmer-name,salary,technologies

class Programmer:
    def setName(self,name): #in setter getter methds we dont use  __init__ constructor
        self.name=name
    def getName(self)    :  #gettr meth should only print or retrn 
        return self.name

    def setSalary(self,salary):
         self.salary=salary
    def getSalary(self)    :
         return self.salary

    def setTechnologies(self,techs):
         self.technologies=techs
    def getTechnologies(self)    :
         print(self.technologies)      

p=Programmer()
p.setName('sam')           #setting or passing values through setter method
p.setSalary(30000)
p.setTechnologies(['python','js','html'])
print(p.getName())               #getting back the values which we set through setter
print(p.getSalary())
p.getTechnologies()             #as there is alrady print in getTechnologies() we are just calling

#practice qtns
#inner classes
#create a sudent class with attributes name,id using getter setter methods




