import math

print("Hello World")
print("*" * 10)
# PyLint
# print "Hello World"
# 2+
# PEPs
x = 2
print(x)
# Valiables
student_count = 1000
rating = 4.99
is_published = False
is_accessed = True
course_name = "Python Programming"
# string
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:4])
print(course[0:])
print(course[:4])
print(course[:])
print(course[0:-1])
# Escape Sequence
# \"
# \'
# \\
# \n
course = "Python \"Programming"
print(course)
course = "Python \'Programming"
print(course)
course = "Python \\Programming"
print(course)
course = "Python \nProgramming"
print(course)
# Formatted String
first = "Raju"
last = "Hasan"
full = first+" "+last
print(full)
full = f"{first} {last}"
print(full)
# String Method
course = " Python Programming "
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.rstrip())
print(course.lstrip())
print(course.find("Prog"))
print(course.replace("P", "J"))
print("Pro" in course)
print("Swift" not in course)
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
# Type Conversion
x = input("x: ")
print(type(x))
y = int(x)+1
print(f"x: {x}, y: {y}")
# y=x+1
# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy
# ""
# 0
# "None"
# Comparison Operators
10 > 3
10 >= 3
10 < 20
10 <= 20
10 == 10
10 == "10"
10 != "10"
"bag" > "BAG"
"bag" == "BAG"
ord("b")
ord("B")
# Conditional Statements
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")
# Ternary Operator
