#számbekérő modul
#Többféle paraméterezéssel
#2022.11.18 Darusi Jázmin


def szamBe(szoveg,tort=False,minimum=False,maximum=False):
#    print(szoveg)
#    print(tort)
#    print(minimum)
    hiba=True
    while hiba:
        try:
            if tort:
                szam=float(input(szoveg))
            else:
                szam=int(input(szoveg))
        except:
            print("HIBA!!")
        else:
            hiba=False


szamBe("Adjál meg számot: ", minimum=10, tort=True)
    
