animals=("bence","martin","giraffe","kelgyó","kágyilló")

print(animals[1])
print(animals[-1])

print(animals[:4])
print(animals[1:4])
print(animals[1:-1])

print(animals[:4:2])

animals=list(animals)
animals[1]="milán"
animals=tuple(animals)

print(animals[1])

ureg=[]

for i in range(4,-1,-1):
    print(i)
    ureg.append(animals[i])

print(ureg)
