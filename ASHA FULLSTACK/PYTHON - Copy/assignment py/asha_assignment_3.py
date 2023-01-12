#1creat string,display it and  checks it data type

a="aisha"
print(a)
print(type(a))

s="django"
#2use  index to print out the following and also reverse the above string
"d" "o" "jan" "djan" "go" 
print(s)

print(s[0])
print(s[5])
print(s[1:4])
print(s[0:4])
print(s[4:])
print(s[::-1])
#3demonstrate following string methods on given strings

S='  learning python at level up  '
print(S)
#remove white spaces on both ends

print(S.strip())
#show thr occurences of charector in string
print(S.count("e"))
#locate substring
print(S.find('at'))
#print the length of string
print(len(S))
#split te string into substring
print(S.split())
#represent the different cases 
print(S.upper())
print(S.lower())
print(S.title())

4#concatinate the following string
x="With Levelup I'm on cloud" + '9'
print(x)

#5.justify how strings are immutable 
s3='levelup'
#s3[1]='a'
#print(s3)

#6.Find the length of string 
mystr= 'levelup Institute'
print(mystr)
print(len(mystr))
#7.Using suitable string manipulation print the below output
'levelup levelup levelup'
a=b=c='levelup'
print(a,b,c)
