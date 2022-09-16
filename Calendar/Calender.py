from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import calendar

root = Tk()
root.geometry('400x300')
root.title('Calender')

img = ImageTk.PhotoImage(Image.open('calendar.png'))
label = Label(image=img)
label.place(x=170,y=3)

def show():
        m = int(month.get())            # Getting Value of Month
        y = int(year.get())             # Getting Value of Year
        output = calendar.month(y,m)
        box.insert('end',output)        # Printing Output in the Text Box

def clear():
        box.delete(1.0,'end')

Label(root,text="Month",font=('verdana','10','bold')).place(x=70,y=80)
month = Spinbox(root, from_= 1, to = 12,width="5") 
month.place(x=140,y=80) 
  
Label(root,text="Year",font=('verdana','10','bold')).place(x=210,y=80)
year = Spinbox(root, from_= 2021, to = 3000,width="8") 
year.place(x=260,y=80) 

box = Text(root,width=33,height=8,relief=RIDGE,borderwidth=2)
box.place(x=70,y=110)

ttk.Button(root,text="Show",cursor="hand2",command=show).place(x=60,y=250)
ttk.Button(root,text="Clear",cursor="hand2",command=clear).place(x=160,y=250)
ttk.Button(root,text="Exit",cursor="hand2",command=root.destroy).place(x=260,y=250)

root.mainloop()