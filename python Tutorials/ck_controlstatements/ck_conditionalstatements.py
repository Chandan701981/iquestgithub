'''
Created on 16-Oct-2025

@author: chandan
indentation: it is the leading space to define a block of code
1 indentation: 1 tab space = 4 normal spaces
conditional staements: flow of program execution will be decided based on a condition
(decision making statement)

1. if statements
2. if-else statements
3.series if-else statements
4.nested if-else statements
'''
#

age = int(input("please enter your age:"))


if age > 0:
    if age<=3:
        print("you're a toddler")
    elif age<=12:
         print("you're a child")
    elif age<=18:
         print("you're a teenager")   
    elif age<=60:
         print("you're an adult")
else:
        print("you're senior citizen") 
        
  
         
    

  