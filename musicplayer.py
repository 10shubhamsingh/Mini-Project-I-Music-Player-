import os
import pickle
import tkinter as tk
from pygame import mixer

class Player(tk.Frame):      #player class
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.pack()

        self.playlist=[]

        self.create_frames()

    def create_frames(self):
        self.track=tk.LabelFrame(self,text='Song Track',
                        font=("Times New Roman",14,"bold"),
                                 bg="grey",fg="black",bd=5,relief=tk.GROOVE)
        self.track.configure(width=400,height=300)
        self.track.grid(row=0,column=0)


root=tk.Tk()
root.geometry('600x400')
root.wm_title('Music player')

app=Player(master=root)
app.mainloop()
