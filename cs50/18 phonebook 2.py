import csv

from cs50 import get_string

file = open("18 phonebook.csv", "a") # a - append mode

name = get_string("Name: ")
number = get_string("Number: ")

writer = csv.writer(file) # włączenie funkcjonalności csv dla pliku

writer.writerow([name, number]) # writerow( ) - dodaje wiersz

file.close()


# można też tak:
# with open("18 phonebook.csv", "a") as file
#
#    number = get_string("Number: ")
#
#    writer = csv.writer(file) # włączenie funkcjonalności csv dla pliku
#
#    writer.writerow([name, number]) # writerow() - dodaje wiersz
#
# file.close() # - ta linijka chyba niepotrzebna