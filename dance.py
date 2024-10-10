from tkinter import *
import time
root=Tk()
def store():
    print("Submiting form...")
    currentform=f"{[usernamevar.get(),agevar.get(),gendervar.get(),dancetypevar.get(),vanservicevar.get()]} \n"
    with open("form.txt","a") as f:
        f.write(currentform)
    time.sleep(1)
    print("Form Submitted. Thank You !!!")    


root.geometry("1000x330")
root.title("Admission form")
mainframe=Frame(root,bg="grey",relief=SUNKEN,pady=20,padx=30,borderwidth=15)
mainframe.pack(side=TOP,fill=BOTH)
Label(mainframe,bg="light grey",fg="black",font=('times new roman',20,"bold"),text="Super Dancers").pack(fill="x",side=TOP)
inputframe=Frame(mainframe,bg="orange",pady=15,padx=10,relief=SUNKEN,borderwidth=10)
inputframe.pack(fill=BOTH)

usernamevar=StringVar()
agevar=StringVar()
gendervar=StringVar()
dancetypevar=StringVar()
vanservicevar=IntVar()

username=Label(inputframe,text="Name of Student : ",bg="orange",font=("times new roman",15,"bold"))
age=Label(inputframe,text="Age : ",bg="orange",font=("times new roman",15,"bold"))
gender=Label(inputframe,text="Gender : ",bg="orange",font=("times new roman",15,"bold"))
dancetype=Label(inputframe,text="Dance Type : ",bg="orange",font=("times new roman",15,"bold"))

username.grid(row=0,column=0)
age.grid(row=1,column=0)
gender.grid(row=2,column=0)
dancetype.grid(row=3,column=0)



usernameentry=Entry(inputframe,textvariable=usernamevar)
ageentry=Entry(inputframe,textvariable=agevar)
genderentry=Entry(inputframe,textvariable=gendervar)
dancetypeentry=Entry(inputframe,textvariable=dancetypevar)

usernameentry.grid(row="0",column="1")
ageentry.grid(row="1",column="1")
genderentry.grid(row="2",column="1")
dancetypeentry.grid(row="3",column="1")

vanservice=Checkbutton(inputframe,text=" Van Service",
variable=vanservicevar,font=("",15,"bold"),bg="yellow",
disabledforeground="orange",fg="black",borderwidth=10,relief=SUNKEN,height=1)
vanservice.grid(row="2", column="5")

Button(inputframe,text="SUBMIT",command=store).grid(row=4,column=2)
Button(inputframe,text="EXIT",command=exit,padx=15).grid(row=4,column=4)


root.mainloop()