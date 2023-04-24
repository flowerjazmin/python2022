# Import the required libraries
from tkinter import *
import math




class forgat2:
    canvas=0
    vonalak=[]
    szog=0
    szogSebesseg=0.05
    szinek=[]
    
    def __init__(self,canvas,vonalak):
        self.canvas=canvas
        self.vonalak=vonalak

        for i,betu in enumerate(self.vonalak):
            betu+=betu[:2]
            betu=self.nagyit(betu,2)
            self.vonalak[i]=self.eltol(betu,200,200)

        self.kozepSzamol()

    def rajzol(self):
        canvas.delete("all")
        self.szog+=self.szogSebesseg
        for i,betu in enumerate(self.vonalak):        
            betu=self.eltol(betu, -self.kozep[0], -self.kozep[1])
            betu=self.forgat(betu,self.szog)
            betu=self.eltol(betu, self.kozep[0], self.kozep[1])
            
            self.canvas.create_line(betu, fill=self.szinek[i], width=2)

    def eltol(self,pontok,x,y):
        vissza=[]
        for i, pont in enumerate(pontok):
            if i%2==1:
                vissza.append(pont+y)
            else:
                vissza.append(pont+x)
        return vissza
               
    def nagyit(self,pontok,meret=1):
        vissza=[]
        for pont in pontok:
            vissza.append(pont*meret)
        return vissza
       

    def forgat(self,pontok, szog):
        vissza=[]
        for i, pont in enumerate(pontok):
            if i%2==0:
                szogRadian=math.radians(szog)
                
                x = pontok[i]*math.cos(szogRadian) - pontok[i+1]*math.sin(szogRadian)
                y = pontok[i]*math.sin(szogRadian) + pontok[i+1]*math.cos(szogRadian)
                vissza.append(x)
                vissza.append(y)
        return vissza

    def kozepSzamol(self):
        self.kozep=[0,0]
        db=0
        for betu in self.vonalak:
            xK=betu[::2]
            yK=betu[1::2]
            self.kozep[0]+=sum(xK)
            self.kozep[1]+=sum(yK)
            db+=len(xK)
        
        self.kozep[0]/=db
        self.kozep[1]/=db




























# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("600x300")

# Create a canvas widget
canvas=Canvas(win, width=1000, height=1000)
canvas.configure(bg="lightgray")
canvas.pack()

# Add a line in canvas widget

M = [10,10,30,10,90,60,150,10,170,10,170,170,150,170,150,30,90,80,30,30,30,170,10,170,10,10]


nev=[M]

#for i in range(5):
#    nev.append(eltol(M,100*i,0))


elso=forgat2(canvas, nev)
elso.szinek=["purple"]






for betu in nev:
#    betu=nagyit(betu,0.5)
 #   betu=eltol(betu,100,100)
   pass






#canvas.create_line(M, fill="red", width=5)

#m2=eltol(M,100,100)

#canvas.create_line(m2, fill="red", width=5)




szog=0

while True:
    elso.rajzol()
    
    win.update_idletasks()
    win.update()

    #win.mainloop()














