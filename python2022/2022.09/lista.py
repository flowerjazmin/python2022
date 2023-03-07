lista= ["alma", "cseresznye", "lime", 42]
print(lista)
print(lista[1])

print(len(lista))

print(lista[len(lista)-1])

print(type(lista[len(lista)-2]))

lista[2]="cukornád"
print(lista)

lista.append("nyomorák")
print(lista)

lista.insert(1, "miagyász")
print(lista)
