#b = ["IV", "III", "II", "XX", "II", "XX"]
#a = ["II", "IV", "II", "XIX", "XV", "IV", "II"]


def love_meet(bob, alice):

    dates = set()
    for i in alice:        
        for j in bob:                        
            if i == j:                
                if not j in dates:
                    dates.add(j)               
    print(dates)
    return dates
    
 

def affair_meet(bob, alice, silvester):
#    ...
#

if __name__ == "__main__":
    assert love_meet(
        ["IV", "III", "II", "XX", "II", "XX"],
        ["II", "IV", "II", "XIX", "XV", "IV", "II"],
    ) == {"II", "IV"}

    assert affair_meet(
        ["IV", "III", "II", "XX", "II", "XX"],
        ["II", "IV", "II", "XIX", "XV", "IV", "II"],
        ["XVIII", "XIX", "III", "I", "III", "XVIII"],
    ) == {"XIX"}