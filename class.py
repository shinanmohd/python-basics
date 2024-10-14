'''
class Student:
    x=5
    b='Hello'
s1=Student()
s2=Student()
print(s1.x)
print(s1.b)
print(s2.b)

class Car:
    x='suv'
    y='sedan'
c1=Car()
print(c1.x)
print(c1.y)
'''

#07 - august
'''
class Sample():
    a=5
s1=Sample()
s2=Sample()
print(s1.a)
s1.a=25
print(s1.a)
print(s2.a)
'''

#self instance

'''class Sample:
    a=5                       #attribute
    def index(self):          #method
        print('Hello World')
s1=Sample()
print(s1.a)
s1.index()'''

'''class Sample:
    a=5                       #attribute
    def index(self):           #method
        a='hello'
        print('value of a : ',a)
s1=Sample()
print(s1.a)
s1.index()'''
'''
class Sample:
    a=5                       #attribute
    def index(self):           #method
        a='hello'
        print('value of a : ',self.a)
s1=Sample()
print(s1.a)
s1.index()
'''

#class
#create a class
'''
class Room:
    length=0.0
    breadth=0.0

    #method to calculate area
    def calculate_area(self):
        print("area of room=",self.length*self.breadth)

#create object of room class
study_room=Room()
bed_room=Room()
#assign values to all the properties
study_room.length=42.5
study_room.breadth=30.8
bed_room.length=20
bed_room.breadth=70
#access method inside class
study_room.calculate_area()
bed_room.calculate_area()
'''
'''
class Room:
    def fun(self,length,breadth):
        self.l=length
        self.b=breadth
r2=Room()
r1=Room()
r1.fun(40,20)
r2.fun(10,30)
print(r1.l)
print(r1.b)
print(r2.l)
print(r2.b)

'''
'''
class Room:
    def fun(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(f"area is {self.length*self.breadth}")
r1=Room()
r2=Room()
r1.fun(40,20)
r2.fun(10,30)
r1.area()
print(r1.length)
print(r1.breadth)
print(r2.length)
print(r2.breadth)
'''
#
'''
class person:
    work_place="IBM"    #class variable
    def __init__(self,name,age):
        self.name=name      #this is an instance variable
        self.age=age

    def display(self):
        print("Name of person",self.name)
        print("Age of person",self.age)
        print("Work place of a person",person.work_place)
p1=person('Ravi',21)
print(p1.name,p1.age,p1.work_place)

p1.name='suhail'
print(p1.name)
p1.display()

p2=person('kavya',12)
p2.display()
'''
'''
# class methods demo
class Student:
    # class variable
    school_name='ABC School'

    # constructor
    def __init__(self,name,age):
        # instance variables
        self.name=name
        self.age=age
    # instance method
    def show(self):
        # access instance variables and class variables
        print('Student:', self.name, self.age, Student.school_name)

    # instance method
    def change_age(self, new_age):
        # modify instance variable
        self.age = new_age

    #instance method
    @classmethod
    def modify_school_name(cls,new_name):
        #modify class variable
        cls.school_name=new_name

s1=Student('Harry',12)

#call instance methods
s1.show()
s1.change_age(14)

#call class method
Student.modify_school_name('XYZ School')
#call instance methods
s1.show()
'''

#09/07/24

#Inheritence

#syntax
'''
class Superclass:
    #attributes and methods
class Subclass(Superclass):
    #attributes and method
'''

'''
class Animal:
    def bark(self):
        print("Animal bark")
class Human(Animal):
    def speak(self):
        print("Speaking")
h=Human()
h.bark()
h.speak()
'''
'''
class Animal:
    #Attribute and method of the parent class
    name=''

    def eat(self):
        print("I can eat")

#inherit from Animal
class Dog(Animal):

    #new method in subclass
    def display(self):
        #access name attribute of superclass using self
        print("my name is",self.name)

#create an object of the subclass
labrador=Dog()

#access superclass attribute and method
labrador.name="Rohu"
labrador.eat()

#call subclass method
labrador.display()
'''
'''
class Vehicle:

    def __init__(self,name,year,color):
        self.name=name
        self.year=year
        self.color=color

    def display(self):
        print("Name of a vehicle is:",self.name)
        print("year launch vehicle is:",self.year)
        print("color of the car is:",self.color)

class Car(Vehicle):

    def __init__(self,name,year,color,brand):
        self.brand=brand
        #invoking parent class constructor
        Vehicle.__init__(self,name,year,color)

    def display(self):
            print("Name of a vehicle is:",self.name)
            print("year launch vehicle is:",self.year)
            print("color of the car is:",self.color)
            print("brand of a car is:",self.brand)

c=Car("polo","1946","Black","VW")
c.display() #method overriding
'''
#---------------------------------------------------------------
#operator overloading
'''
a=10
b=5
c=a+b #addition
a='a'
b='v'
c=a+b #concatenation
# same operator with different operation
'''
#method overloading(it only work for certain condition)
'''
def room(a,b):
    return a+b
def room(a,b,c):
    return a+b+c
'''
#----------------------------------------------------------------

# parent class
'''
class Person():
  def _init_(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

# child class
class Student(Person):
  def _init_(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super()._init_("Rahul", age)

  def displayInfo(self):
    print(self.sName, self.sAge)

obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()
'''

#multiple inheritance
#syntax
'''
class Parent1:
    #statement
class Parent2:
    #statement
class Child(Parent1,Parent2):
    #statement
'''
'''
class Calculation:
    def summation(self,a,b):
        return a+b

class Calculation2:
    def multiply(sefl,a,b):
        return a*b

class Derived(Calculation,Calculation2):
    def divide(self,a,b):
        return a/b

d=Derived()
print(d.summation(10,20))
print(d.multiply(10,20))
print(d.divide(10,20))
'''
























    









        



















