num1=input("Enter a number: ")
num2=input("Enter another number: ")
result=float(num1)+float(num2)
print(result)

friends=[1,2,3,5,4,6]
friends.append(8)
friends.insert(2,4)
friends.reverse()
friends.remove(4)
print(friends)
friends.pop()
print(friends)
print(friends.count(4))
friends.clear()
print(friends)

months={
    "Jan":"January",
    "Feb":"February"
}

print(months['Jan'])
print(months.get('Jan','Not valid key'))