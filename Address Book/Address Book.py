#import library
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk

#Creating Main window
root = Tk()
root.geometry('800x600')
root.resizable(0,0)
root.title('Address Book')

a=ImageTk.PhotoImage(file="image.jpg")
img=Label(root,image=a)
img.place(x=0,y=0)

contactlist = [
    ['John',  '0176738493'],
    ['David',  '2684430000'],
    ['Holy',   '4338354432'],
    ['Coder Buzz','6834552341']
    ]
#To Create Frame
frame = Frame(root)
frame.pack(side = RIGHT)

scroll = ttk.Scrollbar(frame,orient=VERTICAL)
select = Listbox(frame,yscrollcommand=scroll.set,height=20)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT,fill=Y)
select.pack(side=LEFT,fill=BOTH,expand=1)


#Function to Get Selected Value
def Selected():
    return int(select.curselection()[0])
    
#To Add New Contact
def AddContact():
    contactlist.append([Name.get(), Number.get()])
    Select_set()

#To Delete Selected Contact
def DELETE():
    del contactlist[Selected()]
    Select_set()
   
#To View Selected Contact
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

#To Clear Fields
def RESET():
    Name.set('')
    Number.set('')


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
Select_set()

Name = StringVar()
Number = StringVar()
#+++++++++++++++ Buttons ++++++++ labels +++++++++ Entry Widget +++++++++++++++++++++++
Label(root,text="** Address Book **",font=("Helvetica",20,"bold"),bg="#DFE4EA").place(x=200,y=50)
Label(root,text="NAME",font="12",bg="#DFE4EA").place(x=150,y=150)
ttk.Entry(root,textvariable=Name,width=25).place(x= 250,y=150)
Label(root,text="PHONE NO.",font="12",bg="#DFE4EA").place(x=150,y=190)
ttk.Entry(root,textvariable=Number,width=25).place(x= 250,y=190)

ttk.Button(root,text=" ADD",cursor="hand2",command = AddContact).place(x=150,y=250)
ttk.Button(root,text="DELETE",cursor="hand2",command = DELETE).place(x=250,y=250)
ttk.Button(root,text="VIEW",cursor="hand2",command = VIEW).place(x=350,y=250)
ttk.Button(root,text="RESET",cursor="hand2",command = RESET).place(x=200,y=300)
ttk.Button(root,text="EXIT",cursor="hand2", command = root.destroy).place(x=300,y=300)

root.mainloop()