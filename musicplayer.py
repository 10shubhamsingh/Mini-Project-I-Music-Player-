import os
import pickle
import tkinter as tk
from pygame import mixer

class Player(tk.Frame):      #player class
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.pack()

root=tk.Tk()
root.geometry('600x400')
root.wm_title('Music player')

app=Player(master=root)
app.mainloop()
