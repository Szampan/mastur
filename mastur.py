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

import random

sounds = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]
bassStrings = ["e", "a", "d", "g"]

print(sounds)

def strE(fret):
    if fret > 4:
        fret -= 12
    sound = sounds[fret + 7]
    return sound

#w budowie:
#def bassString(name, fret):

#zrobić jeszcze losowanie strun

#


def randomSound():
    #return sounds[random.randint(0, 11)]
    return random.choice(sounds)

question = randomSound()
answer = int(input(f"On which fret of the E string you can find sound {question}? "))

def isRight(x):
    if strE(x) == question:
        return "ok!"
    else:
        return "wrong"


print(isRight(answer))


#teraz warunek testujący czy odpowiedź jest dobra (funkcja?)


#input_fret = int(input("Which fret on the E string?"))

#print(f"{input_fret} fret on the E string is {strE(input_fret)}")