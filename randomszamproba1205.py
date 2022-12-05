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
