#This is a GUI based Mathematical Table teller for students
from tkinter import *
root=Tk()
root.geometry("300x630")
root.title("Table Teller")
root.configure(bg="dark cyan",borderwidth=15,relief=SUNKEN)

def table():
    f = Frame(root, borderwidth="13", bg="cyan")
    f.pack(fill=BOTH, side=TOP)
    for i in range(1,11):

        Label(f,text=f"{num.get()}",font="lucida 18 bold",bg="cyan").grid(row=i+1,column=0)
        Label(f,text="X",font="lucida 18 bold",bg="cyan").grid(row=i+1,column=1)
        Label(f,text=f"{i}",font="lucida 18 bold",bg="cyan").grid(row=i+1,column=2)
        Label(f,text="=",font="lucida 18 bold",bg="cyan").grid(row=i+1,column=3)
        Label(f,text=f"{(num.get()*i)}",font="lucida 18 bold",bg="cyan").grid(row=i+1,column=4)

    Button(f,text="Reset",command=f.destroy,bg="red").grid(row=13,column=4)
Label(root,text="Welcome to Table Teller",bg="aqua",font="lucida 12 bold",padx=10).pack(side=TOP,fill=X)
Label(root,text="Enter Number : ",bg="gold").pack()
num=IntVar()
Entry(root,textvariable=num).pack(padx=10,pady=10)
num.set("")
submit=Button(root,text="Confirm",bg="maroon",fg="white",font="lucida 12 bold"
              ,command=table).pack()

f=Frame(root,borderwidth="13",bg="cyan")
f.pack(fill=BOTH,side=TOP)

root.mainloop()
