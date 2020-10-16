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
                                   font=("Times New Roman", 14, "bold"),
                                   bg="white", fg="white", bd=2, relief=tk.GROOVE)
        self.controls.configure(width=410, height=80)
        self.controls.grid(row=2, column=0,pady=5,padx=10)

    def track_widgets(self):
        pass

    def control_widgets(self):
        pass

    def tracklist_widget(self):
        pass


root=tk.Tk()
root.geometry('600x400')
root.wm_title('Music player')

app=Player(master=root)
app.mainloop()
