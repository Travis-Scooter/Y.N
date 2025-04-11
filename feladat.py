ponthatarok = [ 90, 76, 61, 51, 0 ]

def getNum(msg : str = "Kérek egy számot: "):
    try:
        return int(input(msg))
    except:
        print("Ez nem egy szám, kérek újat...")
        return getNum(msg)

pontszam = getNum("A dolgozat pontszáma: ")

osztalyzat : str

if pontszam >= ponthatarok[0]:
    osztalyzat = "jeles"
elif pontszam < ponthatarok[0] and pontszam >= ponthatarok[1]:
    osztalyzat = "jó"
elif pontszam < ponthatarok[1] and pontszam >= ponthatarok[2]:
    osztalyzat = "közepes"
elif pontszam < ponthatarok[2] and pontszam >= ponthatarok[3]:
    osztalyzat = "elégséges"
elif pontszam < ponthatarok[3] and pontszam >= ponthatarok[4]:
    osztalyzat = "elégtelen"
else:
    osztalyzat = "elégtelen"

print("A te osztályzatod: " + osztalyzat + "!")
