#multi level a--> b-->c     b is inhering from a  c is inhriting from b

class A:
    def feature1(self):
        print(" feature1 is working")
    def feature2(self):
        print(" feature2 is working")
class B(A):  #B is child of A
    def feature3(self):
        print(" feature3 is working")
    def feature4(self):
        print(" feature4 is working") 

class C(B): #C is child of B  so c can inherit A properties also
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