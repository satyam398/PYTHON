from tkinter import*
root=Tk()
root.geometry('400x300')

def up():
    x=ent.get().upper()
    res.set(x)
    
def lw():
    x=ent.get().lower()
    res.set(x)
    
def tl():
    x=ent.get().title()
    res.set(x)
def sw():
    x=ent.get().swapcase()
    res.set(x)
    
def cq():
    x=ent.get().capitalize()
    res.set(x)
    
def cl():
   x=ent.set("")
   res.set("")  

ent=StringVar()
res=StringVar()
Label(root,text="Text case convert",font="Arial 20").place(x=100,y=50)

Label(root,text="Enter your text",fg="orange",font="Arial 12").place(x=50,y=80)
Entry(root,textvariable=ent).place(x=50,y=100)

Label(root,text="Result",fg="orange",font="Arial 12").place(x=50,y=120)
Entry(root,textvariable=res).place(x=50,y=140)

Button(root,text="Convert to uppercase",bg="orange",command=up).place(x=30,y=170)
Button(root,text="Convert to lowercase",bg="orange",command=lw).place(x=155,y=170)
Button(root,text="Convert to title case",bg="orange",command=tl).place(x=280,y=170)
Button(root,text="Convert to swap case",bg="orange",command=sw).place(x=30,y=200)
Button(root,text="Convert to capitalize",bg="orange",command=cq).place(x=155,y=200)
Button(root,text="clear",bg="orange",command=cl).place(x=280,y=200)

root.mainloop()
    
