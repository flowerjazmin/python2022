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
