#CALCULATOR
from tkinter import*
root=Tk()
root.geometry('125x175')
root.config(bg="cyan")

def f1(n):
    global data
    data=data+n
    da.set(data)

def clr():
    global data
    data=""
    da.set(data)
    
def eql():
    global data
    x=da.get()
    data=str(eval(x))
    da.set(data)
    

data=""
da=StringVar()

Entry(root,textvariable=da).grid(row=0,columnspan=4) 

Button(root,text="7",bg="orange",font="Arial 15",command=lambda:f1('7')).grid(row=1,column=0)
Button(root,text="8",bg="orange",font="Arial 15",command=lambda:f1('8')).grid(row=1,column=1)
Button(root,text="9",bg="orange",font="Arial 15",command=lambda:f1('9')).grid(row=1,column=2)
Button(root,text="+",bg="orange",font="Arial 15",command=lambda:f1('+')).grid(row=1,column=3)

Button(root,text="4",bg="orange",font="Arial 15",command=lambda:f1('4')).grid(row=2,column=0)
Button(root,text="5",bg="orange",font="Arial 15",command=lambda:f1('5')).grid(row=2,column=1)
Button(root,text="6",bg="orange",font="Arial 15",command=lambda:f1('6')).grid(row=2,column=2)
Button(root,text="-",bg="orange",font="Arial 15",command=lambda:f1('-')).grid(row=2,column=3)

Button(root,text="1",bg="orange",font="Arial 15",command=lambda:f1('1')).grid(row=3,column=0)
Button(root,text="2",bg="orange",font="Arial 15",command=lambda:f1('2')).grid(row=3,column=1)
Button(root,text="3",bg="orange",font="Arial 15",command=lambda:f1('3')).grid(row=3,column=2)
Button(root,text="*",bg="orange",font="Arial 15",command=lambda:f1('*')).grid(row=3,column=3)

Button(root,text="c",bg="orange",font="Arial 15",command=clr).grid(row=4,column=0)
Button(root,text="0",bg="orange",font="Arial 15",command=lambda:f1('0')).grid(row=4,column=1)
Button(root,text="=",bg="orange",font="Arial 15",command=eql).grid(row=4,column=2)
Button(root,text="/",bg="orange",font="Arial 15",command=lambda:f1('/')).grid(row=4,column=3) 

root.mainloop()
