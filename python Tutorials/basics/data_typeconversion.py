'''
Created on 15-Oct-2025

@author: Admin

'''
from basics.data_types import num8
num1 = 23 # int
num2 = 34.5 # float
num3 = 4+5j # complex
name = 'Vivek' # str
var1 = True # bool
var2 = False # bool
var3 = None # NoneType

print("Type of num1:",type(num1))
print("Type of num2:",type(num2))
print("Type of num3:",type(num3))
print("Type of name:",type(name))
print("Type of var1:",type(var1))
print("Type of var2:",type(var2))
print("Type of var3:",type(var3))

print("=======converting in to data type=======") 
#int to all other
num4 = float(num1)
print('num4:',num4)
print("type of num4:",type(num4))
num5 = complex(num1)
print('num5:',num5)
print("type of num5:",type(num5))        
num6 = str(num1)
print('num6:',num6)
print("type of num6:",type(num6))
num7 = bool(num1)
print('num7:',num7)
print("type of num7:",type(num7))
#float to all other
num = int(num2)
print('num8:',num8)
print("type of num8:",type(num))
num9 =complex(num2)
print('num9:',num9)
print("type of num9:",type(num9))
num10 =bool(num2)
print('num10:',num10)
print("type of num10:",type(num10))
#complex to all other
num11 =float(num3)
print('num11:',num11)
print("type of num11:",type(num11))
print(123)
      
       