#write a python prgrm to reverse the string
s='python training at levelup'
print(s[::-1])
#in the below string remove spaces
s='  python is easy  '
print(s.lstrip())
#using string concatination join
mystr="todays date is"
mystr2='28/10/2022'
print(mystr+mystr2)
txt='todays date is{}'
mystr='28/10/2022'
print(txt.format(mystr))
#create a list add multiple element to list remove lat elementsand empty the list

lst=[1,2,3]
lst2=[4,5,6]
print(lst+lst2)
lst.extend([4,5,6])

lst.pop()
print(lst)
lst.clear()
print(lst)

#change 'hi' to 'hello in tuple
x=('hi','hey','bey')
y=list(x)
y[0]='hello'
x=tuple(y)
print(x)











    




