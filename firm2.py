#TEXT TO SPEECH
from tkinter import*
import pyttsx3
root=Tk()
root.geometry('300x200')
def f1():
    text=tx.get()
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    tx.set("")

tx=StringVar()    
Label(root,text="Text to Speech",fg="cyan",font="Arial 30",bg="yellow").pack()
Label(root,text="Enter text",fg="orange",font="Arial 20").place(x=80,y=50)
Entry(root,textvariable=tx).place(x=80,y=100)
Button(root,text="Speak",command=f1,font="Arial 15").place(x=100,y=150)
root.mainloop()
