#3-11-2022
#input output function
#print() --it is inbuilt function which writes to user console
#input()---it is in built function that allows user input

#print()
print()
print('hi*3')
print('hello'*3) #  hello 3 times
print('python is to learn \n to learn than java') 
a,b=10,20
print(a,b)
print(a,",",b)
print(a,b,sep=',')
c=30
print(a,b,c,sep=',')#to print "," btwn values#

#formatting using print
name="jhon"
marks=90.5
print("name is",name,"marks are",marks)

#formate using .format()
age =30
print("name is {},marks are {}".format(name,marks))
print("name is {0}, marks are {1} age is {2}".format(name,marks,age)) # number place holder
print(f"name is {name},marks are{marks}, age is{age}")  # name place holder

#practice qtn
#logical operators
#member ship operators
#comparision operators
#use formate method to print

#4-11-2022

# input function -- input from user'''
'''s=input()
print(s)
x=input('enter your name:')
#print(s)
y=(input('enter 2 nd num'))
z=x+y  # with out int() it is taking x and y as strngs so doing--concatinating
# print(z)
print(type(x))  # now type is int with out int type will be str
print(type(y))
print(type(z))
x=int(input("enter 1 num:"))
y=int(input("enter 2 num:"))
z=x+y
print(z)-----givs num op'''



#read the charecter using i/p func
'''ch=input("enter a charecter")
print(ch[1]) #gives 1 index char
print(ch)
ch=input("enter a char")[3]   #gives 3 index elem
print(ch)'''


#reading expressions using input()
#result=eval(input)
'''x=6
y=7
a=input("enter a expression")
z=eval(a)
print(z)'''


#raeding multiple inputs

'''lst=[int(x) for x in input("ente val:").split()]   #mulitpke int inputs frm user
print(lst)'''
#print(type(lst))
#lst=[float(x) for x in input("ente  float vals:").split()]  #mulitpke float inputs frm user
#print(lst)

'''lst=[x  for x in input("enter strs:").split()]  #mulitpke str inputs frm user
print(lst)'''
'''x,y=[int(x) for x in input("enter values:").split()]
print(x+y)'''

#map()  for accepting multiple user inputs

'''mi=list(map(int,input("enter int inputs").split()))
print(mi)'''

mf=list(map(float,input("enter float inpts:").split()))
print("float otpts are",mf)
ms=list(map(str,input("enter str inputs:").split()))
print("string opts are:",ms)



##print(b)
#practice qtns
#read charecter from user
#read expression from user
# raad multiple inputs from user
#read multiple input from user using map()
#take two num from user and multiply tehm
















































