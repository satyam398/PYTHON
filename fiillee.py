#LOGIN FORM
from tkinter import*
from tkinter import messagebox
import sqlite3
root=Tk()
root.geometry('300x300')

x=sqlite3.connect('ddd1.db')
sql="select *from reg "
res=x.execute(sql)

def f1():
    x=0
    for i in res:
     if i[1]==EM.get() and i[2]==PA.get():
         x+=1
    if x==1:
        messagebox.showinfo('info','sucess')
        root.destroy()
        import fi4
    else:
        messagebox.showerror('error','not valid')
     
EM=StringVar()
PA=StringVar()

Label(root,text="Login",font="Arial 30",fg="red").pack()

Label(root,text="Email",font="Arial 18").place(x=0,y=100)
Entry(root,textvariable=EM).place(x=150,y=100)

Label(root,text="Password",font="Arial 18").place(x=0,y=150)
Entry(root,textvariable=PA).place(x=150,y=150)

Button(root,text="Submit",font="Arial 20",fg="black",command=f1).place(x=100,y=200)

root.mainloop()
              
