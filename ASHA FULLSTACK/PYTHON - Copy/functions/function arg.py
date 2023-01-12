#function arguments 
def func(x):
    x=8
    print("x is",x)

func(6)    #just calling functn with some arg

def update(lst):
 print(id(lst))
 lst[1]=25
 print(id(lst))
 print( "list is",lst)

 lst1=[10,15,20]
 update(lst1)
#or another way to pass list itself as orgument
update([10,15,20])

