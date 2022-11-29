
#1. feladat: 10 szám bekérése

szamok=[]
for i in range(10):
    szamok.append(int(input(str(i+1)+". szám: ")))

#2. feladat: kiírás

for i in szamok:
    print(str(i), end="")
print()

#print("".join(szamok))
#3. feladat: kiírás 2 oszlopba

for i in range(10):
    print(str(szamok[i])+"\t", end="")
    if i%3==2:
        print()

#4. feladat: bekért számok átlaga
atlag=sum(szamok)/len(szamok)
print()
print(atlag)

osszeg=0

for i in szamok:
    osszeg+=i
atlag=osszeg/len(szamok)
print(atlag)

#5. feladat: szöbeg tárolás
szoveg= "dfjkl hadjk fhadjkhéa dfjghfékghfd jkghdf th dasbd sdasdf dsfdsf dsaf"

#6. betübekérés
betu="qwe"
while betu!="":
    betu=input("Kérek egy betűt: ")
    szoveg=szoveg.replace(betu,betu.upper())
    print(szoveg)

#7. ismétlés

#8. szavankénti megfordítás
lista=szoveg.split(" ")
lista.reverse()
szoveg2=" ".join(lista)
print(szoveg2)



