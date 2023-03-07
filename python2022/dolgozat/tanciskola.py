f=open("tancrend.txt")
lvas=f.read().splitlines()
db=len(lvas)//3
tanc=[]
fiu=[]
lany=[]

for i in range(db):
    tanc.append(lvas[3*i])
    lany.append(lvas[3*i])
    fiu.append(lvas[3*i])

f.close()

print("Első tánc: " + tanc[0])
print("Utolsó tánc: " + tanc[db-1])

print("Szamba táncok száma: ", tanc.count("samba"))

for e in range(db):
    if lany[e]=="Vilma":
        print(tanc[e])

par=input("Kérek egy táncot: ")
tancok=0

if tanc.count(par)<0:
    print("Ilyen tánc nem volt.")
else:
    for e in range(db):
        if lany[e]=="Vilma" and tanc[e]==parok:
            print("A " + tanc[e] + " bemutatóján Vilma " + fiu[e] + " párja volt.")
            tancok=tancok+1
    if tancok==0:
        print("Vilma nem táncolt samba-t.")
