from tkinter import *
from tkinter import ttk
from pygame import mixer
import os
from tkinter.filedialog import askdirectory

root=Tk()
root.geometry("500x370")
root.resizable(0,0)
root.title('Music Player -Coder.Buzz')
root.config(bg="red")

def load():
	directory = askdirectory()
	os.chdir(directory)

	songs=os.listdir()
	for s in songs:
		playlist.insert(END,s)

def playsong():   
    currentsong=playlist.get(ACTIVE)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()
    Label(root,text="Playing:- "+str(currentsong),bg="red",fg="white",font=3).grid(row=1,columnspan=4,pady=5)

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()    

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

playlist=Listbox(root,selectmode=SINGLE,font=('Arial',15),width=43,bg="yellow")
playlist.grid(columnspan=5,padx=10,pady=10)

ttk.Button(root,text="Play",cursor="hand2",command=playsong).grid(row=3,column=0,padx=10)
ttk.Button(root,text="Pause",cursor="hand2",command=pausesong).grid(row=3,column=1)
ttk.Button(root,text="Stop",cursor="hand2",command=stopsong).grid(row=3,column=2,padx=10,pady=10)
ttk.Button(root,text="Resume",cursor="hand2",command=resumesong).grid(row=3,column=3)
ttk.Button(root,text="Load Music Folder",cursor="hand2",command=load).grid(row=2,columnspan=5)

root.mainloop()