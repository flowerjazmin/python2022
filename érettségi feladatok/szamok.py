
f=open("felszam.txt", "r")

kerdesek=[]

for sor in f:
    josor=sor.replace("\n", "")
    josor2=f.readline().replace("\n", "")
    temp=josor2.split(" ")
    kerdesek.append([josor, int(temp[0]), int(temp[1]), temp[2]])


f.close
#♥
print("2. feladat")
print("Az adatfile-ban " + str(len(kerdesek)) + " kérdés van.")
