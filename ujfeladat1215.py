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






