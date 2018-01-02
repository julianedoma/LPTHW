lexicon = {
    ('directions', 'north'),
    ('directions', 'south'),
    ('directions', 'east'),
    ('directions', 'west'),
    ('directions', 'down'),
    ('directions', 'up'),
    ('directions', 'left'),
    ('directions', 'right'),
    ('directions', 'back'),
    ('verbs', 'go'),
    ('verbs', 'stop'),
    ('verbs', 'stop'),
    ('verbs', 'kill'),
    ('verbs', 'eat'),
    ('stops', 'the'),
    ('stops', 'in'),
    ('stops', 'of'),
    ('stops', 'from')
    ('stops', 'at')
    ('stops', 'it'),
    ('nouns', 'door'),
    ('nouns', 'bear'),
    ('nouns', 'princess'),
    ('nouns', 'cabinet'),
    ('numbers', '0'),
    ('numbers', '1'),
    ('numbers', '2'),
    ('numbers', '3'),
    ('numbers', '4'),
    ('numbers', '5'),
    ('numbers', '6'),
    ('numbers', '7'),
    ('numbers', '8'),
    ('numbers', '9'),
    }

def scan(sentence):

    words = sentence.lower().split()
    pairs = []

    for word in words:
        word_type = lexicon[word]
        tupes = (word, word_type)
        pairs.append(tupes)

    return pairs
