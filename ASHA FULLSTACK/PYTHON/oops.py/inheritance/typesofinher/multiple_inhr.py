#multiple parents one child
#mro--- method resolution order if c is inheriting b and the a , super() will take a class  it moves form left to right
#in c class  if we write super().init it will access a class constructor
#C-----> A,B
class A:   #A is parent
    def __init__(self):
        print("A init")
        
    def feature1(self):
        print(" feature1 is working")
    def feature2(self):
        print(" feature2 is working")
class B:  #B is  parent
    def __init__(self):
        super().__init__()
        print("B init")

    def feature3(self):
        print(" feature3 is working")
    def feature4(self):
        print(" feature4 is working") 

class C(B,A): #C is child of A and B  so c can inherit A  and B properties also if  we enter class C(A,B) then it will give only a and  c init
    def __init__(self):
        print("c init")
        super().__init__()   #it will invoke A class init


    def feature5(self):
        print(" feature5 is working")
    def feature6(self):
        print(" feature6 is working")         

c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4() 
c1.feature5()
c1.feature6()

#create a class Car BMW Audi

class Car:
    def function1(self):   #instance methods 'self' as arguments
        print("function1 is working")
    def function2(self):
        print("function2 is working")    

class Bmw:
    @staticmethod
    def function3():
        print("function3 is working")
    @staticmethod
    def function4():
        print("function4 is working")

class Audi(Car,Bmw):
    def function5(self):
        print("function5 is working")
    def function6(self):
        print("function6 is working")

a1=Audi()
a1.function1() 
a1.function2() 
a1.function3() 
a1.function4() 
a1.function5() 
a1.function6()        





