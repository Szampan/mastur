i = 1
while True:
    print(i)
    i *= 2      # będzie liczyć w nieskończoność,
                # w przeciwieństwie do C, gdzie 
                # int ma ograniczoną wielkość
                # ALE floating pointy nadal będą 
                # nieprecyzyjne (bez odpowiednich bibliotek)