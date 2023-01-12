#1.Given the tuples:
t1=("hi",1,2,5)
t2=(6,7,8)
#Concatenate the tuples.'''
print(t1+t2)

   
#2.Create tuples using constructors. 
tp1=tuple(('python',2,4,6,8)) 
print(tp1)
#3.change the tuple item from 'tulip' to 'lotus' in  below tuple using suitable method
tp=('rose','lily','tulip','jasmine')
tpl=list(tp)
print(tpl)
tp1[2]='lotus'
print(tp1)
tp=tuple(tp1)
print(tp)
print(tp)

#4.Demonstrate working of copy function for tuples.'''
t1=("hii",'bye','hi')
'''t2=t1.copy()
print(t2)'''
#5.Given tuple:
#demonstrate membership test.'''
tuple=('c','o','o','l')
print('c' in tuple)
print('o' not in tuple)
print('L' in tuple)