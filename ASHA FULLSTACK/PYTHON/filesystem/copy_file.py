#copy file-in this we are working with binary files i. e image files

#copy means reading and writing
f=open('mypic.jpg','rb')
f1=open('ashaimg.jpg','wb')
print(f1)  #at this stage (ashaimg.jpg)file created but its empty
for i in f:
    f1.write(i)  #it writes i from f to f1

print(f1)       #at this (ashaimg.jpg) written with imga from f

f2=open('textforcopy.txt','rb')
f3=open("copyingtext.txt",'wb ')

for i in f2:
    f3.write(i)

print(f2)    

'''f=open('cons logo.png','rb')
f1=open('cons logo2.png','wb')
for i in f:
    f1.write(i)'''

    #un able to copy text file