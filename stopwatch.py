#This is a simple GUI based stopwatch

import time
from tkinter import *
from tkinter import messagebox

def second(secs):
    for i in range(secs,-1,-1):
        time.sleep(1)
        if i<10:
            sec.set(f"0{i}")
            secLabel.update()
        else :
            sec.set(i)
            secLabel.update()
def minute(mins,sec=0):
    if sec:
        min.set(f"0{mins}")
        minLabel.update()
        second(sec)
        for i in range(mins-1,-1,-1):
            if i<10:
                min.set(f"0{i}")
                minLabel.update()
            else :
                min.set(i)
                minLabel.update()
            second(59)

    else:
        for i in range(mins - 1, -1, -1):
            if i < 10:
                min.set(f"0{i}")
                minLabel.update()
            else:
                min.set(i)
                minLabel.update()
            second(59)
def mainfunc():
        minute(minvar.get(),secvar.get())

root=Tk()
root.geometry("300x200")
root.title("Stop Watch by Namo")
root.configure(bg="dark green")
minvar=IntVar()
minvar.set("")
secvar=IntVar()

Label(root,text="Minutes : ",bg="dark green",fg="white",font="lucida 12 bold").grid(row=0,column=0)
Scale(root,variable=minvar,from_=0,to=60,orient=HORIZONTAL,bg="dark green",troughcolor="lime",fg="white",font="lucida 12 bold").grid(row=0,column=1)
Label(root,text="Seconds : ",bg="dark green",fg="white",font="lucida 12 bold").grid(row=1,column=0)
Scale(root,variable=secvar,from_=0,to=60,orient=HORIZONTAL,bg="dark green",troughcolor="lime",fg="white",font="lucida 12 bold").grid(row=1,column=1)
b=Button(root,text="Start",command=mainfunc,bg="gold")
b.grid(row=2,column=0)
f=Frame(root,bg="yellow",borderwidth=20,relief=RAISED)
f.grid(row=2,column=1)
min=IntVar()
min.set("00")
sec=IntVar()
sec.set("00")
minLabel=Label(f,textvariable=min,font="lucida 15 bold",bg="khaki",pady=10,padx=10)
minLabel.grid(row=0,column=0)
secLabel=Label(f,textvariable=sec,font="lucida 15 bold",bg="khaki",pady=10,padx=10)
secLabel.grid(row=0,column=2)
Label(f,text=":",font="lucida 15 bold",bg="khaki",pady=10).grid(row=0,column=1)

root.bind()

root.mainloop()
