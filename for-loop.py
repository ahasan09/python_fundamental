for number in range(3):
    print(f"Attempt {number}") 

for number in range(3):
    print("Attempt",number+1,(number+1)*".")

for number in range(1,4):
    print("Attempt",number,number*".")

for number in range(1,10,2):
    print("Attempt",number,number*".")


#For..Else
successful=True
for number in range(3):
    print("Attempt")
    if not successful:
        print("Successfull")
        break
else:
    print("Attempted 3 times and failed")    

#Nested For Loop
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

print(type(5))
print(type(range(5)))
print(type([1,2]))
#Complex Type [range list]
#Iterable
for x in range(5):
    print(x)

for x in "Python":
    print(x)

for x in [1,2,3,4,5]:
    print(x)

count=0
for x in range(1,10):
    if x%2==0:
        print(x)
        count+=1
print(f"We have {count} even numbers") 
      