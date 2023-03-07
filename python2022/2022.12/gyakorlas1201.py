def oszlopba(munkalista, db):
    for i in range(len(munkalista)):
        print(munkalista[i], end=" ")
        if i%db==db-1:
            print()
    print()

szamok = []
for i in range(0):
    szamok.append(int(input("Kérek egy számot: ")))

szamok = [1,2,3,4,5,6,7,8,9,10]
print(szamok)

for i in range(len(szamok)):
    print(szamok[i], end=" ")
    if i%3==2:
        print()
print()


szamBe = int(input("Kérek egy keresendő számot: "))
if szamBe in szamok:
    print("Van benne.")
else:
    print("Nincs benne.")

oszlopba(szamok, 5)
