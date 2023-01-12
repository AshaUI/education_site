#file ids where we store our data
#data can be anythig like text data,binary(images,audio,vedeo, etc)

#open file syntax
#f=open('filename','modes')

#close file syntax
#f.close()

'''modes
w-write to file(every time writes new content to file)
r-read from file
a-append to file (current content of file will not be deleted'''

#modes of binary files
#wb   ,rb   ,ab

#write string to a file
'''f=open('myfile.txt','w')  #opening a file ,it will automatically creates new file with the name we given,
s=input("enter text:")    #text we have to write should store in a variable  (s)
f.write(s)  #writing the content wich is stored in s to file by using statement f.write()
f.close() '''  #after any operation we should cles the file
#after entering a text while run time we can go and check in myfile, text will be there

#after entering a  single text the control is coming out, its not taking other string so fr that  we need to use condition 

#write multiple strings to a file
f=open("myfile.txt",'w')
print("enter text,type # when you r done")
s=''
while s!='#':
  s=input()  #takes input
  f.write(s) #enters input in file
  f.write('\n') #after evry single string it will take new line for new srting,while run time if we enter # control will come out

f.close()  
