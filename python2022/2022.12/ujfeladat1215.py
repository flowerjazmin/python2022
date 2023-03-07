import random

start=int(input("Kérek egy kezdő értéket: "))
veg=int(input("Kérek egy végző értéket: "))
mennyi=int(input("Kérem, hogy hány darabot emeljünk ki: "))

lista=[]

for i in range(mennyi):
    lista.append(random.randint(start, veg))

print(lista)


legnagyobb=max(lista)
egyseg=80//legnagyobb

for e in lista:
    print("*"*(e*egyseg))


#3 jegyű szám bekérés

szam=[]

while len(szam)!=3:
    szam=input("Kérek egy 3 jegyű számot: ")

szam=int(szam)

if szam%12==0:
    print("Osztható.")


print(szam)


szoveg="Lorem ipsum dolor sit amet, cock consectetur adipiscing elit. Nunc id gravida mauris, eu tempor dui. Ut convallis et leo et auctor. Integer lacinia porta sapien vel rutrum. Mauris lacinia a justo in sagittis. Proin orci justo, vehicula at accumsan vitae, accumsan a augue. Maecenas hendrerit ipsum eu malesuada scelerisque. Nullam tempor purus sed ante iaculis condimentum. Ut convallis nulla rhoncus metus aliquam sagittis. Sed faucibus, arcu nec vulputate pulvinar, purus neque molestie massa, vel maximus sapien dolor in lacus. Donec interdum, augue at faucibus convallis, nisl mi mollis lectus, in facilisis lacus lacus placerat libero. Ut mollis at turpis hendrerit efficitur. Phasellus vel mollis lacus. Maecenas luctus posuere sapien non aliquet. Pellentesque quis ultricies felis, quis molestie tellus. Fusce vel nunc ac dolor rutrum gravida."

betu="c"



print(len(szoveg.split(" ")))

szoveg2=szoveg.replace(betu, betu.upper())
print(szoveg2)















