# sys.argv() odczytuje argumenty z linii komend w formie 
# listy. Pierwszy argument to nazwa programu.


from sys import argv

if len(argv) != 1:
    print(f"Hello, {argv[1]}")
else:
    print("hello, world")