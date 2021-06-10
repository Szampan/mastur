# program zliczający z pliku csv ile osób należy do którego domu
# w csv są dwie kolumny: data i nazwa domu

import csv

houses = {
"Gryffindor": 0,
"Hufflepuff": 0,
"Ravenclaw": 0,
"Slytherin": 0
}

with open("Sorting Hat - Form Responses 1.csv", "r") as file:   # r- read
    reader = csv.reader(file) #allows to read automaticaly
    next(reader) #next() przeskakuje pierwszy wiersz (nagłówki)
    for row in reader:
        house = row[1] # row[1] - druga kolumna. Pierwsza byłaby row[0]
        houses[house] += 1

for house in houses:    # iteracja po wszystkich kluczach słownika houses
    print(f"{house}: {houses[house]}")