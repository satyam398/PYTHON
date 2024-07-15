#
from tkinter import *
root=Tk()
root.geometry('500x300')

def f1():
    root.destroy()
    import firm
    
def f2():
    root.destroy()
    import firm1
    
def f3():
    root.destroy()
    import firm2
    
def f4():
    root.destroy()
    import firm3
    
def f5():
    root.destroy()
    import firm4
    
def f6():
    root.destroy()
    import firm5
    
def f7():
    root.destroy()
    import firm6
    
def f8():
    root.destroy()
    import firm7
    

    
    
Button(root,text="calculator",fg="cyan",font="Arial 20",command=f1).grid(row=0,column=0)
Button(root,text="digital clock",fg="blue",font="Arial 20",command=f2).grid(row=0,column=1)
Button(root,text="Text to speech",fg="orange",font="Arial 20",command=f3).grid(row=1,column=0)
Button(root,text="youtube download",fg="red",font="Arial 20",command=f4).grid(row=1,column=1)
Button(root,text="Text converter",fg="green",font="Arial 20",command=f5).grid(row=2,column=0)
Button(root,text="Text count",fg="black",font="Arial 20",command=f6).grid(row=2,column=1)
Button(root,text="Spelling checker",fg="sky blue",font="Arial 20",command=f7).grid(row=3,column=0)
Button(root,text="BMI calulator",fg="light green",font="Arial 20",command=f8).grid(row=3,column=1)

root.mainloop()
