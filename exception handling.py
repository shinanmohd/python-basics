#02/08/24

#Exception Handling
'''
try:
    print("Hello")
    print(5/0)
    print('Hi')
except ZeroDivisionError:
    print('Error handling')
finally:
    print('hi')


a='Hello'
b=2
try:
    print(a+b)
except TypeError:
    print('Error handling')
finally:
    print('python')

a=['hello','red','kiwi']
try:
    print(a[1])
    print(a[3])
except IndexError:
    print('error no index')
finally:
    print(a[0])
'''
'''
def fun(a):
    if a<4:
        b=a/(a-3)
        print('Value of b:',b)
    else:
        print('5 is greater')
try:
    fun(3)
except ZeroDivisionError:
    print('Error handling')
finally:
    fun(2)
    fun(5)
'''
'''
print("hello")
raise TypeError('error detected')
print('hi')
'''
'''
try:
    print(5/0)
except Exception as e:
    print('error')
    raise TypeError('cannot divide with 0')
'''
def divide(a,b):
    if b==0:
        raise Exception("cannot divide by zeo")
    returna/b
try:
    result=divide(10,0)
except Exception as e:
    print("errror occures",e)
print(20,5)



