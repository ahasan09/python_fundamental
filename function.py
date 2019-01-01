def greet(first_name,last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")    

greet("Raju","Hasan")

def get_greeting(name):
    return f"Hi {name}"


message=get_greeting("Raju")
print(message)

def increment(number,by):
    return number+by

print(increment(3,by=2))