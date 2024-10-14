# DATA STRUCTURE
'''
1.List
2.Tuple
3.Dictionary
4.Set
'''
#List(ordered,indexed,duplication allowed,mutable(change))
'''a=["Hello",2,"red",3.2,True,"black",98,"red"]'''
'''print(a)
print(type(a))'''

#create a list by using list function

'''b=list((1,2,3,4,5))
print(b)'''

#item get from a list by index
'''print(a[0])
print(a[3])'''

#length
'''print(len(a))'''

#new item ad into a list
#1 append() ->item added into a last position
'''a.append('orange')
print(a)
a.append(100)
print(a)'''

#2 insert() ->an item added into specified position
'''a.insert(1,"apple")
print(a)'''

#replace an item in a list
'''a[2]="grey"
print(a)'''

#an item delete from list
#1, pop() -> last item deleted
'''a.pop()
print(a)'''
#2, pop(index)
'''a.pop(4)
print(a)'''
#3, remove -> specified item deleted
'''a.remove('black')
print(a)
a.remove('orange')
print(a)'''

#del ->delete whole list
'''del a
print (a)'''
#index() ->find index number
'''print(a.index('black'))
'''
#count()
'''print(a.count('hello'))
print(a.count('red'))'''

#number list
'''num=[23,5,1,2,9,5]'''

#sum
'''print('total',sum(num))'''

#max
'''print(max(num))'''

#min
'''print(min(num))'''



'''print(num[1]+num[3])'''

#sort
'''num.sort()
print(num)'''

#sorted
'''print(sorted(num))'''


'''
a=["Hello",2,"red",3.2,True,"black",98,"red"]
i=0
max_len=len(a)-1
while i<=len(a)-1:
    print(a[i])
    i+=1'''
# for loop
'''for i in a:
    print(i)'''


#range (start,end,step)
'''print(list(range(12)))
print(list(range(3,30)))
print(list(range(1,11,3)))'''



'''for i in range(1,11):
    print(i)


for i in range(2,11,2):
    print(i)

for i in range (1,11):
    if i%2==0:
        print(i)'''



#result needed is [3,5,5]

'''b=["red","black","white"]
c=[]
for i in b:
    max=len(i)
    c.append(max)
print(c)'''

#3 TUPLE(ordered,immutable,duplication is allowed,indexed)
#creation of tuple
a=('apple','airccraft','amazon','amazon',1,2,3,True)
'''print(a)'''
#finding length of tuple
'''print(len(a))'''

#create one item in tuple
'''B=('baloon')
print(type(B))

b=('baloon',)
print(type(b))'''
#create using tuple()
'''D=tuple(('design',))#->dout
print(D)
print(type(D))'''

#accessing the items in tuple
'''print(a[2])'''

#accessing the item using negative index
'''print(a[-1])'''#-> last item can be accessed
'''print(a[-2])'''#->second last item can be accessed

#Range
'''print(a[2:7])'''#->access from2-6
'''print(a[2:]'''#->access from 2 to last item
'''print(a[:5])'''#->access from 0-4

#Range of negative indexing
'''print(a[-4:-1])'''#->access from 4th element from last to 2nd element from last

#check item present in tuple
'''if 'apple' in a:
    print('yes,apple is presnet')
else:
    print('apple is not presnet')'''
    
#change tuple value
'''
a=('apple','airccraft','amazon','amazon',1,2,3,True)
y=list(a)
y[1]='switch'
a=tuple(y)
print(a)'''

#add item to tuple
'''
a=('apple','airccraft','amazon','amazon',1,2,3,True)
z=list(a)
z.append('False')
a=tuple(z)
print(a)'''

#add tuple to tuple
'''
a=('apple','airccraft','amazon','amazon',1,2,3,True)
v=('black',)
a+=v
print(a)'''
#add item to tuple using insert
'''
a=('apple','airccraft','amazon','amazon',1,2,3,True)
k=list(a)
k.insert(2,'phone')
a=tuple(k)
print(a)
'''

#remove item from tuple
'''
a=('apple','airccraft','amazon','amazon',1,2,3,True)
j=list(a)
j.remove("amazon")
a=tuple(j)
print(a)'''

