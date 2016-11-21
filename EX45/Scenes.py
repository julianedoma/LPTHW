class Scene(object):

    def enter(self):
        print "I'm a skeleton code for all locations in the game."
        exit(1)

class Game_Over(Scene):

    oops = [
        "Your mission as a detective failed."
        "Your boss won't be happy about that"
        "since he put so much hope in you!"
    ]

    def enter(self):
        print Game_Over.oops
        exit(1)

class University(Scene):

    def enter(self):
        print "A bunch of Serial Killers are casting a shadow over Lueneburg these days."
        print "Two People where shot in the street, 4 children disappeared"
        print "And two dead dogs where found."
        print "People in Lueneburg are scared to death avoiding going in the streets."
        print "You are hired to finally find the unscrupulous murders and the missing children."
        print "Be aware of a really dangerous place - Look out for sudden shots"
        print "and keep your head of suspicious people!"
        print "\n"
        print "You are starting off at the University Campus."
        print "While doing some research you are meeting a Student"
        print "Strange guy having a strange look at you."
        print "What are you doing?"
        print "1 ask him about the incidents"
        print "2 threaten him with a gun"

        action = raw_input("> ")

        if action == "1":
            print "The guy looks scared and tells you about a suspicious"
            print "person he knows who always hangs out in the City."
            print "Am Sand 5, to be exactly."
            print "sudden shoots appear and you hide at KonRad."
            print "The guy ran in a different direction."
            print "What are you doing now?"
            shooter_defeated = False

            while True:
                choice = raw_input("> ")
                if choice == "shoot around":
                    print "You are shooting around but no one is there."
                elif choice == "look around" and not shooter_defeated:
                    print "You suddenly see the shooter in front of you."
                    shooter_defeated = True
                elif choice == "shoot" and shooter_defeated:
                    print "You hit him right into his stomach."
                    print "He falls and dies."
                    print "Good Job! You are going to leave this crazy place asap"
                    print "and catch the next bus to Am Sande."
                    return 'am_sande'

                else:
                    print "This doesn't help!"
                    print "A guy appears right in front of you and shoots you"
                    return 'game_over'

        elif action == "2":
            print "Within the next moment, the guy pulls out his pepper spray"
            print "and suddenly your whole face burns like hell."
            print "You threatened an innocent person."
            print "Not very professional. Look out!"
            return 'university'

        else:
            print "Can't do that!"
            return 'university'

class Am_Sande(Scene):

    def enter(self):
        print "Am Sande is totally empty."
        print "You are going straight to house 5 and enter."
        print "There's an apartment door opened."
        print "What are you doing? Enter or Ring the bell"

        decision = raw_input("> ")

        if decision == "enter" or "Enter":
            print "Slowly you are walking into the hallway of a really"
            print "chaotic apartment."
            print "Suddenly you see a body laying on the floor."
            print "Shoot, the next one!"
            print "It's a dead man with a piece of paper in his hands."
            print "It says: Meet me at the Trainstation at 2 pm."
            print "Whoever it is, you have to find out - it is almost 2!"
            return 'trainstation'

        elif decision == "Ring the bell" or "ring the bell":
            print "The bell makes a loud sound."
            print "As you stand in front of the door, again,"
            print "a gun shot appears from upstairs "
            print "and hits you right in your chest."
            return 'game_over'

        else:
            print "You can't do this."
            return 'Am_Sande'

class Trainstation(Scene):

    def enter(self):
        print "After looking around you can see a tall man"
        print "standing around at the bus stop of the trainstation."
        print "After a while you are sure, that he is looking and "
        print "waiting for someone."
        print "You keep an eye on him for a while."
        print "Suddenly he takes his bike and starts leaving."
        print "What are you doing?"
        print "1 Run after him."
        print "2 Try to crack a bike lock."

        choice = raw_input("> ")
        if choice == "1":
            print "You start running after him. "
            print "Damn, he's so fast."
            print "He's turning into a big dark piece of forest. "
            print "Soon he notices you following him."
            print "He stops, asking what you want."
            print "As he noticed that you know too much of his situation"
            print "He knocks you down."
            return 'forest'

        if choice == "2":
            print "You pick a bike in a hidden place and try to "
            print "crack the numbers of the lock: "

            code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
            attempt = raw_input("> ")
            attempts = 0

            while attempt != code and attempts < 3:
                print "Wrong code, it's not working!"
                attempts += 1
                attempt = raw_input("> ")

            if attempt == code:
                print "Great, got it!"
                print "You take the bike and hurry up to get after him."
                print "He's turning into a big dark piece of forest. "
                print "Soon he notices you following him."
                print "He stops, asking what you want."
                print "As he noticed that you know too much of his situation"
                print "He knocks you down."
                return 'forest'
            else:
                print "Shoot, it takes too long."
                print "As you decide to run after him "
                print "instead of getting a bike, the suspicious is gone."
                print "You totally lost track of your only path."
                return 'game_over'

class Forest(Scene):

    def enter(self):
        print "You are waking up in a abondonded cottage in the middle "
        print "of the forest. You are locked in the basement of the cottage."
        print "There's a ladder downstairs and a small window."
        print "Where are you heading?"

        action = raw_input("> ")
        if action == "ladder downstairs" or "ladder" or "downstairs":
            print "You can see the guy standing there with a gun."
            print "He knows your intentions and is ready to shoot you."
            print "What are you doing?"
            print "1 Suggest a game"
            print "2 Try to hit him."

            reaction = raw_input("> ")

            if reaction == "1":
                print "He looks at you very sceptical but agrees."
                print "The guy is writing down a random number between 0 and 9."
                print "If you are guessing the number right, you'll be free"
                print "If not, you'll be one of the missing people "
                print "of Lueneburg."

                number = random.randint(0, 9)
                guess = int(raw_input("Your guess: "))
                if number != "guess":
                    print "You lost the game."
                    print "The guy is throwing you in the basement of the "
                    print "cottage, where you see all the missing children "
                    print "bounded up. No one will find you ever."
                    return 'game_over'
                if number == guess:
                    print "You can't believe it - you won!!"
                    print "The moment the guy realises what just happened"
                    print "He shoots hisself."
                    print "In the basement of the cottage you find all he child-"
                    print "ren who were missing in Lueneburg."
                    return 'won'
                else:
                    print "You lost the game, this was not the right number."
                    return 'game_over'

            if reaction == "2":
                print "The moment you try to knock him down, he shoots"
                print "you right in the chest."
                return 'game_over'

        elif action == "small window":
            print "You jump out of the windown, hoping to be able to leave."
            print "But it is higher than you thought in the beginning. "
            print "You hurt your foot so bad that you can't walk."
            print "The guy comes out of the cottage door and shoots you."
            print "You are dying."
            return 'game_over'

class Finished(Scene):

    def enter(self):
        print "You report the results of your investigation to your boss."
        print "He is so happy about how the situation turned out."
        print "Good job, you won the game!"
        return 'finished'
