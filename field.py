from tkinter import *
import time, random

field = Tk()
# Set window(field) attributes
field.title('Game')
field.resizable(0,0)
field.wm_attributes('-topmost',1)

# Draw canvas
canvas = Canvas(field, width=500, height=400, highlightthickness=0)
canvas.pack()
field.update()