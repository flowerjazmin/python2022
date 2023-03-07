import random
import math


lista=[]
for i in range(10):
    szam= random.random()
    lista.append(math.floor(szam*90)+10)

print(lista)

lista=[]
for i in range(10):
    lista.append(random.randint(10,99))

print(lista)


print(random.randint(-1000,1000)*3)
lista=[]
for i in range(100):
    lista.append(random.randint(-1000,1000)*3)

print(lista)

print(sum(lista))
tutel=[]
for e in lista:
    if e%5==0:
        tutel.append(e)

print(tutel)

tutel=[e//15 for e in lista if e%5==0]

print(tutel)


#hf pótlás

print(random.randrange(167,1667,2)*6)

#randinttel

print((random.randint(83,832)*2+1) * 6)




szavak=["alma", "körte", "barack", "banán", "dinnye", "szőlő"]

#random.seed(1)
print(szavak[random.randint(0,len(szavak)-1)])

print(random.choice(szavak))


#[["alma",14],["körte",18],[].....]
print("-"*20)

nagyLista=[]

for e in szavak:
    #print(e)
    kisLista=[]
    kisLista.append(e)
    kisLista.append(random.randint(12,312))
    #print(kisLista)
    nagyLista.append(kisLista)

print(nagyLista)


for e in nagyLista:
    print(e[0].ljust(10), str(e[1]).rjust(4), "kg", "."*(e[1]//6))




















