import random
#w budowie:

sounds = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]
bassStrings = ["e", "a", "d", "g"]

def bassString(name, fret): # return a name of the sound assigned to a fret on the particular string
    if fret > 24:
        print("There are 24 frets!")
    else:
        if name == "e":
            if fret > 4:
                fret -= 12
            sound = sounds[fret + 7]
            return sound
        elif name == "a":
            sound = sounds[fret]
            return sound        
        elif name == "d":
            if fret > 6:
                fret -= 12
            sound = sounds[fret + 5]
            return sound
        elif name == "g":
            if fret > 1:
                fret -= 12
            sound = sounds[fret + 10]
            return sound
        else:
            return 0


def randomStringAndSound():
    x = random.choice(bassStrings)
    y = random.choice(sounds)
    return x, y

#stringAndSound = "e", "a"

#print(stringAndSound)

print(bassString("e", 5))