# Python wyszukując w słowniku używa metody hash table 
# (zamiast linear)

from cs50 import get_string

people = {
    "Brian": "111-111-111",
    "David": "222-222-222"
}

# numer briana

print("Brian's number: " + people["Brian"])

for i in people:
    print(i)


# numer wg wpisanego imienia

name = get_string("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")