#pickle dump ---picke is alreddy exisped module tat has methods of loading(writing) and dumpimg (reading)
import pickle,student  #importing both picke module to serialize  and student module to pass values to class variables
'''f=open('student.dat','wb')
s=student.Student(11,'jhon',90.5)
pickle.dump(s,f)  #this lin dumps above given values to student file  of Student class

f.close()'''

f=open('emp.dat','wb')
e=student.Employee(101,40000)
pickle.dump(e,f)
f.close()

