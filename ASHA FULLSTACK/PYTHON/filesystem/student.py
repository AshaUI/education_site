#pickle i sused to serialise file(connect) from other file file we are pasing values to class variables

class Student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks

    def display(self):
        print(self.id,self.name,self.marks)    

class Employee:
    def __init__(self,id,salary):
        self.id=id
        self.salary=salary

    def display(self):
        print("emp id is:",self.id)   
        print("emp salary is:",self.salary)  

        
