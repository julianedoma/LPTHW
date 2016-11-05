print "You enter a dark room with two doors. Do you go through door #1, door #2 or #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
if door == "3":
    print "There's a mysterious box with a shiny surface. What do you do?"
    print "1. Open the box."
    print "2. Take the box and try to leave as quick as possible."

    box = raw_input("> ")

    if box == "1":
        print "You find a beautiful diamant. But what now?"
        print "1. Take it out of the box and take it."
        print "2. Leave it in the box and call your friend."
        print "3. I don't know what to do. I'll just stay here and wait for my mam resucing me."

        diamant = raw_input("> ")

        if diamant == "1":
            print "The box is exploding immediately and you die. Good job!"
        if diamant == "2":
            print "Your friend tells you to take the diamant. What's your decision?"
            print "1. Yeah, let's give it a shot."
            print "2. Noooo way, I'm too scared.I'll leave this place right now!"

            take_it = raw_input("> ")

            if take_it == "1":
                print "The box is exploding immediately and you die. Good job!"
            elif take_it == "2":
                print "On your way out you fall into a trap and die. Good job!"
            else:
                print "This is not a valid answer."

    elif box == "2":
        print "On your way out you fall into a trap and die. Good job!"

    else:
        print "This is the right decision. Level solved!"

else:
        print "You stumble around and fall on a knife and die. Good job!"
