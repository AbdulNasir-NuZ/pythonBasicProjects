from tkinter import *
import random

#Initialize Window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock Paper Scissors')
root.config(bg ='white')

#User Choice
user_take = StringVar()
Label(root, text = 'Choose One: rock, paper, scissors',bg="white",font=10).place(x = 70,y=50)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'antiquewhite2').place(x=90,y = 100)

#Computer Choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
    
#Function to Play
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set("Tie, You Both Select's Same!")
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set("You Loose, Computer Select's Paper")
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set("You Win, Computer Select's Scissors")
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set("You Loose, Computer Select's Scissors")
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set("You Win, Computer Select's Rock")
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set("You Loose, Computer Select's Rock")
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set("You Win, Computer Select's Paper")
    else:
        Result.set('Invalid: Choose any one -- rock, paper, scissors')
      
##Function to Reset
def Reset():
    Result.set("") 
    user_take.set("")

#Buttons
Entry(root,textvariable = Result,bg ='antiquewhite2',width = 50).place(x=25,y =250)
Button(root,text = 'PLAY',command = play).place(x=170,y=150)
Button(root,text = 'RESET',command = Reset).place(x=100,y=310)
Button(root,text = 'EXIT',command = root.destroy).place(x=250,y=310)

root.mainloop()
