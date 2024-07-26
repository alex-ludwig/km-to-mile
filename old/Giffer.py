from tkinter import StringVar, TOP
from tkinterdnd2 import TkinterDnD, DND_ALL
import customtkinter as ctk

class App(ctk.CTk, TkinterDnD.DnDWrapper):
    #def __init__(self, *args, **kwargs):
    def __init__(self, _name="App Name", w=200, h=200, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)
        #
        self.geometry(str(w)+ "x" + str(h))
        #self.geometry("350x100")
        #self.title("Get file path")
        self.title = _name

        nameVar = StringVar()

        entryWidget = ctk.CTkEntry(self)
        entryWidget.pack(side=TOP, padx=5, pady=5)

        pathLabel = ctk.CTkLabel(self, text="Drag and drop file in the entry box")
        pathLabel.pack(side=TOP)

        entryWidget.drop_target_register(DND_ALL)
        entryWidget.dnd_bind("<<Drop>>", get_path)

ctk.set_appearance_mode("dark")
#ctk.set_default_color_theme("blue")

def get_path(event):
    pathLabel.configure(text = event.data)

#root = TkinterDnD.Tk()
app = App("Giffer", 800, 550)
app.mainloop()