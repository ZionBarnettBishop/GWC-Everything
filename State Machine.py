jsonData = {'Name':[], 'Age':[], 'Place':[], 'X':[]}
Pyjson = json.loads(jsonData)
while True:
    x= "Yes" or "No"
    player= 1
   
                                                        

    if player == 1:
        name = input("What is your name?")
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

    x = input("Do you like Computer Science, Yes or No?")
    if x.isnumeric():
        print("Answer Yes or No!")

    if x == "No":
        print("Why you here girl!!")

    elif x == "Yes":
        print("That's Cool!")
    else:
        if x.isnumeric():
            print("What?")

    dict['Name'].append(name)
    dict['Age'].append(age)
    dict['Place'].append(place)
    dict['X'].append(x)

    print(dict)





