#naming a module--we can give any name to modules and save with .py extension
#Re naming a module-we can give an alias name to kodule by using 'as' keyword
# for renaming and importing a part of code we have to first import that file then rename and then import a apart of code
import calc 
print(calc.person['city'])

#renaming calc as ca
import calc as ca
print(ca.person['age'])

#importing one part of code

from calc import person  #we dont need any code other than person
print(calc.person['name'])
print(calc.lst[3])