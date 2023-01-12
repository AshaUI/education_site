#FSD  - Test 1
#1.In the given tuple add 'india'
tpl=('usa','uk','canada')
tp2=list(tpl)
print(tp2)
tp2.append('india')
print(tp2)
tpl=tuple(tp2)
print(tpl)


#2.Reverse the string
s='Python Traning at Levelup'
print(s[::-1])


#3.print numbers divisibe by 3 and 5 between 1 to 100
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)

#4.Write a python program to print odd numbers in a range
for i in range(1,35):
    if i%2!=0:
        print(i)

#5.Write a python program to generate multiplication table 
for i in range(1,11):
    print("2*",i,"=",2*i)
# a given number
#6.A person named Sahil,as a citizen of nation has a right to vote.
   #Considering minimun age to vote write a function in python that he is 
   #eligible to vote.
def eligibility(x) :
 if x>=18:
    print("person eligible to vote")
 else:print("not eligible to vote") 

eligibility(21)   
eligibility(17)

'''7.create a module by name module1,write three functions in it - add,sub,mulitply
two numbers,how would you excute only  multiply  function in a module named module2'''
'''module1.py
 def add(x,y):
    return x+y

 def sub(x,y):
    return x-y

 def multiply(x,y):
    return x*y'''

from module1 import multiply 

print(multiply(2,3))    

#8.John knows following list of technologies - python,java,django,html ordered on the
#basis of his proficiency in them(highest to lowest),but for an interview he had to be 
##proficient in django more then java and also he requires basic knowledge of css that could
#be least prioritized.How do you help John with this ?

lst=['python','java','django','html']
lst.remove('java')
lst.insert(2,'java')
lst.append('css')

print(lst)

#9.Write a lambda to print only odd numbers from list
lst=[1,2,3,4,5,6,7,8]
result=list(filter(lambda x:x%2!=0,lst))
print(result)

#10.type cast the below
    # 1.int to float
x=12
y=float(x)
print(type(y))

    # 2.tuple to set
tpl=(1,2,1,1,2,3,4)
s=set(tpl)
print(s)
    # 3.str to int'''
x="10198"
y=int(x)
print(type(y))