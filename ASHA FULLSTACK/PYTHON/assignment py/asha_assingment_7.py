#1.Demonstrate the following functions for dictionaries:
d1={'name':"John",'age':30,'city':"delhi",'country':"India"}
#1.copy
d2=d1.copy()
print(d2)
#2.dictionary constructor
d3=dict(name="jhon",age=30,city="delhi",contry="india",gender='male')
print(d3)
#3.length of dictionary
print(len(d3))

#4.remove item from the dictionary
d1.pop('country')
print(d1)

#5.delete dictionary
del d3['gender']
print(d3)
d3.clear()
print(d3)
  
#2.using keys and indexing,print 'python; from the dictionaries:'''

d1={'key':'python'}
print(d1['key'])
d2={'key1':{'key2':'python'}}
print(d2['key1']['key2'])
d3={'key1' : [{'nest_key':["let's learn",['python']]}]}
print(d3['key1'][0]['nest_key'][1][0])
# 3.Given the dictionary change empid to "AA22"
thisdict = {
  "emp_name": "Rahul",
  "emp_id": "AA11",
  "emp_salary": 10000
}  
thisdict['emp_id']="AA22"
print(thisdict)
#4.Refering dictionary in question 3 add an item to this dict dictionary, and also delete the same item added to the dictionary.
thisdict['emp_age']=30
print(thisdict)
del thisdict['emp_age']
print(thisdict)
#below methods will also work
'''
thisdict.pop('emp_age')
print(thisdict)
thisdict.popitem()
print(thisdict)'''





