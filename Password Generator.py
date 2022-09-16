from tkinter import *
from tkinter import ttk
import random

root=Tk()
root.geometry("600x500")
root.resizable(0,0)
root.title("Password Generator")

def generate():
	length=a.get()
	lower="abcdefghijklmnopqrstuvwxyz"
	upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	number="0123456789"
	symbols="[]{}()*;/,._-"

	alll=lower+upper+number+symbols
	password="".join(random.sample(alll,length))
	Label(root,text="Random Generated Password:- ",font=10,fg="red").place(x=150,y=250)

	x=Entry(root,bd=0,width=40,fg="green",font=10)
	x.insert(0,password)
	x.config(state="readonly")
	x.place(x=250,y=280)
	

a=IntVar()
Label(root,text="** Password Generator **",font=("Helvetica",15,"bold")).place(x=180,y=80)
Label(root,text="Enter Length:- ").place(x=150,y=150)
l_entry=ttk.Entry(root,textvariable=a)
l_entry.place(x=250,y=150)

ttk.Button(root,text="Generate",cursor="hand2",command=generate).place(x=250,y=200)
root.mainloop()