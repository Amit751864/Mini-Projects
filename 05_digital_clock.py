import tkinter as tk
from time import strftime


root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    Label.config(text =string)
    Label.after(1000,time)
#calibri
Label =tk.Label(root,font=('Castellar',50,'bold') ,background='yellow',foreground='black')
Label.pack(anchor='center')



time()
root.mainloop()

  

