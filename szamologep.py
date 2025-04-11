"""
Készítsünk egy egyszerű számológép programot! 
Kérjünk be két számot, illete egy műveleti jelet!
Csak összeadást, kivonást, szorzást és osztást.
Írjuk konzolra az eredményt a minta szerint!

Például:

Egyik szám? 10
Műveletjel? +
Másik szám? 20
10 + 20 = 30
"""

def getNum(msg : str = "Kérek egy számot: "):
    try:
        return int(input(msg))
    except:
        print("Ez nem egy szám, kérek újat...")
        return getNum(msg)

def getMuvelet():
    inp = input("Kérek egy műveletjelet: (+, -, *, /)")

    return inp

szam1 = getNum()
muvelet = getMuvelet()
szam2 = getNum("Kérek egy második számot: ")

eredmeny : float or int
if muvelet == "+":
    eredmeny = szam1 + szam2
elif muvelet == "-":
    eredmeny = szam1 - szam2
elif muvelet == "*":
    eredmeny = szam1 * szam2
elif muvelet == "/":
    eredmeny = szam1 / szam2

print(f"{szam1} {muvelet} {szam2} = {eredmeny}")
