import tkinter as tk
from typing import Text
from reader import Reader
from mail import email
from downloader import Yt_Downloader,Fb_Downloader
from tkinter import Canvas, Label, Menu,ttk
from PIL import ImageTk,Image



window=tk.Tk()
window.geometry('1000x900')
window.title("Automation")
window.resizable(False,False)
window.config(bg="turquoise1",bd=5)

menubar=Menu(window,bg="alice blue")

downlo=Menu(menubar,tearoff=0)
downlo.add_command(label="Youtube_video",foreground="black",command=lambda:Yt_Downloader(),font=("arial",15,"bold"),activebackground="deep sky blue")
downlo.add_separator()
downlo.add_command(label="Facebook_video",foreground="black",command=lambda:Fb_Downloader(),font=("arial",15,"bold"),activebackground="deep sky blue")
downlo.config(bd=3)

menubar.add_cascade(label="Downloader",menu=downlo,foreground="black",font=("arial",15,"bold"),activebackground="deep sky blue")

menubar.add_command(label="PDF reader",foreground="black",command=lambda:Reader(),font=("arial",15,"bold"),activebackground="deep sky blue")
menubar.add_command(label="send_mail",foreground="black",command=lambda:email(),font=("arial",15,"bold"),activebackground="deep sky blue")
menubar.add_separator()
menubar.config(bd=5)
canvas=Canvas(window,width=1000,height=900)
canvas.pack(fill='both',expand=True)
img=Image.open("logo/mainbg.png")
logo=img.resize((1000,900))
bg=ImageTk.PhotoImage(logo)
canvas.create_image(0,0,image=bg,anchor='nw')
texts=Label(window,text="Automator",font=("Itallic",30,'bold'),fg="red",bg="peachpuff2")
canvas.create_window(500,800,window=texts)


window.config(menu=menubar)



window.mainloop()