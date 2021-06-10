import cs50

# przed get_int() biblioteka źródłowa cs50.  jeśli 
# nie zaimportowałem konkrentej funkcji, tylko 
# całą bibliotekę.
# NAMESPACING - bo mogą być dwie funkcje o takich 
# samych nazwach z różnych bibliotek:

x = cs50.get_int("x: ")     
y = cs50.get_int("y: ")

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
