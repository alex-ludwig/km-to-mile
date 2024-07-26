import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import StringVar, filedialog, TOP, END, ALL, Canvas
from tkinterdnd2 import TkinterDnD, DND_ALL
from tkhtmlview import HTMLLabel
import webbrowser
from tkvideo import tkvideo
import cv2


'''
G I F F E R   A P P
v0.1

'''

'''
-----------------
 M A I N   A P P
-----------------
'''

class App(ctk.CTk, TkinterDnD.DnDWrapper):
    
    def __init__(self, name, w, h, *args, **kwargs):
        
        super().__init__(fg_color="#DDD")
        self.TkdndVersion = TkinterDnD._require(self)
        
        self.title(name)
        self.geometry(str(w)+ "x" + str(h))
       
        self.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)  # configure grid system
        self.grid_columnconfigure((0,1,2,3), weight=1)
        
        
        
        self.output_frame = outputSide(self)
        self.input_frame = inputSide(self)
        self.top_frame = topSide(self)
        self.footer_frame = bottomSide(self)


class topSide(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        # add widgets onto the frame...
        self.grid(row=0, column=0, pady=(10,0), padx=20, sticky="nsew", columnspan=7)
        self.grid_columnconfigure(0, weight=1)
        logo_image = Image.open('assets/logo.png')
        
        logo = ctk.CTkImage(logo_image, size=(100,100))
        logo_holder = ctk.CTkLabel(self, image=logo, text="").grid(row=0, column=0, sticky="nsew")
        
class bottomSide(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#333", **kwargs)

        # add widgets onto the frame...
        self.grid(row=7, column=0, padx=0, sticky="nsew", columnspan=7, rowspan=2)
        self.grid_columnconfigure(0, weight=1)
        
        footer_text = "Feito por Alex Ludwig"
        self.footer_url = "https://www.alexludwig.com.br"
        
        txt = ctk.CTkButton(self, text=footer_text, text_color="#666", hover_color="#333", bg_color="transparent", fg_color="transparent", corner_radius=0, height=40, command=self.get_url)
        
        txt.grid(row=0, column=0, sticky="nsew")
        
    def get_url(self):
        webbrowser.open(self.footer_url)
        
        
'''
---------------------
 I N P U T   A R E A
--------------------- 
'''
class inputSide(ctk.CTkFrame):
    
    entryWidget = ""
    listbox = ""
    main_button = ""
    loaded = False
    
    
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="white", **kwargs) #bg_color="red", fg_color="transparent",

        # SET UP
        self.grid(row=1, column=0, padx=(20,10), pady=20, sticky="nsew", columnspan=3, rowspan=6)
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        
        # TITLE 1
        input_text = "Drag and drop:"
        self._copy1 = ctk.CTkLabel(self,text=input_text)
        self._copy1.grid(row=0, column=1, pady=5, sticky="n")
        
        # DRAG AND DROP
        self.entryWidget = ctk.CTkEntry(self, height=200)
        self.entryWidget.grid(row=1, column=1, sticky="nsew")
        self.entryWidget.drop_target_register(DND_ALL)
        self.entryWidget.dnd_bind("<<Drop>>", self.get_path)
        self.entryWidget.grid_columnconfigure(0, weight=1)
        self.entryWidget.grid_rowconfigure(0, weight=1)
        
        
        #listbox.grid(row=0, column=0, sticky="nsew")
        
        
        # TITLE 2    
        input_text = "Click to choose:"
        self._copy2 = ctk.CTkLabel(self,text=input_text)
        self._copy2.grid(row=2, column=1, sticky="n", pady=10)
        
        # BUTTON
        self.button = ctk.CTkButton(self, corner_radius=10, text="Buscar", command=self.get_files, fg_color="#333")
        self.button.grid(row=3, column=1, sticky="nsew", pady=10)
          
    def get_path(self, event):
        
        self.loaded = True
        file_path = event.data
        all_files = self.tk.splitlist(file_path)
        all_names = [self.get_file_name(i) for i in all_files]
        extension = [self.get_file_extension(i) for i in all_files]
        self.show_files(all_files, all_names, extension[0])
            
    def get_files(self):
       
        self.loaded = True
        all_files = filedialog.askopenfilenames()
        all_names = [self.get_file_name(_file) for _file in all_files]
        extension = [self.get_file_extension(i) for i in all_files]
        self.show_files(all_files, all_names, extension[0])     
            
    def get_file_name(self, name_path):
        #'''TEST OTHER OS'''
        # gets the last "/" in the name_path
        _last = [i for i in range(len(name_path)) if name_path[i] == "/"][-1]
        _in = _last + 1
        # gets the index of the dot in the ".ext"
        _out = -4
        #returns the slice of the name
        return name_path[_in:]
    
    def get_file_extension(self, file_path):
        
        return file_path[-4:]
    
    def show_files(self, paths, files, extension):
        
        # if not self.loaded:
        #     self.restart_all()
        self.listbox = ctk.CTkTextbox(self.entryWidget, width=0, height=0, bg_color="transparent", fg_color="transparent")
        self.listbox.insert("0.0",text="\n".join(files))
        self.listbox.grid(row=0, column=0, sticky="nsew")
        self.listbox.configure(state="disabled")
        self.button.configure(text="Recomeçar", command=self.restart_all)
        
        outputSide.set_result(app.output_frame, paths, files, extension)
    
    def restart_all(self):
        
        self.listbox.grid_remove()
        self.button.configure(text="Buscar", command=self.get_files)
        self.listbox.configure(state="normal")
        self.listbox.delete("1.0",END)
        self.listbox.grid(row=0, column=0, sticky="nsew")
        

'''
-----------------------
 O U T P U T   A R E A
-----------------------
'''     
class outputSide(ctk.CTkFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="white",**kwargs) #bg_color="blue", fg_color="transparent",  
        # add widgets onto the frame...
        self.grid(row=1, column=3, padx=(10,20), pady=20, sticky="nsew", columnspan=1, rowspan=6)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=1)
        #self.right = ctk.CTkFrame(self, bg_color="#000000", fg_color='transparent')
        #self.right.grid(row=0, column=2, columnspan=1, sticky="ew", padx=(0,0))
        #self.grid(row=0, column=0)
        self.label = ctk.CTkLabel(self, text="File Manager")
        self.label.grid(row=0, column=0, sticky="nsew")
        
        self.canvas = Canvas(self, bg="red")
        self.canvas.grid(row=2, column=0, sticky="nsew")
        #self.canvas.grid_columnconfigure(0, weight=1)
        #self.canvas.grid_rowconfigure(0, weight=1)
        #self.extension_box = ctk.CTkTextbox(self)
        #self.extension_box.grid(row=1, column=0, sticky="nsew")



    def set_result(self, paths, names, extension):
        
        #self.extension_box.delete("1.0", END)
        if extension != ".mp4": 
            extra = f"Image Sequence - Extension: [{extension}]"
        else: 
            extra = "Video to Gif"
        
        #self.extension_box.insert("0.0", text=extra)
        self.show_image(paths, names, extension)

    def show_image(self, paths, names, extension):
        
        print(extension)
        if extension != ".mp4":
            
            image_file = Image.open(paths[0])
            x = image_file.size[0]
            y = image_file.size[1]
            ar = int(x)/int(y)
            cw = int(self.canvas.winfo_reqwidth())
            ch = int(self.canvas.winfo_reqheight())
            cw_end = cw
            print(cw, ch)
            if y > cw:
                cw_end = ch
            ch_end = int(cw_end*ar)
            new_size = (cw_end, ch_end)
            print(new_size)
            
            
            image_file = image_file.resize(size=(cw_end, ch_end), resample=Image.Resampling.LANCZOS)
            image_asset = ImageTk.PhotoImage(image_file)
            self.image_asset = image_asset
            self.canvas.create_image(cw/2, ch/2, anchor="center" , image=image_asset)
            self.canvas.update()
            
            # image_holder = ctk.CTkLabel(self.canvas, image=imagetk, text="")
            # image_holder.grid(row=1, column=0, sticky="nsew")
            
        else:
            
            player = tkvideo(paths[0], names[0], label="video_label", loop = 1, size = (640,460))
            print("video\n\n\n")
            
    
        

app = App("Giffer v0.1", 800, 550)
app.mainloop()


#app.input_frame.entry_area.drop_target_register(DND_ALL)
#app.input_frame.entry_area.dnd_bind("<<Drop>>", self.get_path)

