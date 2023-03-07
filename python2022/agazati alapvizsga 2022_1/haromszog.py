def haromszog():
    
    vissza=[]
    for i in range(3):
        szam=""
        while szam=="":
            try:
                szam=int(input("Kérek egy egész számot: "))
            except:
                print("Ez nem egész szám!")
        vissza.append(szam)

    return vissza
