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
for i in range(len(fruits)):
    if len(fruits[i])<5:
        print(fruits[i])







