import customtkinter


class App(customtkinter.CTk):
    
    def __init__(self, name="my_app", w=400, h=150):
        super().__init__()
        
        self.title(name)
        self.design(w, h)
        
        #print("hello")
        
        
    def button_callback(self):
        print("button pressed")
    
    def design(self, w, h):
        self.geometry(str(w)+ "x" + str(h))#"400x150")
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0), weight=1)
        self.panel_1 = customtkinter.CTkFrame(self, width=w, height=h, fg_color="transparent", bg_color=("#D0D0D0", "0.5"))
        self.panel_1.grid(row=0, column=0, padx=20, pady=20)
        
        ##
        main_frame = self.panel_1
        main_frame.grid_columnconfigure((0,1,2), weight=1)
        
        label_1 = customtkinter.CTkLabel(master = main_frame, text="label 1", pady=10, bg_color=("#333333"), text_color="white")
        label_1.grid(row=0, column=0, pady=10, columnspan=2)

        # self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        # self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        # self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        # self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        # self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        # self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
    
    def start_loop(self):
        print(self)
        self.mainloop()
    
    def destroy_loop(self):
        print(self)
        self.destroy()
        
app = App("Giffer", 800, 550)
app.start_loop()