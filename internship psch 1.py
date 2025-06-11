#Program to add two numbers 
x = 10
y = 15
z = x + y
print(z)

#program to subtract two numbers 
a = 45
b = 15
c = a - b
print(c)

#program to multiply two numbers
q = 8
r = 10
s = q * r
print(s)

#program to perform some arithmetic operation
m = 15
n = 20
o = 5
p = (m * n) / o 
print(p) 

#testing for left shift operator
g = 5
h = g << 1
print (h)

#now on modules
import sys
print(sys.version)
print(sys.version_info)

#Calendar
import calendar
print(calendar.month(2025,6))

import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)  

#random number
import random
a=random.randint(1,7)
print(a)

import random
b=random.randrange(1,3)
print(b)

import random
c=random.random()
print(c)

import random
d=random.uniform(1,3)
print(d)

import random
e=[2,3,5,-50,30,-10]
f=random.choice(e)
print(f)

import random
j=[50,19,17,-5,-30]
random.shuffle(j)
print(j)

# Pyramid Pattern using stars
rows = 5

for i in range(1, rows + 1):
    # Print spaces
    print(" " * (rows - i), end="")
    
    # Print stars
    print("*" * (2 * i - 1))







