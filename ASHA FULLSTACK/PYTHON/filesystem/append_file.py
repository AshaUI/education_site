#append to file --adding text to already written file

f=open("myfile.txt",'a')  #as we re adding to already existed file so took 'a'
s=input("enter text to be added:")
f.write(s)
 
f.close
'''f=open("myfile2.txt",'a')
s=input("enter string to be aded:")
f.write(s)

f.close()'''