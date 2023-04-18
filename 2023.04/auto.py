class auto:
    def __init__(self,szin,ajtok,marka,tipus):
        self.szin=szin
        self.ajtok=ajtok
        self.marka=marka
        self.tipus=tipus

    def indul(self):
        print("Brrrrr")

    def kurt(self):
        print("Tü-tűű")

    def jelzo(self):
        print("Kat kat kat")


class BMW(auto):    
    def __init__(self,szin,ajtok,marka,tipus):
        super().__init__(szin,ajtok,marka,tipus)

    




kocsi=auto("piros", 4, "Opel", "Corsa")

print(kocsi)
kocsi.indul()
