import math

# Numbers
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10 % 3)
print(10**3)
x = 10
print(x)
x = x+3
print(x)
x += 3
print(x)
# Working with Numbers
print(abs(-2.9))
print(round(2.9))
print(math.ceil(2.2))
print()

from math import *
try:
    10/0
    number=int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")    
except:
    print("Invalid input")    
