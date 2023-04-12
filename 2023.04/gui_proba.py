# Import the required libraries
from tkinter import *

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
canvas.create_line(00,00,200,35,20,300,700,500, fill="red", width=5)


canvas.create_line(100,200,100,35, fill="green", width=5)
canvas.create_line(300,200,300,35, fill="green", width=5)
canvas.create_line(100,35,300,35, fill="green", width=5)
canvas.create_line(100,200,300,35, fill="red", width=5)

win.mainloop()
