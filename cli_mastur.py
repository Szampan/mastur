import random

sounds = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]

# print(sounds)

def note_name(name, fret): # return a name of the sound assigned to a fret on the particular string
    if fret > 24:
        print("There are 24 frets!")
    else:
        #### WYWALA SIĘ NA WYŻSZYCH PROGACH
        if name == "e":
            while fret > 4:
                fret -= 12
            sound = sounds[fret + 7]
            return sound
        elif name == "a":
            while fret > 11:
                fret -= 12
            sound = sounds[fret]
            return sound        
        elif name == "d":
            while fret > 6:
                fret -= 12
            sound = sounds[fret + 5]
            return sound
        elif name == "g":
            while fret > 1:
                fret -= 12
            sound = sounds[fret + 10]
            return sound
        else:
            return 0

def random_sound():
    return random.choice(sounds)

question = random_sound()
answerStr = input(f"Where is sound {question}? Type the name of the string: ")
answerFret = int(input(f"Now type the fret number: "))

def is_right(x, y):
    if note_name(x, y) == question:
        return "ok!"
    else:
        return "wrong"

print(is_right(answerStr, answerFret))
