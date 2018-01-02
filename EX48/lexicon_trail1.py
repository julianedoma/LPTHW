directions = {"north", "south", "east", "west", "down", "up", "left", "right", "back"}
verbs = {"go", "stop", "kill", "eat"}
stop_words = {"the", "in", "of", "from", "at", "it"}
nouns = {"door", "bear", "princess", "cabinet"}
numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


class Lexicon(objects):
    self.startlexicon = startlexicon
    sentence = raw_input('>> ')
    words = sentence.split()

class words(stuff):
    self.words = words
    def scan(self, sentence):
        self.sentence = sentence
        self.words = sentence.split()
        stuff = []

class directions(words):
    for word in self.words:
        if word in directions:
            stuff.append(('direction', word))
    return stuff

class verbs(words):
    for word in self.words:
        if word in verbs:
            stuff.append(('verb', word))
    return stuff

class stop_words(words):
    for word in self.words:
        if word in stop_words:
            stuff.append(('stop verb', word))
        return stuff

class nouns(words):
    for word in self.words:
        if word in nouns:
            stuff.append(('noun', word))
        return stuff

class numbers(words):
    for word in self.words:
        if word in numbers:
            stuff.append(('number', word))
        return stuff

def startlexicon():
    print "Please enter any command for your character."
    userinput = raw_input(">> ")
    sentence == userinput

startlexicon.stuff()
