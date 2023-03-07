f=open("szavazatok.txt")
jeloltek=[]

for sor in f:
    temp=sor.replace("\n", "")
    jeloltek.append(temp)


#print(jeloltek)

print("2.feladat")
print("A helyhatósági választáson {} képviselőjelölt indult.".format(len(jeloltek)))

f.close()

print("3.feladat")
nev=str(input("Kérek egy képviselőnevet: "))


#print(jeloltek[0])



for e in jeloltek:
    #print(e)
    if nev==str(e[2]):
        print(e[1])
    else:
        print("Ilyen nevű képviselő nem szerepel a nyílvántartásban.")





#print(jeloltek)

print("4.feladat")

szavazott=[]
szavazott.append(jeloltek)


print(szavazott)
