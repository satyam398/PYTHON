#DIGITALCLOCK
from tkinter import*
from time import strftime
root=Tk()
root.title("DIGITAL CLOCK")

def clk():
    res=strftime('%d-%B-%Y %A %H:%M:%S')
    x.config(text=res)
    x.after(1000,clk)

x=Label(root,bg="black",fg="cyan",font="Arial 50")
x.pack()
clk()

root.mainloop()
