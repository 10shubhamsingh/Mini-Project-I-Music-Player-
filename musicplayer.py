import os
import pickle
import tkinter as tk
from pygame import mixer
from tkinter import filedialog
from tkinter import PhotoImage

class Player(tk.Frame):      #player class
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.pack()

        self.playlist=[]

        self.create_frames()
        self.track_widgets()
        self.control_widgets()
        self.tracklist_widget()

    def create_frames(self):
        self.track=tk.LabelFrame(self,text='Song Track',
                        font=("Times New Roman",14,"bold"),
                                 bg="grey",fg="white",bd=5,relief=tk.GROOVE)
        self.track.configure(width=410,height=300)
        self.track.grid(row=0,column=0,padx=10)

        self.tracklist = tk.LabelFrame(self, text=f'Playlist - {len(self.playlist)}',
                                   font=("Times New Roman", 14, "bold"),
                                   bg="grey", fg="white", bd=5, relief=tk.GROOVE)
        self.tracklist.configure(width=190, height=400)
        self.tracklist.grid(row=0, column=1, rowspan=3,pady=5)

        self.controls = tk.LabelFrame(self,
                                   font=("Times New Roman", 15, "bold"),
                                   bg="white", fg="white", bd=2, relief=tk.GROOVE)
        self.controls.configure(width=410, height=80)
        self.controls.grid(row=2, column=0,pady=5,padx=10)

    def track_widgets(self):

        self.canvas= tk.Label(self.track, image=img)
        self.canvas.configure(width=400, height=240)
        self.canvas.grid(row=0, column=0)

        self.canvas= tk.Label(self.track, font=("Times New Roman", 15, "bold"),
                              bg='white',fg='dark blue')
        self.canvas['text']='Music Player'
        self.canvas.configure(width=30, height=1)
        self.canvas.grid(row=1, column=0)



    def control_widgets(self):
        pass

    def tracklist_widget(self):
        pass


root=tk.Tk()
root.geometry('600x400')
root.wm_title('Music player')

img= PhotoImage(file='images/music.gif')

app=Player(master=root)
app.mainloop()
