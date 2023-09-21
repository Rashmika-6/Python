from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("750x450")
window.title("MCA")
myframe=LabelFrame(window,text="Registration Form",bg='sky blue',fg='white',font=20)
myframe.pack()

mylabel1=Label(myframe,text="Name:")
mylabel1.grid(row=1,column=1,pady=20)
ent=Entry(myframe,width=30,borderwidth=5)
ent.grid(row=1,column=2)

mylabel2=Label(myframe,text="Father's Name:")
mylabel2.grid(row=2,column=1,pady=20)
ent=Entry(myframe,width=30,borderwidth=5)
ent.grid(row=2,column=2)

mylabel3=Label(myframe,text="DOB:")
mylabel3.grid(row=3,column=1,pady=20)
ent=Entry(myframe,width=30,borderwidth=5)
ent.grid(row=3,column=2)

mylabel4=Label(myframe,text="RollNo.:")
mylabel4.grid(row=4,column=1,pady=20)
ent=Entry(myframe,width=30,borderwidth=5)
ent.grid(row=4,column=2)

mylabel5=Label(myframe,text="Branch:")
mylabel5.grid(row=5,column=1,pady=20)
ent=Entry(myframe,width=30,borderwidth=5)
ent.grid(row=5,column=2)

mylabel6=Label(myframe,text="Address:")
mylabel6.grid(row=6,column=1,pady=20)
txt=Text(myframe,width=30,height=5,borderwidth=5)
txt.grid(row=6,column=2)

def click():
    x=ent.get()
    mylabel=Label(myframe,text="Successful"+x)
    ent.delete(0,END)
    messagebox.showinfo("information","Successfully Registered")
mybutton=Button(myframe,text="submit",padx=30,command=click)
mybutton.grid(row=7,column=3)

mybutton1 = Button(myframe, text="Fill Again",padx=30, command=click)
mybutton1.grid(row=7, column=2)

window.mainloop()