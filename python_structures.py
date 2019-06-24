
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:12:05 2019
@author: pedrocampelo
"""


#VARIABLES TYPES

#FLOAT
#Floats are the decimal number (with dot)

b = 125.0           #float  - import to remember that comma are replaced by dot in python
c = 390.8           #float  - import to remember that comma are replaced by dot in python
print(int(b))       #float -> int
print(int(c))       #float -> int

#INT
#Int represent the number that are strictly integers (removes all dots)

d = 134             #int
print (float(d)     # int -> float
    
#STRING  
#String is a text variable
name='Pedro'
lastname='Pedro Campelo'
name_lastname=name+' '+last_name
print ('My name is', name_lastname)

       
#operations e transformations
lines_yesterday = "50"        #string
lines_today = "108"           #string
       
lines_total = lines_yesterday + lines_today    #trying to add two strings
print(lines_yesterday)  
Output: "50180"             #soma os caracteres das duas strings
       
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

#Creating a list with a looping
L2=[]                      
for i in range(10):
  L2.append(i)
  print(L2)
  
#Creating a list with a looping inside the list
L3=[x for x in range(10)] 
print (L3)


# Important to remember that the first list index is the number 0 and the last one is (n-1)
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
print(animal)


"""
For other cool stuff with lists check: 
https://www.geeksforgeeks.org/inbuilt-data-structures-python/
"""



#TUPLE
#Tuple is an immutable ordered sequence of elements contained within parentheses ( )
#Python tuples work exactly like Python lists except they are immutable, i.e. they can’t be changed in place
       
t0=()                       #An empty tuple
t1 = (0, )                  #A one-item tuple (not an expression)
t2 = (0, 1, 2, 3)           #A four-item tuple
t3 = 0, 1, 2, 3             #Another four-item tuple (same as prior line, just minus the parenthesis)
t3 =(‘abc’, (‘def’, ‘ghi’)) #Nested tuples

       
       
#SET
#Unordered collection of unique objects.
#Set operations such as union (|) , intersection(&), difference(-) can be applied on a set.
#Sets are immutable i.e once created further data can’t be added to them () are used to represent a set.
#Objects placed inside these brackets would be treated as a set
       
       # Python program to demonstrate working of 
# Set in Python 
   
# Creating two sets 
set1 = set()                                     #creating with a for
for i in range(1, 6): 
       set1.add(i)       
 
lista2=[for i in range(5)]                       #creating a set from a list
set2=set(lista2)       
   
# Adding elements to set1 

   
# Adding elements to set2 
for i in range(3, 8): 
    set2.add(i) 
   
print("Set1 = ", set1) 
print("Set2 = ", set2) 
print("\n")

       
       
#DICTONARY (DICT)
#Consists of key value pairs. The value can be accessed by unique key in the dictionary.
#Keys are unique & immutable objects. Syntax:

#      dictionary = {"key name": value}  

      
# Create a new dictionary  
d = {}        # or d = dict() # 
d={'key1':'value1', 'key2': 'value2', 'key3':'value3'}
       

print (d)              #print the whole dictionary
print (d.keys())       # print only the keys
print (d.values())     # print only values 
print (d.items)        # print a tuple (keys,values)

  
# iterate over dictionary  
lista1=[x for x in range(2)]
lista2 = []
for i in range(len(lista1)):
       lista2.append(2*i)
       
#or lista2=[2*x for x in range(2)]
   
d2={}
for i in range(5):
       d2.update('valor'+str(i):lista1[i])
       
#if want to change the value in a dict can use the same dict.update() function:
for i in range(5):
       d2.update('valor'+str(i):lista2[i])       
       
       
for index, value in enumerate(d2):                          # another method of iteration 
    print (index, value , d[value]) 
  

print '(valor2' in d2)             # check value in a dict  
del d['valor2']                    # delete the key-value pair 
print '(valor2' in d2)             # check again  


"""
For other cool stuff with lists check: 
https://www.geeksforgeeks.org/python-set-4-dictionary-keywords-python/
"""
       

#Dataframe

#Creating a dataframe from a array (vector) of lists
df1 = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['col1', 'col2', 'col3'])

#Creating a dataframe from a dict (i usually do this most)
dict_aux = {'col1': [1, 2], 'col2': [3, 4], 'col3':[5,6]}
columns_aux = ['colum1', 'colum2', 'colum3']
df = pd.DataFrame(data=dict_aux, columns=columns_aux)

df.head(10)
df.tail(15)
df.columns
sum(df.colum1)
max(df.colum1)
df['colum5']=df['colum1'] - df['colum3'].mean()         #subtracting another column mean
df['column1_t-1']=df['colum1'].shift(1)                 #select the above line


#concat two dfs with the SAME columns:
#if the columns are not the same, total of columns of the result will include all includes in the concated dfs with some NA values

 df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']},
                     index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                     'B': ['B4', 'B5', 'B6', 'B7'],
                     'C': ['C4', 'C5', 'C6', 'C7'],
                     'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])
        

 df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                     'B': ['B8', 'B9', 'B10', 'B11'],
                     'C': ['C8', 'C9', 'C10', 'C11'],
                     'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])

df_zao = pd.concat([df1,df2,df3])

df_zao_aux = df1.append(df2)
df_zao = df_zao_aux.append(df2)           #it can also be done with append function


#to filt the dataframe, just select cols:

df[df['col1']==2]

for i in len(df['col1']):
    if df['col1'][i]==1:
        print (i) 

#Also check groupby library to see other cool filters

"""
For other cool stuff with lists check: 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
"""
