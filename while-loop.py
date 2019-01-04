number=100
while number>0:
    print(number)
    number//=2

command=""
while command.lower()!="quit":
    command=input(">")
    print("ECHO",command)    

#Infinite Loop

guess=""
secret_word="Raju"
guess_count=0
guess_limit=3
out_of_guesses=False

while guess!=secret_word and not out_of_guesses:
    if guess_count<guess_limit:
        guess=input("Enter guess: ")
        guess_count+=1
    else:
        out_of_guesses=True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("YOU WIN!")    