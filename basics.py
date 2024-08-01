#escape sequence =\n,\t
"""print("hello") 
print(1+2)
print("beat"+"box")
print("\thello")
print('1')
print('a+\nb')

#print("world"+12) edhellum ore line error ayaa thayek illadh execute cheyulla

print("world"*12)
#print("world"+12) str + * only work avullu

print(2+5)
print('2'+'8')"""

#arithmetic operation
"""#1 addition
print(1+2)
#2 substraction
print(1-2)
#3 multiplication
print(1*2)
#4 division
print(2/2)
#5 floor division (convert integer value)
print(6//4)
#6 modulo (get remonder value)
print(4%2)
#7 exponential
print(4**2)#4^2
#8 root
print(4**(1/2)) #root4"""

#boolean operator(<,>,<=,>=,!=,==)
"""print(8>4)
print(8<4)
print(8!=4)
print(8!=8)
print(8==8)
print("hello"=="hello")"""#comparison operator it compares the char in index value of both string

#variables(used for temp storage, we can reassign value)
"""a=10
print(id(a))
a=5""" #new m/y create avum inside that 5 store avum old m/y a=10 inactive garbage value avum
"""print(id(a))
print(a*5)
print(a+5)
b=6
c=8
d=b+c
print('result is',d)
e=b%c
print('result is',e)
print(b**c)    #b^c(6^8)
print(b**(1/2))  #root of b"""

#type function (used to identify the datatype of a value stored in variable)

"""z=30
print(type(z))
c="hello"
print(type(c))"""

#type conversion (convert one data type into another)

"""print(int('2')+int('4'))
print(int(5.6)+int(3.4))
print(float(5)+float(2))"""

#input function

"""a=int(input("enter your 1st no"))
b=int(input("enter your 2st no"))
c=a+b
d=a*b
e=a-b
f=a/b
g=a//b
h=a%b
j=a**(1/2)
print('result for a+b is',c)
print('result for a*b is',d)
print('result for a-b is',e)
print('result for a/b is',f)
print('result for a//b is',g)
print('result for a%b is',h)
print('result for a**(1/2)',j)"""
#swapping
'''x=int(input("enter your 1st no"))
y=int(input("enter your 2st no"))
print('Before swapping')
print('value of x',x)
print('value of y',y)
print('----------------------------')
temp=x
x=y
y=temp
print('value of x',x)
print('value of y',y)'''
# without using third variable
'''x=int(input("enter your 1st no"))
y=int(input("enter your 2st no"))
print('Before swapping')
print('value of x',x)
print('value of y',y)
print('----------------------------')
x,y=y,x
print('After swapping')
print('value of x',x)
print('value of y',y)'''
#condition statement
'''
1, if
2, ladder if
3, if else
4, ladder if else
5, elif'''
#syntax
#1, if
'''if condition:
      statement
      '''
# example
'''if 10>2:
    print('10 is greater than 2')
print('program is finished')
if 10+1==9+2:
    print('they are equal')'''
#2, ladder if
'''if condition:
        statement
        if condition
            statement
'''
# example
'''if 2<5:
    print('5 is greater than 2')
    if 4==2:
        print('4 is equal to 2')
        if 10>3:
            print('10 is greater than 3')
print('program is finished ')'''
#3 if else
'''x=int(input("enter your 1st no"))
y=int(input("enter your 2st no"))
if x==y:
    print('square')
else:
    print('rectangle')'''
'''a=int(input("enter your 1st no"))
if a%2==0:
    print('number is even')
else:
    print('number is odd') '''
#4 if else ladder
'''
if condition:
    statement
else:
    if condition:
        statement
    else
        statement'''
#example:
'''num=int(input("enter a no:"))
if num>13:
    print('hello')
else:
    if num<2:
        print('welcome')
    else:
        if num==10:
            print('hi')
        else:
            print('python')'''
#elif
'''color=input("enter a color:")
if color=="red":
    print("color is red")
elif color=="green":
    print("color is green")
elif color=="blue":
    print('color is blue')
else:
    print("it is not RGB color code")'''
#inplace operator
'''a=10
a+=5
print(a)#15
b=15
b-=5
print(b)#10
c=100
c/=5
print(c)#20
d=4
d*=10
print(d)#40
e=5
e**=2
print(e)#25
f=100
f//=3
print(f)#33
g=11
g%=5
print(f)#1'''

#logical operator
'''# and or not
print(5>3 and 5==5)#true
# and operator returns true if both of ots operands are true
print(10>5 or 10!=10)#true
# or operator returns true if atleast one of its operands is true
print(not 5==5)#false
# not operator returns the opposite boolean value of its operand'''

#identity operator
'''a=10
b=5
c=10
print(a is not b)
print(a is c)'''
# it will check the address of the both variable and give true if the address is same and false if address is not same


#string formating
'''name=input("enter your name")
age=int(input("Enter your age"))
print("My name is{} and i'm{} years old".format(name,age))
print("My name is{} and i'm{} years old".format(age,name))#this is problem of string formating

#f-string
print(f"My name is{name} and i'm{age} years old")'''

# in operator
'''x=input('Enter a character:')
vowel="aeiouAEIOU"
if x in vowel:
    print('is vowel')
else:
    print('not a vowel')'''

'''x=int(input('enter the number'))
y=int(input('enter the number'))
z=int(input('enter the number'))
if x>y and x>z:
    print(f"{x}is greater")
elif y>x and y>z:
    print(f"{y}is greater")
else:
    print(f"{z}is greater")'''

#loop
#1 while
#syntax

'''
intialisation
while condition (limit):
    statement
    increment'''
#example   
'''i=1
while i<=10:
    print('Hello')
    i+=1
print('finished')'''

'''i=1
while i<=10:
    if i%2==0:
        print(i)
    i+=1'''

#18/07/2024

#break
'''while 1==1:
    print("Hello")
    break
------------------------------
i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+=1'''

#continue
'''i=0
while i<9:
    i+=1
    if i==3:
        continue
    print(i)
-------------------------------
i=0
while i<=10:
    i+=1
    if i==2:
        print("skipping 2")
        continue
    if i==5:
        print("Hello")
        break
    print(i)

--------------------------------
i=10
while i>0:
    if i==5:
        i-+1
        break
    print(i)
    i-=1
print('Thank you')'''

    
