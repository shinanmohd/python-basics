#01/08/2024

#list comprehensions
#syntax
'''
new_list[expression fro itam in item in iterable if condition ==True]
'''
'''
fruits=['apple','banana','kiwi','mango','berry']
new_list=[]
for i in fruits:
    if 'a' in i:
        new_list.append(i)
print(new_list)
'''


'''
new_list=[i for i in fruits if 'a' in i]
print(new_list)
'''

'''
new_list=[i for i in fruits if 'banana' not in i]
print(new_list)
'''
'''
numbers=[4,2,8,5]
squares=[i**3 fr i in numbers]
print(squares)
'''
'''
data ='codeme'
vowel="aeiouAEIOU"
new_list=[i for i in data if i in vowel]
print(new_list)
'''
#1-10 even numbers
'''
d=[i for i in range(1,11) if i%2==0]
print(d)
'''
'''
f=[i for i in range(10,51,10)]
print(f)
'''
#slicing
#list slicing
'''
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(a[:])
print(a[3:])
print(a[:7])
print(a[4:10])
print(a[3:12:2])
print(a[::2])
print(a[3::2])
print(a[:14:3])
'''
#Reverse slicing
'''
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
print(a[::-1])
print(a[-2:])
print(a[:-3])
print(a[-5:-2])
print(a[3:1:-1])
print(a[2:-2])
print(a[5:2:-1])
print(a[-1:-4:-1])
print(a[-4:-1:2])
print(a[-2:-5:-1])
print(a[-1:-6:-1])
print(a[-6:-2:-1])#result is empty list bcz starting cherudhum ending velludhum
print(a[-2:-6:-1])
print(a[4:2])#result is empty list bcz starting velludhum ending cherudhum
'''
'''
s='hi i am a DataAnalyst'
print(s[:])
print(s[3:])
print(s[-3:])
print(s[-5:-2])
print(s[5:2:-1])
print(s[-2:-5:-1])
print(s[-1:-6:-1])
print(s[-1:-6])
print(s[::-1])
'''











































