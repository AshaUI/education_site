# check file
import os,sys

'''if os.path.isfile('myfile.txt'):  #checks for the file whether file"myfile.txt" existed or not
    f=open('myfile.txt','r')    #it  opens and reads content from file and stores  in s
    s=f.read()
    print(s)  #prints the stored code in o/p windw
    f.close()  

else:
    print("file does not exists")   #if file cudnt found or doesnt exist
    sys.exit()  '''

check_file=os.path.isfile('myfile.txt')
print(check_file)  #check_file is variable if file found it will pass true other wise fals   