import random

vezetek=["Nagy", "Kovács", "Tóth", "Szabó", "Varga"]
kereszt=["Ábel", "Dagobert", "Edmund", "Odin", "Fábián"]

nevek=[]

for e in range(100):
    nevek.append(random.choice(vezetek) + " " + random.choice(kereszt))
    
print(nevek)



