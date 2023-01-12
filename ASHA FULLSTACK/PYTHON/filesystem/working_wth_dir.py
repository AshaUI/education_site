#directory is a folder or a place where we store our files, collection of related files
#working wth dir

import os
print(os.getcwd())  #getcwd()-get current working directory it returns path of current project path fr us

print(os.listdir()) #it gives list of names of all files in current folder

#create a directory
'''os.mkdir('mypics')  #mkdir()=make directory ,
                   #creating another folder/dir inside this currnt path(folder) with the name we give 'mypic',which is created at last

print(os.listdir())  #it gives list of names of all folders along with newly added folder(os.mkdir('mypics'))  in current folder 
 '''

 #change my folder name or rename the dir
'''os.rename('mypics','myimages')
print(os.listdir())#chnging mypics to myimages'''

#remove the dir
'''os.rmdir('myimages')  #rmdir()--remove dir
print(os.listdir())'''

#check if directory is ther in folder or not
print(os.getcwd())
check=os.path.isdir('D:\\ASHA FULLSTACK') # this path we have copied fron terminal and checking wether this folder is exted or not
                                          # it gives true or false  and stores in a variable ,and the path is only having single slash 
                                          #wen we run with sinlge slash its giving eror so add another slash to get error free op
print(check)  


#practise
#crete  .py file with some text read and append teh file


 
