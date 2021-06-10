import sys

numbers = [4, 6, 8, 2, 7, 5, 0]

# linear search

if 0 in numbers:
    print("Found")
    sys.exit(0)         # not necessary
else:
    print("Not found")
    sys.exit(1)