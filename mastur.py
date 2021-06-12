# 1. Gryf: 
#    odległości między progami jako ułamek całości
#    Najlepiej jako funkcja rekurencyjna
#
# 2. quiz do zgadywania w którym miejscu jest dźwięk 
#    Np. pytanie: Gdzie jest E? Odp.: E0, A7, E12, D3
#
# 3. Ficzery:
#   Punktacja za dobre odpowiedzi
#   Im wyższe progi tym więcej punktów
#   Im szybciej, tym więcej punktów
#
# 1. apka losuje dzwiek i pyta usera gdzie jest ten dzwiek
# 2. user podaje nazwe struny i numer progu
# 3. apka sprawdza czy nazwa struny i numer progu odpowiadają nazwie dźwięku
#
#

import random

sounds = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]

print(sounds)

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


def randomSound():
    return random.choice(sounds)

question = randomSound()
answerStr = input(f"Where is sound {question}? Type the name of the string: ")
answerFret = int(input(f"Now type the fret number: "))

def isRight(x, y):
    if bassString(x, y) == question:
        return "ok!"
    else:
        return "wrong"

print(isRight(answerStr, answerFret))