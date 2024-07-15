#

from tkinter import*
from tkinter import messagebox
import sqlite3
root=Tk()
root.geometry('500x400')


x=sqlite3.connect('ddd1.db')
sql="create table if not exists reg(Name varchar(28),Email varchar(50),Password varchar(10))"
x.execute(sql)

def f3():
    if pw.get()==cpw.get():
       sq="insert into reg(Name,Email,Password) values(?,?,?)"
       data=(nm.get(),em.get(),pw.get())
       x.execute(sq,data)
       x.commit()
       x.close()
       messagebox.showinfo('success',"succ regi")
       import fiillee
       nm.set("")
       em.set("")
       pw.set("")
       cpw.set("")

    else:
         messagebox.showerror('error',"password not matched")

nm=StringVar()
em=StringVar()
pw=StringVar()
cpw=StringVar()

Label(root,text="Register Form",fg="orange",font="Arial 40 bold").place(x=100,y=0)

Label(root,text="Name",font="Arial 16").place(x=0,y=100)
Entry(root,textvariable=nm).place(x=200,y=100)

Label(root,text="Email",font="Arial 16").place(x=0,y=140)
Entry(root,textvariable=em).place(x=200,y=140)

Label(root,text="Passwod",font="Arial 16").place(x=0,y=180)
Entry(root,textvariable=pw).place(x=200,y=180)

Label(root,text="Confirm Password",font="Arial 16").place(x=0,y=220)
Entry(root,textvariable=cpw).place(x=200,y=220)

Button(root,text="Submit",bg="orange",font="Arial 20",command=f3).place(x=180,y=280) 
       
