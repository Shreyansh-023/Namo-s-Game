
#This is a Game based on Randomness
#The computer randomly chooses a number between 1 to 100
# We need to guess the number in minimum guesses to win

from tkinter import *
from tkinter import messagebox as mess
import random
import time
'''import pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()'''


compnumber=random.randint(1,101)
# print(compnumber)

def  hintShow(hint,i):
    mess.showinfo("Namo's Hint",f"{hint}\nChance no.{i}")


level=[]
def SubmitNumber():
    level.append("1")
    if len(level)>10:
        Label(root,text=f"Game Over Buddy !!! \n The Number was {compnumber}\n Better Luck next time",
        bg="red",font=("",20,"bold"),borderwidth=29,relief=RAISED).grid(row=0,column=0)
        
    else:
        if compnumber==int(usernumber.get()):
                Label(root,text=f"Congratulations !!! \n You got me in {len(level)} guesses ",bg="gold",font=("",40,"bold"),borderwidth=29,relief=RAISED).grid(row=0,column=0)
        elif compnumber>int(usernumber.get()):
                newhint=f"{int(usernumber.get())} is smaller than my choice."
                hintShow(newhint,len(level))

        elif compnumber<int(usernumber.get()):
                newhint=f"{int(usernumber.get())} is bigger than my choice."
                hintShow(newhint,len(level))

k=[]
def listen():
    k.append("2")
    if len(k)>1:
        speak("You can listen this only once.")
    else:
        speak(content)

if __name__ == '__main__':
    root=Tk()
    # From here your GUI Start
    root.geometry("1000x500")
    root.title("Number's Game with Namo")
    color="dark grey"
    mainframe=Frame(root,relief=SUNKEN,borderwidth=20,pady=20,padx=20,background=color
                    ,height=1000)
    mainframe.grid(row=0,column=0)
    Label(mainframe,text="Welcome to Namo's Choice Game",bg="black",fg="white",relief=RAISED,borderwidth=20,
        font=("times new roman",30,"bold")).pack(side=TOP,fill="x")
    compframe=Frame(mainframe,relief=SUNKEN,borderwidth=15,pady=10,
                    padx=10,bg="orange",height=500,width=500)
    compframe.pack(side=LEFT)
    content="""Hello, Welcome. My name is Namo
    I will be playing this game with
    you. I have choosen a number
    between 1 to 100, Your task is
    to find that number using hints
    I will be giving to you throughout
    the game. Thank you !!!
    (You have got 10 chances for it)
    Good luck."""
    Label(compframe,text=content,bg="linen",fg="black",padx=10,pady=10,
        font=("times new roman",12,"bold")).pack(side=TOP,fill="x")
        
    Button(compframe,text="Listen",bg="limegreen",command=listen,font=("",13,"bold")).pack(side=TOP)
    userframe=Frame(mainframe,bg="silver",pady=20,padx=20,relief=GROOVE,borderwidth=15)
    userframe.pack()
    Label(userframe,text="Slide to your guessed number : ",bg="gold",fg="black",relief=RAISED,
        font=("",12,"bold")).grid(row=0,column=0)

    usernumber=Scale(userframe,bg="black",fg="white",orient=HORIZONTAL,length=400)
    usernumber.grid(row=1,column=0,pady=10)
    usernumber.set(50)
    Button(userframe,text="Submit",bg="maroon",command=(SubmitNumber),
                fg="white",font=("",13,"bold")).grid(row=3,column=0,pady=40)

    root.mainloop()
