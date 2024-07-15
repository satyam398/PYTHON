#BMI CALCULATOR
from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry('400x300')

def f1():
    try:
      weight=float(bt.get())
      height=float(ht.get())
      bmi=weight/(height**2)
      if bmi<18.5:
          messagebox.showinfo('info','underweight')
      elif bmi>=18.5 or bmi<24.9:
          messagebox.showinfo('info','normal')
      elif bmi>=24.9 or bmi<29.9:
          messagebox.showinfo('info','overweight')
      else:
           messagebox.showinfo('info','obesity')
    except ValueError:
           messagebox.showerror('error','enter valid')

def f2():
    ht.set("")
    bt.set("")

ht=StringVar()
bt=StringVar()

Label(root,text="BMI CALCULATOR",bg="light green",fg="blue",font="Arial 30").pack(fill="x")
Label(root,text="enter height(in m)",font="Arial 15").place(x=0,y=60)
Entry(root,textvariable=ht).place(x=170,y=65)
Label(root,text="enter weight(in kg)",font="Arial 15").place(x=0,y=110)
Entry(root,textvariable=bt).place(x=170,y=115)
Button(root,text="result",font="Arial 15",command=f1).place(x=100,y=200)
Button(root,text="clear",font="Arial 15",command=f2).place(x=200,y=200)

root.mainloop()
