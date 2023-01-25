import random

def szoBeker():
    szo=input("Kérek egy szót: ")
    if szo=="":
        jelentes=""
    else:
        jelentes=input(szo+" jelentése: ")
    return [szo, jelentes]


szavak=[]
def sokBeker():
    szo=szoBeker()
    while szo[0]!="":
        szavak.append(szo)
        szo=szoBeker()
    return szavak

def filebaIr(lista):
    f=open("szotar.txt", "a")

    for e in lista:
        #print(e)
        f.write(" ".join(e))
        f.write("\n")
    f.close()


kerdesek=[]
def beolvas():
    f=open("szotar.txt", "r")
    
    for sor in f:
        kerdesek.append(sor.replace("\n", "").split(" "))
    
    f.close






def kerdez():
    valasztott=random.choice(kerdesek)
    #print("valasztott", valasztott)
    rossz=[]
    for e in range(3):
        temp=random.choice(kerdesek)
        #print("temp", temp)
        while not (temp not in rossz and temp!=valasztott):
            temp=random.choice(kerdesek)

        rossz.append(temp)
        #print("rossz",rossz)



    print("-"*40)
    print("Mit jelent: "+ valasztott[0]+ "?")

    rossz.append(valasztott)
    #valaszbekeres
    abc="abcdefghijklmnopqrstuvwxyz"
    random.shuffle(rossz)

    i=0
    for e in rossz:
        print(abc[i]+ ") " +e[1])
        i+=1



    valasz=input("Válasz: ")

    hol=4
    
    while hol>=4:
        try:
            if valasz!="":
                hol=abc.index(valasz)
        except:
            valasz=input("Válassz újra: ")
        else:
            if hol>=4:
                valasz=input("Válassz újra: ")


    if valasztott[0]==rossz[hol][0]:
        print("Válaszod helyes! :D")
    else:
        print("Válaszod hibás! :c")

    

    


    
    

beolvas()
for i in range(10):
    kerdez()



#szavak=sokBeker()
#filebaIr(szavak)




