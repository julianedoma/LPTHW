from sys import exit

def kitchen():
    print "You enter the kitchen."
    print "It is dirty and it smells really bad."
    print "What are you going to do? Leave or look around?"

    activity = raw_input("> ")

    if "leave" in activity:
        start2()
    elif "look around" in activity:
        kitchen_investigation()
    else:
        dead("The smell is so bad that you pass out.")

def kitchen_investigation():
    print "After a while you find a safe with a two digit code to open it."
    print "What are you going to do?"
    print "1. I'll give it a try!"
    print "2. I'll look around the castle for hints."

    code = raw_input("> ")

    if code == "1":
        print "Type in the two digit code:"
        final_code = raw_input("> ")
        two_digits = int(final_code)

        if two_digits == 36:
            print "The door of the save opens and you find a shiny diamant!"
            print "You won! Congrats!"
            exit(0)
        else:
            print "The code is wrong. Go and look for more hints!"
            start2()

    else:
        print "Look around the castle."
        start2()

def bath():
    print "You enter the bathroom."
    print "There's a secret door in the right corner."
    print "Are you entering or going back?"

    secret_door = raw_input("> ")

    if secret_door == "go back":
        start2()
    elif secret_door == "enter":
        dead("You are going through the door and fall in a deep, black hole!")

def stairs():
    print "There's a knive lying on the stairs."
    print "What are you going to do? Take (1) or leave (2) it?"

    knive = raw_input("> ")

    if knive == "1":
        print "Good decision. You might need it in this scary place."
        print "There's not more to see."
        box()
    elif knive == "2":
        print "Not taking this disgusting thing."
        first_floor()
    else:
        dead("You stumble and fall down the stairs and die.")

def box():
    print "As you go further, you enter an empty room."
    print "In one corner, you can see a small box."
    print "You get curious and approach the box in order to open it."
    print "All of a sudden, you can see a Wolf staring at you gnetching its teeth."
    print "What are you doing for your defense?"
    wolf_defeted = False

    defense = raw_input("> ")

    while True:
        if defense == "knive" and not wolf_defeted:
            print "After a long bloody fight, the wolf lying on the ground."
            print "You can grab the box and open it."
            print "In it you find a sheet with the digits 3 and 6 on it."
            print "What does this mean??!"
            start2()
            wolf_defeted = True
        else:
            dead("It doesn't help. The wolf got you!")

def first_floor():
    print "As you go further, you enter an empty room."
    print "In one corner, you can see a small box."
    print "You get curious and approach the box in order to open it."
    print "All of a sudden, you can see a Wolf staring at you gnetching its teeth."
    print "What are you doing for your defense?"

    strategy = raw_input("> ")

    if strategy == "run":
        start2()
    elif strategy == "knive":
        print "You'd better have taken it, stupid!"
    else:
        dead("It doesn't help. The wolf got you!")

#def first floor with while loop or for loop knive taken etc., + find digits!
def start():
    print "You are in the hallway of an abandoned castle."
    print "There's a door to your right and left and stairs to go in the first floor."
    print "Where are you going?"

    choice = raw_input("> ")

    if "right" in choice:
        kitchen()
    elif "left" in choice:
        bath()
    elif "upstairs" in choice:
        stairs()
    else:
        dead("You are so shocked by a scary noise so that you pass out.")

def start2():
    print "Back in the hallway downstairs. Where now?"
    print "right, left or upstairs?"

    choice = raw_input("> ")

    if "right" in choice:
        kitchen()
    elif "left" in choice:
        bath()
    elif "upstairs" in choice:
        stairs()
    else:
        dead("You are so shocked by a scary noise so that you pass out.")

def dead(why):
    print why, "You lost!"
    exit(0)

start()
