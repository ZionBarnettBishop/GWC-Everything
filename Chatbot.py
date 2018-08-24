poem=("Roses are red, violets are blue, I am really cute, but you look like poo;)")
no=("idc", poem)
answer = input("Hello!")
player = 1
WW = 1
power = "Yes" or "No"
choice = "Yes" or "No"


op=input("How are you?")

if not op.isnumeric():
    print("Interesting!")
elif op.isnumeric():
    print("Wow")
    
response=input("What school do you go to?")
print("I've heard of", response)

option=input("Would you like to hear a poem?")
print("Idc!", poem)

age=input("How old am I?")
if not age.isnumeric():
    print("Correct!")
elif age.isnumeric():
    print("Nope...HAHAH!")

tanswer=input("Let's play a game!")
if player == 1:
    name = input("Im going on a new mission and I need back-up!!What is your name?")
    if name.isnumeric ():
            print("That's not a name. Type your name.")
    else:
        print("Hi," ,name)
        
age =input("How old are you?")
if not age.isnumeric():
        print("That's not your age. Type your age.")
        age = int(age)
else:
    print(age, "years old!")
place =input("Where are you from?")
if place.isnumeric():
    print("That's not a place! What city or state are you from?")
else:
    print("I've been to", place)

power = input("Do you have any superpowers! Yes or No")
if power.isnumeric():
    print("Answer Yes or No!")
if power == "No":
    print("Sorry, I couldn't use you during the trip")
if power == "Yes":
    answer =input("What is it?")
    print(answer, "could really help me during my mission!")
if answer.isnumeric():
    print("That's not a super power!Bye")
    exit()
else:
     power= input(answer, "could be very useful during my mission!Would you like to come? Yes or No?")
if power == "Yes":
    print("Let's go!")
    exit()
if power == "No":
    print("Oh well")

    print("My favorite is.... ")
def myname():
    name= "Z.I.O.N"
    print(name)
myname()
print("Bye!")

    
    
