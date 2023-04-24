# Import the required libraries
from tkinter import *
import math

def eltol(pontok,x,y):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i%2==1:
            vissza.append(pont+y)
        else:
            vissza.append(pont+x)
    return vissza
           
def nagyit(pontok,meret=1):
    vissza=[]
    for pont in pontok:
        vissza.append(pont*meret)
    return vissza
   

def forgat(pontok, szog):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i%2==0:
            szogRadian=math.radians(szog)
            
            x = pontok[i]*math.cos(szogRadian) - pontok[i+1]*math.sin(szogRadian)
            y = pontok[i]*math.sin(szogRadian) + pontok[i+1]*math.cos(szogRadian)
            vissza.append(x)
            vissza.append(y)
    return vissza





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


nev=[]

for i in range(5):
    nev.append(eltol(M,100*i,0))

for betu in nev:
    betu=nagyit(betu,0.5)
    betu=eltol(betu,100,100)


kozep=[0,0]
db=0
for betu in nev:
    xK=betu[::2]
    yK=betu[1::2]
    kozep[0]+=sum(xK)
    kozep[1]+=sum(yK)
    db+=len(xK)
    
kozep[0]/=db
kozep[1]/=db



#canvas.create_line(M, fill="red", width=5)

m2=eltol(M,100,100)

#canvas.create_line(m2, fill="red", width=5)




szog=0

while True:
    canvas.delete("all")
    szog+=0.5
    print(szog)
    for betu in nev:        
        betu=eltol(betu, -kozep[0], -kozep[1])
        betu=forgat(betu,szog)
        betu=eltol(betu, kozep[0], kozep[1])
        canvas.create_line(betu, fill="green", width=2)

        win.update_idletasks()
        win.update()

    #win.mainloop()

