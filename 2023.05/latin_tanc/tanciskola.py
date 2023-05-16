class tanc:
    def __init__(self, tanc, lany, fiu):
        self.tanc=tanc
        self.lany=lany
        self.fiu=fiu
        
    def __str__(self):
        return "Tánc: {}, Lány: {}, Fiú: {}.".format(self.tanc,self.lany,self.fiu)

    def isVilma(self):
        return self.lany=="Vilma"







f=open("tancrend.txt")

sorok=[]

#2.mego

tancok2=[]
temp=[]

for e in f:
    sorok.append(e.strip())
    #2.mego
    if len(temp)<3:
        temp.append(e)
    else:
        tancok2.append(tanc(temp[0],temp[1],temp[2]))
f.close()









#1.mego
tancok=[]

for i in range(len(sorok)//3):
    tancc=sorok[i*3]
    lany=sorok[i*3+1]
    fiu=sorok[i*3+2]
    tancok.append(tanc(tancc, lany, fiu))

print(tancok)


print("2. feladat")
print("Első tánc: {}, utolsó tánc: {}".format(tancok[0].tanc, tancok[-1].tanc))

db=0
for egyTanc in tancok:
    if egyTanc.tanc=="samba":
        db+=1

print("3.feladat")
print("Ennyi pár mutatta be a sambát: {}".format(db))


print("4.feladat")
print("Vilma ezekben szerepelt:")

for egyTanc in tancok:
    if egyTanc.isVilma():
        print(egyTanc.tanc)














