#YOUTUBE DOWNLOADER
from tkinter import*
from pytube import YouTube
from tkinter import messagebox
root=Tk()
root.geometry('500x300')

def f1():
    video_url=txt.get()
    try:
        yt=Youtube(video_url)
        stream=yt.streams.get_highest_resolution()
        stream.download()
        status_label.config(text="Download complete!")
    except :
        messagebox.showerror('error','wrong url')
    
txt=StringVar()
Label(root,text="YOUTUBE DOWNLOAD",bg="red",fg="white",font="Arial 30").pack(fill="x")
Label(root,text="Enter url",font="Arial 20").place(x=0,y=100)
Entry(root,textvariable=txt).place(x=110,y=110)
Button(root,text="Download",fg="white",bg="red",font="Arial 20").place(x=150,y=200)
root.mainloop()
