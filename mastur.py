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



sounds = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]

print(sounds)

def strE(fret):
    sound = sounds[fret + 7]
    return sound

print(f"1 próg na strunie E to {strE(1)}")