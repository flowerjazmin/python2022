beSzam = 0

while beSzam<2 or beSzam>5:
    beSzam = int(input("Adj meg egy számot 2 és 5 között: "))

autok = []
for i in range(0,beSzam):
    autok.append(input("Kérem a(z) " +str(i+1) + ". autó márkát: "))

print(autok)



#Múltkori házi megoldásának áttekintése
szo="Almafa"

mgh=["ö","ü","ó","e","u","i","o","ő","ú","a","é","á","ű","í"]
if szo.lower()[0] in mgh:
    print("az")
else:
    print("a")
