#SPELLING CHECKER
from tkinter import*
from textblob import TextBlob
root=Tk()
root.geometry('400x200')

def cor():
    text=clr.get()
    blob=TextBlob(text)
    corrected_text=blob.correct()
    x=str(corrected_text)
    res.set(x)
    
def c1():
    clr.set("")
    res.set("")


clr=StringVar()
res=StringVar()

Label(root,text="SPELLING CHECKER",font="Arial 30",fg="orange",bg="yellow").pack()
Label(root,text="Enter text",font="Arial 18").place(x=0,y=50)
Entry(root,textvariable=clr).place(x=120,y=60)
Label(root,text="result",font="Arial 18").place(x=0,y=100)
Entry(root,textvariable=res).place(x=120,y=110)
Button(root,text="check",fg="Red",font="Arial 20",command=cor).place(x=50,y=150)
Button(root,text="clear",fg="Red",font="Arial 20",command=c1).place(x=200,y=150)
root.mainloop()
