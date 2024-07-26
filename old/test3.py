from tkinter import *
from tkinter import Label
import tkvideo

root = Tk()
my_label = Label(root)
my_label.pack()
player = tkvideo.tkvideo("ANIME.mp4", my_label, loop = 1, size = (1280,720))
player.play()

root.mainloop()