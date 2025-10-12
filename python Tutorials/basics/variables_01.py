'''
Created on 12-Oct-2025

@author: chandan
comments : provides description about single line or block of a code , two types of comments 
single line comments : starts with # (hashtag) symbol
multi-line comments : starts with triple single quotes or double quotes  and ends with same notation 

variables : name given to memory location which stores input or output data and the data stored can be changed thats why the name is variable.
syntax : variable_name = value
'''

num2=8943
num3=7.84
name="chandan"
print(name)
print(id(name))
# Defining multiple variables in single line
num4,num5,num6 = 34,13,45
print(num4)
print(id(num4))
print(num5)
print(id(num5))
print(num6)
print(id(num6))

num9=47
print(num9)
print(id(num9))

#1.#while definnig the variables variable name should always be in left hand side and value should be in right hand sidebar
#2.variable name should start with character/letter it should not start with numbers
#3.numerical values dhould not start eith 0
'
num8,num7=89,60
print("num8:",num7)
print(num8,num7)
num8,num7,num4,num3,num5=70,60,50,40,50
print(num7,num5,num8,num4,"num3")
print("num3:",num8)