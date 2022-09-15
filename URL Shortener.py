from tkinter import * 
import pyshorteners
from tkinter import ttk

root=Tk()
root.geometry("400x400")
root.resizable(0,0)
root.config(bg="#A535BF")
root.title("URL-Shortener")

Label(root,text="** URL- Shortener **",font=("Aerial",15),bg="#A535BF",fg="white").place(x=100,y=30)
Label(root,text="Enter URL",font=(10),bg="#A535BF",fg="white").place(x=55,y=75)

def short_my_url():
    urls = url.get()
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(urls)

    a=Entry(root,bd=0,width=40)
    a.insert(0,short_url)
    a.config(state="readonly")
    a.place(x=50,y=200)

url=ttk.Entry(root,width=40)
url.place(x=50,y=100)

ttk.Button(root,text="Short My URL!",cursor="hand2",command=short_my_url).place(x=150,y=150)
root.mainloop()