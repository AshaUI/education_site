a=(10,20,30)
print(a)
print('hi')
print("let's learn python")
print('let"s learn python')
#assing string to var
s='python is easy'
print(s)
#indexing 
print(s[9]) #  indexing o/p is space
print(s[0])
print(s[3])
print(s[-4]) # -ve indexing o/p is e
print(s[-2])  # -ve indexing o/p is s
print(s[-14])
print(s[-13])
str1='life is precious'
print(str1[2])
print(str1[8])
print(str1[1])
print(str1[7])
print(str1[-1])
print(str1[4])
#lenght
print(len(str1))  #lenght 16 index starts  from 0-15

#slicing in strings
s='python is easy'
print(s[0:9]) # it  takes 0-8 indx alph includes 0 index alphabet nad excludes from 9 
print(s[:7])
print(s[10:])  # it includes 10 index alphabet nad prints till end
print(s[7:9]) # it includes 7 index alphabet nad excludes from 9 so it prints 'is'

str1='life is precious'
print(str1[11:])
print(str1[8:11]) # it includes 8 excludes 11 prints 8-10 'pre'
print(str1[1:4])
print(str1[14:])
print(str1[-2:])
print(str1[:-10])
#assingments 
# s1='levelup'
# print elup,up,p,level
s1='levelup'
print(s1[3:])
print(s1[5:])
print(s1[-1:])
print(s1[0:5])

# passing step values to slices
s="012345678954321"
print(s[0:9])
print(s[0:13:3]) #skips 3 rd and all 3 multiple chars
print(s[::-1]) #prints string in reverse order
s='0123456789'
print(s[1:6])
print(len(s))
print(s[::3])#print 3 multiples in order
print(s[::-3])#prints 3 multiples in revers order
print(s[::1]) # prints 1  multiples in order
print(s[::-1])#prints 1 multiple in rev order

#string methods -- 
# strip method--it removes spaces at end 
s='  you are awsome  '
print(s.strip())
print(s.lstrip()) # left hand spaces will be removed 
print(s.rstrip()) # right hand spaces will be removed 
#find() method used to locate substring in'you are' are is sub strin snd yo ou---- it returns index of first lettr in sub string
print(s.find('you'))# it returned index of y is 2
# count() will give no of single same typ of charecters
print(s.count('a'))

print(s.count('y'))

#replace() it replaces
print(s.replace('you','cool'))
print(s)  #we just replaces but not stored

#upper()'lower(),title()
print(s.upper())
print(s.lower())
print(s.title())
# split() it will split string in to substring if it finds any separators separator can be space  ,  .  
a='hello,world'
print(a.split(','))
b='he lloworld'
print(b.split())
# 'is keyword checks is variable dig,alph.... and it can also checks acc index
s='123a #'
print(s.isdigit())
print(s[1].isdigit())
print(s[3].isspace())
#count() it can count single digit and a string also
print(b.count('o'))
print(s.count('a'))
print(s.count('123a'))
#startswith(),endswith(),swapcase(),   in not in checking mthods
y='they are we are you are'
print(y.count('are'))
print(y.startswith('t'))
print(y.endswith('a'))
print(y.swapcase())
print('They' in y)
print('are' not in y)
print('arent' not in y)
# string concatination is joining ,combining,or adding
x='hello'
y='world'
print(x+y)
x='hello'+'100'
age=26
marks=88.8
name='Asha'
txt='i am {} i am {} year old and my marks are {}'
print(txt.format(name,age,marks))
 # string are immutable we cannot change add or replace 

#string methods strip(),split(),count(),is(),upper(),lower(),title(),len(),startswith(),endswith()
#in ,not in