#del
'''del a
print(a)'''

#clear is not in tuple but we can convert it into list and empty it
'''i=list(a)
i.clear()
a=tuple(i)
print(a)'''

















#22/07/24

#Dictionary (key:value) (ordered,unindexed,key unique,mutable)

student={'name':'john','age':20,'place':'calicut',23:76,'location':'calicut'}
'''
print(type(student))
print(student)
'''
#value access from a dictionaty

#1, using key
'''print(student['age'])
print(student['location'])
#print(student['data'])'''

#2, using get()
'''print(student.get('place'))
print(student.get(23))
print(student.get('data'))'''

#creating a dictionary by using dict function

'''a=dict ([('Employee','Tom'),('Salary',10000)])
print(a)
---------------------
b=[(1,2,3,4),('d','e','f'),{1:2,'string':'Tom'},[1,2,3]]
print(b)'''

#1, Updating a key value pair
'''student['age']=[90,23,12]
print(student)'''

#add a key value pair in a dictionary

'''student['color']='red'
print(student)'''

#2, update()
'''student.update({'subject':'english'})
print(student)'''

#clear ->clear the value inside the dictionary
'''student.clear()
print(student)'''

#len
'''print(len(student))'''

#deleting a pair from dictionary

#1,popitem() ->last pair deleted
'''student.popitem()
print(student)
'''
#2, pop()
'''student.pop('age')
print(student)'''

#3, del
'''del student['name']
print(student)'''

#4, del ->delete dictionary
'''del student'''
#copy
'''sam=student.copy()
print(sam)'''

#any function
'''mydict={False:'red',False:'balck'}
print(any(mydict))

mydict={True:'red',False:'balck'}
print(any(mydict))'''

#all function
'''mydict={True:'red',False:'balck'}
print(all(mydict))

mydict={True:'red',True:'balck'}
print(all(mydict))

mydict={False:'red',False:'balck'}
print(all(mydict))'''

#sorted

'''d={1:'red',8:'black',3:'violet',5:'gray'}
print(sorted(d))'''


'''for i in student:
    print(i)'''

'''for i in student.values():
    print(i)'''

'''for i in student.items():
    print(i)'''
'''print(student.keys())'''
'''print(student.values())'''
'''print(student.items())'''

#set (collection of unique data)(inordered,unindexed,duplication not allowed,mutable)
mixed_set={'hello','red',23,'blue',45.9,12,True,'red'}
'''print(mixed_set)
x=set()
print(x)#empty set
print(type(mixed_set))'''

#create a set by using set function
'''a=[1,45,3,7,0,9]
b=set(a)
print(b)'''


#add new item into an set

#1, add()
'''mixed_set.add('apple')
mixed_set.add(90)
mixed_set.add(('html','css'))
print(mixed_set)'''

#2, update
'''mixed_set.update('kiwi')
print(mixed_set)

mixed_set.update(('orange','banana'))
print(mixed_set)'''

#delete an item from set
# 1,discard()
'''
mixed_set.discard('hello')
mixed_set.discard('hi')
print(mixed_set)'''

#2, remove
'''mixed_set.remove('blue')
print(mixed_set)'''

'''mixed_set.remove('hi')''' #-> keyerror
'''print(mixed_set)'''

#clear
'''
mixed_set.clear()
print(mixed_set)
'''

#del
'''
del mixed_set
print(mixed_set)
'''

#len
'''
print(len(mixed_set))
'''

#copy
'''
x=mixed_set.copy()
print(x)
'''


# union

'''
a={20,20,60,35,25,90,45}
b={99,66,30,77,45,90,11}
print('union:',a|b)
print('intersection:',a&b)
print(a-b)
print(b-a)
print(a^b)'''


'''
print(total)
additin(23,56)
addition(90,56)'''


#29-july

#functions - independent block of code which only runs when it is called, code reusability
'''
1.Built-in functions
2.User-defined functions

def function_name():
    body

'''

'''def sample():
    print('Hello world')
sample()'''

#giving input inside function
'''
def sample(name):      #variable/parameter/position argument
    print('hello',name)
sample("Tom")             #argument
'''
'''
def sample(name1,name2):
    print('hello',name1,name2)
sample("tom",'john')

def sample(name):
    print("hello",name)
sample('tom')
sample('john')'''

