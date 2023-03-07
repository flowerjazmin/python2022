#1.)
fruits=["alma","szőlő","körte","barac","dragonfruit","licsi"]

print("Ennyi gyümölcs van: {}".format(len(fruits)))

print(fruits[3])

#fruits[3]+="k"
#fruits[3]="barack"

print(fruits.index("barac"))

#fruits[fruits.index("barac")]+="k"

index=fruits.index("barac")
fruits[index]+="k"

print(fruits[3])



#2.)
print("Rövid gyümölcsök.")
#for i in range(len(fruits)):
    #if len(fruits[i])<5:
        #print(fruits[i])

rovid=[]

for i in range(len(fruits)):
    if len(fruits[i])<5:
        rovid.append(fruits[i])

print(rovid)

rovid=[]

for e in fruits:
    if len(e)<5:
        rovid.append(e)

print(rovid)

rovid=[e for e in fruits if len(e)<5]
print(rovid)

rovid=[]

i=0

while i<len(fruits):
    if len(fruits[i])<5:
        rovid.append(fruits[i])
    i+=1

print(rovid)

rovid=[]
i=0

while True:
    print(i)
    if len(fruits[i-1])<5:
        rovid.append(fruits[i])

    if len(fruits)==i:
        break
    
    i+=1

print(fruits[:2])
print(fruits[-2:])
print(fruits[len(fruits)-2:])
print(fruits[1:-1])


paratlan=fruits[1::2]
print(paratlan)

paros=fruits[::2]
print(paros)

masolat=fruits
print(masolat)


masolat.reverse()
print(masolat)

print(fruits[::-1])





