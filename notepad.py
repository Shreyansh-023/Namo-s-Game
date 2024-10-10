import  os
from tkinter import *
from tkinter.messagebox import  showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
def newfile():
    global file
    root.title("Untitled Notepad")
    file=None
    maintext.delete(1.0,END)
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",
                         filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        maintext.delete(1.0,END)
        f=open(file,"r")
        maintext.insert(1.0,f.read())
        f.close()
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="untitled.txt",
                               defaultextension=".txt",
                               filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
        if file=="":
            file=None
        else:
#             save as new file
            f=open(file,"w")
            f.write(maintext.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
    else:
        f = open(file, "w")
        f.write(maintext.get(1.0, END))
        f.close()

def undo():
    pass
def cut():
    maintext.event_generate(("<<Cut>>"))
def copy():
    maintext.event_generate(("<<Copy>>"))
def paste():
    maintext.event_generate(("<<Paste>>"))

def about():
    showinfo("About","This Notepad is built by Namo")
if __name__ == '__main__':

    root=Tk()
    root.title("Untitled - Notepad")
    root.geometry("900x600")
    root.config(borderwidth=20,bg="silver")

    scrolly=Scrollbar(root)
    scrolly.pack(fill=Y,side=RIGHT)

    maintext=Text(root,bg="dark grey",font=("times new roman",13),padx=30,pady=20,
                  yscrollcommand="scrolly")
    scrolly.config(command=maintext.yview)
    maintext.pack(fill=BOTH,expand=True)

    file=None
    # menu

    mainmenu=Menu(root)
    menu1=Menu(mainmenu,tearoff=0)
    mainmenu.add_cascade(label="File",menu=menu1)
    # To open new file
    menu1.add_command(label="New file",command=newfile)
    # To open existing file
    menu1.add_command(label="Open...",command=openfile)
    # To save
    menu1.add_command(label="Save",command=savefile)
    menu1.add_separator()
    # to exit
    menu1.add_command(label="Exit",command=root.destroy)


    menu2=Menu(mainmenu,tearoff=0)
    mainmenu.add_cascade(label="Edit",menu=menu2)
    menu2.add_separator()
    menu2.add_command(label="Cut",command=cut)
    menu2.add_command(label="Copy",command=copy)
    menu2.add_command(label="Paste",command=paste)
    menu2.add_separator()
    # mainmenu.add_cascade(label="Edit",menu=menu2)


    menu3=Menu(mainmenu,tearoff=0)
    mainmenu.add_cascade(label="Help",menu=menu3)
    menu3.add_command(label="About",command=about)


    root.config(menu=mainmenu)

    root.mainloop()
