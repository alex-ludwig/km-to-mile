import tkinter as tk
import ttkbootstrap as ttk

def clicked():
    #print(text_var)
    out_value.set(text_var.get()*1.61)

# window
window = ttk.Window(themename="darkly")#journal
window.title("yo??")
window.geometry("500x350")

# widgetss
title = ttk.Label(master=window, font="serif 48 italic", text="Enter Kms", foreground="#333")

in_frame = ttk.Frame(master=window)
text_var = tk.IntVar()
entry = ttk.Entry(master=in_frame, textvariable=text_var)
btn = ttk.Button(master=in_frame, text='check', command=clicked)

out_value = tk.StringVar()
out_value.set("Km To Mile??")
output = ttk.Label(master=window, font="serif 12 italic", textvariable=out_value)

# display
title.pack(pady=20)
entry.pack(side="left")
btn.pack(side="left", padx=5)
in_frame.pack(pady=15)
output.pack(pady=5)

window.mainloop()