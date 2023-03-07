import random

vezetek=["Nagy", "Kovács", "Tóth", "Szabó", "Varga"]
keresztfiu=["Ábel", "Dagobert", "Edmund", "Odin", "Fábián"]
keresztlany=["Hanna","Zoé","Léna","Emma","Boglárka"]


nevek=[]

for e in range(100):
    nevek.append(random.choice(vezetek) + " " + random.choice(keresztfiu))
    
print(nevek)

print()

lanyok=[]
for e in range(100):
    lanyok.append(random.choice(vezetek) + " " + random.choice(keresztlany))
    
print(lanyok)

