#Exceptions run time are errors{logical error-logic not currect,compiletime error,syntax error,run ime}
#when ever python program is exicuting ,if something goes wrong , an exeption will be raised, and if we dont handle those exptns crrclty it couses 3 things
#1. it 
#exceptions are run time errors,when our python program is executing,if something goes wrong
#an exception is raised and if we dont handle those exceptions correctly,it causes 3 things:
#1.displays unfriendly/unformal information to the user
#2.improper shutdown of resources-editors or terminals
#3.abnormal termination of program-

'''a,b=[int(x) for x in input("enter two numbers:").split()]
c=a/b
print(c)'''
#we use try except  as try catch

#try:
   #code that might raise error
#except:
   #except block code 
#else:
#   #will excecute along with try  
#finally:
#   #however executes whether thr is error or not
#if our expression has chanses to raise any error 
# from zer ,name,attribute we can just give exxept : to catch any error
'''try:
    a,b=[int(x) for x in input("enter two numbers:").split()]
    c=a/b
    print(c)
    print(d)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter non zero number")
except NameError:
    print("variable has not defined")

print('code after exception')'''


#finally will however execute along with try and except block
'''try:
    f=open('expfile.txt','w')
    a,b=[int(x) for x in input("enter two numbers:").split()]
    c=a/b
    f.write("writing %d into file"%c)
    print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter non zero number")
finally:
    f.close()
    print('file closed')

print('code after exception')'''


#else block will execute along with try block

'''try:
    f=open('myfile.txt','w')
    a,b=[int(x) for x in input("enter two numbers:").split()]
    c=a/b
    f.write("writing %d into file"%c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter non zero number")
else:
    print("You have entered non zero number")    
finally:
    f.close()
    print('file closed')

print('code after exception')'''
'''try:
  print(x)   #as this is giving error ecxept block will be executed with right msg

except:
    print("plese define x") 

try:
  x=2
  print(x)  #as x is already defined expt block will b skipped

except:
    print("plese define x") '''

#Practice questions
#Attribute error
#value error
#indentation error  
#Name error
#practice questions

#Attribute error
try:
    x=10
    x.append(6)
    print(x)
except AttributeError:
    print("int has no attribute append")
#value error
try:
    x=int("xyz")
    print(x)
except ValueError:
    print("you have entered wrong value" )
#indentation error
try:
    s=("hi")
    print(s)
except IndentationError:
    print("indentation error occured")
#Name error
# try:
#     name=(sadhik)
#     print(name,'Its a Beautiful day')
# except NameError:
#     print('please enter name in single quote or double quote')
#index error
try:
    l=[1,2,3,4]
    l[4]
except IndexError:
    print('list index position is out of range')
#syntax error
try:
    print ("hi")
except SyntaxError:
   print("you have entered incorrect syntax")
#key error
try:
    d1={1:'sadhik',2:21,3:'roman'}
    d1[4]
except KeyError:
    print("you have entered wrong key value")
try:
   s2={1,2,3,4}
   print(s2)
   s2.remove(6)
except KeyError:
    print('you entered the element out of range')
#type error
try:
   'hi'+3
except TypeError:
    print('you cannot concatenate string to int')   
  

''' #"raise"  key word  -which raises error with given name and given msg
  # 
  # x = 1
print("x is int")
y = 1
if not type(x) is str:
  raise TypeError("Only str are allowed")
'''
