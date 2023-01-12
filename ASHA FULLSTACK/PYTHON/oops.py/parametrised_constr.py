#parametrised constructor-constructors with parametrsor arguments
#create a class by name and having attributes-name,ratings

class Course:
    def __init__(self,name,ratings):
        self.name=name  #here right side namr should match with parameter'name'
        self.ratings=ratings

c1=Course('python',[5,5,5,5,5]) 
print(c1.name)
print(c1.ratings) 
#------------------------------------------------------------------------------------------------------------------------------
class Course:
    def __init__(self,name,ratings):
        self.Course_name=name  #here right side namr should match with parameter'name'
        self.Course_ratings=ratings

c1=Course('java',[10,10,5,5,5]) 
print(c1.Course_name)
print(c1.Course_ratings) 

#---------------------------------------------------------------------------------------------------------------------------------
class Employee:
    def __init__(self,name,id,salary):  #self iscurrnt object,#
        #which ever the object is accessing this class, self will be replaced with obj variable
     self.emp_name=name
     self.emp_id=id
     self.emp_salary=salary

e2=Employee('sam',171510,60000)   #assigning class"Employee" to object variable 'e2'
print(e2.emp_name,e2.emp_id,e2.emp_salary)

#practise qtns
#1.create a class laptop-make,model,price (with out parameters )
#2.create a class Train-train.no, ticket_price,seat_no (with parameters)
