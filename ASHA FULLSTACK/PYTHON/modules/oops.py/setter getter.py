#setter and #getter methods
#getter methods are used to get /return the values ,also known as accessor methods
#setter method are used to set /modify the values ,also known as mutator methos

#create a class Programmer-name,salary,technologies

class Programmer:
    def setName(self,name):
        self.name=name
    def getName(self)    :
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
p.setName('sam')   #setting values through setter meth(passing val to setter meth argmnts)
p.setSalary(30000)
p.setTechnologies(['python','js','html'])
print(p.getName())   #getting back the values which we have set through setters
print(p.getSalary())  #as we are returning in getter, we need to use prin stmnt
p.getTechnologies()  #as already printing in getTechnologie(),we just need to call, no need of print stmnt

#practice qtns
#inner classes
#create a sudent class with attributes name,id using getter setter methods




