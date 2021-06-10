from cs50 import get_string

s = get_string("Do tou agree? ")

if s == "Y" or s == "y":
    print("Agreed")
elif s.lower() in ["n", "no"]:     #lista z możliwymi odpowiedziami
    print("Not agreed")