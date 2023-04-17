# Import the required libraries
from tkinter import *

def eltol(pontok,x,y):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i%2==0:
            vissza.append(pont+x)
        else:
            vissza.append(pont+y)
    return vissza

def nagyit(pontok,meret=1):
    vissza=[]
    for pont in pontok:
            vissza.append(pont*meret)
    return vissza

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x500+100+100")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300, bg="skyblue")
canvas.pack(fill=BOTH, expand=1)

#canvas2=Canvas(win, width=500, height=300, bg="green")
#canvas2.pack(fill=BOTH, expand=1)


# Add a line in canvas widget
#canvas.create_line(100,200,200,35, fill="green", width=5)
#canvas.create_line(00,00,200,35,20,300,700,500, fill="red", width=5)


kor=[100,75,100,35,300,35,100,35,300,150,300,35,250,75,100,75,250,150,250,75,250,150,200,150,300,150,350,150,200,150,200,185]
canvas.create_line(kor, fill="purple", width=5)

"""
canvas.create_line(100,75,100,35, fill="green", width=5)
canvas.create_line(300,35,100,35, fill="red", width=5)
canvas.create_line(300,150,300,35, fill="blue", width=5)
canvas.create_line(250,75,100,75, fill="red", width=5)
canvas.create_line(250,150,250,75, fill="green", width=5)
canvas.create_line(250,150,200,150, fill="yellow", width=5)
canvas.create_line(300,150,350,150, fill="yellow", width=5)
canvas.create_line(200,150,200,185, fill="green", width=5)
"""


kor2=eltol(kor,100,-50)
canvas.create_line(kor2, fill="blue", width=5)

























win.mainloop()
