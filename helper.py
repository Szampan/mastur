#w budowie:

sounds = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]

def bassString(name, fret):
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


print(bassString("e", 0))