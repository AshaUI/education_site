#regular expression is also know an RegEx, are used to match the substring in the given string
#we ased to validate emial or password
#we shoukd import re wen we r wrkig with Regualr exprssn

#regular expression makes use of sequenc charecter t match single charecter in the given string 
''' 
\d- used to match single digit   i.e 0 to 9
\D--used to match non digit char
\s- used to match white spaces
\S-used to match non white spaces
\w-used to match alpha numeric char (a-z)
\W-used to match non alpha num char
\A-used to match start of string
\Z-used to match end of string'''
 


 # why "r" is suing in expression and when to group() when not to group
#Regular Expression methods
#search()-look for the pattren  tat we want to match in the string  from start to end if find it will return only one substring
import re
str="Take up one idea at a time"
result=re.search(r'o\w\w',str)
print(result.group()) #wen we want o print  seqof chars we should group them first so using group() method

result=re.search(r'i\w\w',str) #it takes from i and two oreceeded chars for 2 \w 's
print(result.group()) #wen we want o print  seqof chars we should group them first so using group() method

result=re.search(r'T\w\w\w\s\w\w',str) #it takes from i and two oreceeded chars for 2 \w 's
print(result.group()) #wen we want o print  seqof chars we should group them first so using group() method


#findall()-search for the pattren in regular exp string from the start to end,it will give as many srting matched 

str="Take up one idea.one idea  at a time"
result=re.findall(r'o\w\w',str)
print(result)  #it is returning all substrings which has specfc patrn

str="Take up one idea.one idea  at a time only"
result=re.findall(r'o\w\w',str)
print(result)   #its returnin all string started with 'o' and only 2 chars

str="Take up one idea.one idea  at a time "
result=re.findall(r'i\w\w',str)
print(result)   #its returnin all string started with 'i' and only 2 chars


 # match()  it is going to match only first most  char of entire reg exprssn

str="Take up one idea.one idea  at a time "
result=re.match(r'T\w\w',str)  #for T it is giving o/p but for i its not giving ,,why
print(result.group())   #it will give none 

str="iam asha "
result=re.match(r'i\w\w',str)  #for T it is giving o/p but for i its not giving ,,why
print(result.group())   #it will give none 

#substitute -means replace 

str="Take up one idea.one idea  at a time "
result=re.sub(r"one","two",str)

print(result)

#split() it splits at the point of dlemeter can be digit,\,space  anything

str="Take up 1 one 23 idea.one idea 45 at a time " #it seperates string with given spc char
result=re.split(r'\d',str)
print(result) #it placed "," where evr digits are , it placed 2 comms at 2 digit , 
                       #if want only one cooma evn digits are 2 then use quantifier"+"
result=re.split(r'\d+',str)
print(result) 


#practice qtns
#search()
#findall()
#substitute()
#split()
# match()






















#quantifiers
'''
*-zero or more occurences of preceeding RE
+-one or more occurences of preceeding RE
?-zero or one occurences of perceeding RE
{m}-exact m occurences of preceeding RE
{m,n}-m and n occurences of RE'''

'''str="Take up one idea on 21-12-2022"
result=re.search(r'\d{2}-\d{2}-\d{4}',str)
print(result.group())

#special charecters

\-escape charecter
.-matches exept new line
^-matches at the begining of the RE
$-matches at the end of RE'''

'''str='How rae you'
result=re.search(r'^H\w\w',str)
print(result.group())

str="How are you"
result=re.search(r'u$',str)
print(result.group())

str="How are you?"
result=re.search(r'\?$',str)
print(result.group())


#write a python function that matches an 'a' name zero or more b's(first 'a' and follwed by zero or more b's)


def match(text):
    pattern='ab*'
    if re.search(pattern,text):
        return 'found'
    else:
        return 'not found'    

print(match('abbc'))    #it checks a and zero or more b's   so found
print(match('ac'))    
print(match('bcc'))  #it checks first a and b's, as ther is no a so not found
print(match('bcca'))  #it checks first  so founda and b's,


#write a python program that matches an a follwed by one or more b's

def matches(text):
    pattern='ab+'
    if re.search(pattern,text):
        return 'matched'
    else:
        return 'not matched'    

print(matches('abbc'))    #it checks a and one or more b's   so matched
print(matches('ac'))     #it checks a and one or more b's  as ther is no b so notmatched
print(matches('bcc'))  #it checks first a and b's, as ther is no a so not found
print(matches('bcca'))  #it checks first  so founda and b's,and it checks a follwd by b so not matched
print(matches('bccab'))  #it checks first  so founda and b's,and it checks a follwd by b  so matched


#write a python prgrm tat matches an a and follwed by 3 b's
def matches(text):
    pattern='ab{3}'
    if re.search(pattern,text):
        return 'true'
    else:
        return 'false'    

print(matches('abbbc'))    
print(matches('ac'))   
print(matches('bcc'))  
print(matches('bcca'))  
print(matches('bccabbb')) 
print(matches('bbbcca'))  #checks fr a afolwd by 3 b's so not matched

def matches(text):
    pattern='a{2}b{3}'
    if re.search(pattern,text):
        return 'yes'
    else:
        return 'no'    

print(matches('aabbbc'))    
print(matches('bbbaac'))   
print(matches('bcc'))  
print(matches('bcca'))  
print(matches('bccabbb')) 
print(matches('bbbcca'))  #checks fr a afolwd by 3 b's so not matched

'''

'''str='1-1-2023'
result=re.search(r'\d{1}-\d{1}-\d{4}',str)
print(result.group())'''


'''str='12-12-2023'
result=re.search(r'\d{2}-\d{2}-d{4}',str)   #m occurences
print(result.group())


str='1-1-2023'
result=re.search(r'\d{1}-\d{1}-d{4}',str) #m n occurences
print(result.group())'''


























