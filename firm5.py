#TEXT COUNT
from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry('300x200')
def f1():
    res=tct.get()
    count=0
    for i in res:
        count+=1
    print(count)
    
tct=StringVar()

Label(root,text="TEXT COUNT",fg="orange",font="Arial 30",bg="yellow").pack(fill="x")
Label(root,text="Enter text",fg="red",font="Arial 20").place(x=50,y=50)
Entry(root,textvariable=tct).place(x=50,y=100)

Button(root,text="count",fg="black",bg="blue",font="Arial 20",command=f1).place(x=50,y=150)
      
root.mainloop()