#function to add

'''def add(a,b):
    print(a+b)
add(2,3)
add(10,15)'''

#function to add - user input

'''def add(num1,num2):
    x=num1+num2
    print("result : ",x)
a=int(input('enter 1st number : '))
b=int(input('enter 2nd number : '))
add(a,b)'''

#scopes - local and global variable

'''def sample():
    x=45                #local variable
sample()
print(x)'''

'''x='hello'            #global variable
def sample():
    print("value of x : ",x)
sample() 
print(x)'''


#local and global

'''data="hello"  #global variable
def index():
    x=34 #local variable
    global y
    y=100
    print('value of data',data)
index()
print(data)
print('value of y is:',y)'''


#1, position Arguments
'''
a=int(input('enter your num1:'))
b=int(input('enter your num2:'))
def addition(num1,num2):
    total=num1+num2
    print(total)
addition(a,b)
'''

#2, keyword Argument

'''
def student(name,age,subject):
    print('name of stud:',name)
    print('age of stud:',age)
    print('intrested subject:',subject)
student(subject='english',name='john',age=23)
'''

#3, default parameters

'''
def multiply(a=10,b=2):
    print(a*b)
multiply(20,20)
multiply()
'''

# find the sum of numbers in a list
'''
li=[2,4,6,8]
def addlist(a):
    x=0
    for i in a:
        x=i+x
    print(x)
addlist(li)
'''

#30/07/24

#4, Arbitary positional Arguments(*args)
'''
def student_name(*name):
    print(name[0])
student_name('john','ram','tom')
'''
#5, Arbitary keyword Arguments (**kwargs)
'''
def employee_details(**data):
    print(data)
    print(data.get('name'))
    print(data['salary'])
    print(data.items())
employee_details(name='kevin',salary=10000,position='developer')
'''

#return
'''
def add(a,b):
    return a+b
print(add(2,3))
'''

#function pass into another function
'''
def twice_add(fun,x,y):
    return fun(fun(x,y),fun(x,y))

def add(x,y):
    return x+y


a=5
b=10
print(twice_add(add,a,b))

'''

#recursive function(function that call itself)

'''
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
print(factorial(5))
'''


#Modules (set of functions)
'''
import random
for i in range(5):
    print(random.randint(2,30))

import math
print(math.pi)
print(math.sqrt(100))

from math import *
print(pi)
print(sqrt(200))

from math import pi,sqrt
print(pi)
print(sqrt(200))


from random import randint
print(randint(2,30))

from random import *
print(randint(2,30))
'''
# 31/07/24
#Anonymous function

# lambda function

# lambda arguments:expression (it takes no.of arguments but execute single expression)
'''
a=lambda x:x+5
print(a(10))

b=lambda a,b:a+b+7
print(b(4,3))
'''
#odd or even using lambda
'''
num=lambda x:'Even' if x%2==0 else "Odd"
print(num(2))
print(num(3))
'''
#greater or smaller using lambda
'''
c=lambda x,y:x  if x>y else y
x=int(input('enter the first number:'))
y=int(input('enter the second number:'))
print(c(x,y))
'''
#qstn:if i/p id 15 or greater print i/p*10 if i/p is less than 15 and greater then 5 print i/p if i/p less than 5 print i/p*5
'''
y=lambda x: x*10 if x>=15 else(x*5 if x<=5 else x)
x=int(input('enter the number:'))
print(y(x))
'''

#, map (function,iterable)
'''
def fun(x):
    return x*2
num=[1,2,3,4]
a=map(fun,num)
print(list(a))
'''

'''
def fun(x):
    return 1/x
num=[4,8,3]
a=map(fun,num)
print(list(a))
'''
'''
y=map(lambda x:1/x,[4,8,3])
print(list(y))

a=lambda x:1/x
b=map(a,[4,8,3])
print(list(b))
'''

#filter(function,iterable)

def even(z):
    if z%2==0:
        return True
    else:
        return False
num_list=[2,34,5,6,7,8,9]
data=filter(even,num_list)
print(list(data))




































