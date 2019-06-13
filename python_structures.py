
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:12:05 2019
@author: pedrocampelo
"""


#VARIABLES TYPES
#String is a text variable
#Floats are the number with comma (not integer)
#Int represent the number that are strictly integers (removes all dots)


b = 125.0           #float
c = 390.8           #float  - import to remember that comma are replaced by dot in python
print(int(b))       #float -> int
print(int(c))       #float -> int

d = 134             #int
print (float(d)     # int -> float
       
name='Pedro'
lastname='Pedro Campelo'
name_lastname=name+' '+last_name
print ('My name is', name_lastname)

lines_yesterday = "50"        #string
lines_today = "108"           #string
       
lines_total = lines_yesterday + lines_today    #trying to add two strings
print(lines_yesterday)  
Output: "50180"             #soma os caracteres da string
       
lines_total = int(lines_yesterday) + int(lines_today)    #string -> int: now works
print(lines_yesterday)   
       
lines_more = lines_today - lines_yesterday      #trying to subtrate two strings
print(lines_more)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
       
lines_more = int(lines_today) - int(lines_yesterday) #string -> float: now works
print(lines_more)


"""
For other cool stuff with string, float, int check: 
https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3
"""


       
#LIST 
#List is a mutable ordered sequence of elements that is contained within square brackets [ ]

# Declaring a list 
L = [1, "a" , "string" , 1+2] 
print (L) 



L2=[]                      #Creating a list with a looping
for i in range(10):
  L2.append(i)
  print(L2)
  
L3=[x for x in range(10)]  #Creating a looping inside a lista
print (L3)


# Important remember that the first list index is the number 0 and the last one is (n-1)
len(L)              #finding the lenght os the list
print (L[0])        #1st element of the list
print (L[len(L)])   #Nst element of the list 
print (L[1:3])      #2nd to the 4th elemen in the list

# Append: add a element in the end of the list 
L.append(6) 
print (L) 
  
#Insert: add a element by position
List = ['Mathematics', 'chemistry', 1997, 2000] 
List.insert(2,10087)        # Insert at index 2 value 10087  
print(List)    
  
 
# Pop: deletes the last element of the list 
L.pop() 
print (L) 
 
  
#Del: delet element by position
 
del L[2]  
print (L)


#Remove: delet element by its value
animal = ['cat', 'dog', 'rabbit', 'guinea pig']
animal.remove('rabbit')     # 'rabbit' element is removed


"""
For other cool stuff with lists check: 
https://www.geeksforgeeks.org/inbuilt-data-structures-python/
"""



#TUPLE
#Tuple is an immutable ordered sequence of elements contained within parentheses ( )

#SET


#DICTONARY (DICT)

#






