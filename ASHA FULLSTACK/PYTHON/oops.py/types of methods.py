#types of method 
#3 types of methods

#1.instance method
#2.class methods
#3.static method
#in variables both static var and class level var are considered as same but here both are different

class Student:
    school='ABC'  #class level/static variable
    def __init__(self,m1,m2,m3):
        self.m1=m1   #instance var
        self.m2=m2
        self.m3=m3
    #@instancemethod
    def average(self)  : #instance method(having 'self' as argument)
        print("this is instance method")
        print("average of marks is:",(self.m1+self.m2+self.m3)/3)  

    @classmethod
    def info(clss) :     #class method (having arg other than 'self')
        clss.school='xyz'   
        return clss.school
    @staticmethod
    def display():      #static mehod(does not have any args in side ())
        print("this is static method")

#object

s1=Student(10,30,20)   #object creation and assinging object to var s1
s1.average()           #calling instance method by using s1,average meth is already printing ,so no need of print statemnt
print(s1.info())        #calling class method by using s1   ,info() is returning val, so we need to print here
s1.display()            #calling static method by using s1