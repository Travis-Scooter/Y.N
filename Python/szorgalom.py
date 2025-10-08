def getNum(msg : str = "Kérek egy számot: "):
    try:
        return int(input(msg))
    except:
        print("Ez nem egy szám, kérek újat...")
        return getNum(msg)

osztalyzat = getNum("A szorgalom osztályzata: ")

szorgalom : str

match osztalyzat:
    case 1:
        szorgalom = "rossz"
    case 2:
        szorgalom = "hanyag"
    case 3:
        szorgalom = "változó"
    case 4:
        szorgalom = "jó"
    case 5:
        szorgalom = "példás"
    case _:
        szorgalom = "ez nem egy osztályzat"

print(f"A szorgalom: {szorgalom}!")
