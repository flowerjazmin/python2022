
def ado():
    pass




f=open("utca.txt")

cim=[]
for sor in f:
    temp=sor.replace("\n", "").split(" ")
    cim.append(temp)
    
f.close()

cim.remove(cim[0])
cim.remove(cim[-1])

print("2. feladat. A mintában {} telek szerepel.".format(len(cim)))

a=input("3. feladat. Kérem egy tulajdonos adószámát: ")

for sor in cim:
    if sor[0]==a:
        print(sor[1] + " utca " + sor[2])

#print(cim)
