words = set()


def check(word):
    if word.lower() in words:   #lower() - metoda zmniejszająca litery
        return True
    else:
        return False

def load(dictionary):
    file = open(dictionary, "r ")
    for line in file:
        words.add(line.rstrip())    #.rstrip() - metoda usuwająca puste znaki (spacje, nowe linie, taby)
    file.close()
    return True

def size():
    return len(words)