# w Pythonie ogólnie nie trzeba definiować funkcji main(), ale
# trzeba jeżeli poniżej będą zdefiniowane kolejne funkcje 
# wykorzystywane w kodzie. 
# W innym wypadku definicje pozostałych funkcji musiałyby 
# być na górze


def main():
    for i in range(3):
        meow()

def meow():
    print("meow")


# wcześniej main() był tylko zdefuniowany. Teraz trzeba go użyć:
main()


# taka składnia wywołania maina() byłaby potrzebna w wypadku 
# użycia własnych bibliotek:
# if ___name__ == "__main__":
#   main()