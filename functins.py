#29/07/2024
#functions - independent block of code which only runs when it is called, code reusability
#29-july

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

'''def sample(name):      #variable/parameter/position argument
    print('hello',name)
sample("Tom")             #argument

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
    x=45    #local variable
    print(x)

    
sample()
print(x)'''

'''x='hello'            #global variable

def sample():
    print("value of x : ",x)
    
sample() 
print(x)'''

#to set a local variable as global variable
'''
def sample():
    global y
    y='Good morning'
sample()
print(y)
'''
#1,positional arguments
'''
a=int(input('enter your num1:'))
b=int(input('enter your num2:'))
def addition(num1,num2):
    total=num1+num2
    print(total)
addition(a,b)
'''
#2,keyword arguments
'''
def student(name,age,subjects):
    print('name of students:',name)
    print('age of students:',age)
    print('intersted subjects:',subjects)
student(subjects='english',name='john',age=23)
'''
#3,default parameters
'''
def multiply(a=10,b=2):
    print(a*b)
multiply(20,20)
multiply()
'''
'''
def mul(a,b=10): #first value kodthaa second default akkane pattum
    print(a*b)
mul(2)
'''
'''
def mul(a=10,b): #first default akkiya secnd value kodkaan avulaa
    print(a*b)
mul(2)
'''
#find the sum of numbers in list using fumction
'''
li=[2,3,4,5]
def addlist(a):
    x=0
    for i in a:
        x=i+x
    print(x)
addlist(li)    
'''

#30/07/24

#4,arbitary positional arguments(*args)
'''
def student_name(*name):
    print(name[0])
    print(name[1])


student_name('john','ran','tom')
'''

#5,arbitary keyword arguments(**kwargs)
'''
def employee_details(**data):
    print(data)
    print(data.get('name'))
    print(data['salary'])
    print(data.items())


employee_details(name='kevin',salary='100000',position='devops')
'''
#return
'''
def add(a,b):
    return a+b
print(add(2,3))

'''

#functions pass into another function
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

#modules(set of functions)

#1,math
'''
import math

print(math.pi)
print(math.sqrt)
'''

'''
from math import pi,sqrt
print(pi)

'''


'''
from math import *
print(pi)
print(sqrt(200))
'''

'''
x=abs(-7.25)
print(x)
'''

'''
import math

x = math.ceil(1.4)
y = math.floor(1.4)
z= math.factorial(13)
a=math.pow(5,2)
b=math.log(3)
print(x) 
print(y)
print(z)
print(a)
print(b)
'''

'''
x=pow(3,4.5)
print(x)
'''
#2,random
'''
import random

for i in range(5):
    print(random.randint(2,30))

'''

'''
from random import randint
for i in range(5):
    print(randint(2,30))
'''
'''
import random
x=random.random()
print(x)
'''

'''
import random
li=['abc',22,'sha']
y=random.choice(li)
z=random.choices(li)
print(y)
print(z)
'''
#3,date time
'''
import datetime

x = datetime.datetime.now()
print(x)
'''
'''
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
'''


'''
import datetime
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
'''

#31/07/24

#ANONYMOUS FUNCTION

#1,lambda function
#syntax
#lambda arguments:expression(it takes no.of arguments but execute single expression)
'''
a=lambda x:x+5
print(a(10))
'''

'''
b=lambda x,y:x+y+4
print(b(10,3))
'''
#odd or even using lambda
'''
num=lambda x:'even' if x%2==0 else 'odd'
b=int(input('enter the number'))
print(num(b))
'''

#greatest or smallest
'''
a=lambda x,y:x if x>y else y
b=int(input('enter the first number:'))
c=int(input('enter the second number:'))
print(a(b,c))

'''
#if input is 15 or grater,print 150.input 18,print 180.input 5 otpt 25,inp 4 otpt 20.inpt 6 opt 6
'''
num=lambda x:x*10 if x>=15 else(x*5 if x<=5 else x) 
a=int(input('enter the number:'))
print(num(a))
'''
#map(fun,iterable)
'''
def fun(x):
    return x*2
num=[1,2,3,4]
a=map(fun,num)
print(list(a))
'''
#qstn
'''
def fun(x):
    return 1/x
num=[4,8,3]
a=map(fun,num)
print(list(a))
'''
'''
a=map(lambda x:1/x,[4,8,3])
print(list(a))
'''

'''
b=lambda x:1/x
c=map(b,[3,6,8])
print(list(c))
'''

#filter(function,iterable)
'''
def even(z):
    if z%2==0:
        return True
    else:
        return False
num_list=[2,34,5,6,7,8,9]
data=filter(even,num_list)
print(list(data))
'''
























