from pytube import YouTube 
import os
import re
import requests as req
import wget
from PIL import ImageTk,Image
# from tkinter import *
from tkinter import Label, messagebox,filedialog,Toplevel,Entry,Button,Tk,END


def Yt_Downloader():
    window1=Toplevel()
    window1.geometry("700x600")
    window1.title("Youtube_Downloader")
    window1.config(bg="black")
    window1.resizable(False,False) 

    img=Image.open("logo/yt.jpg")
    resize_img=img.resize((250,200))
    logo=ImageTk.PhotoImage(resize_img)

    label1=Label(window1,image=logo)
    label1.place(x=200,y=10)

    lab1=Label(window1,text="Url:",bg="black",fg="white",font=("itallic",15,"bold"))
    lab1.place(x=30,y=250)

    inps=Entry(window1,bd=4,width=100)
    inps.config(width=50)
    inps.place(x=90,y=250)

    label=Label(window1,text="Save_as:",fg="white",bg="black",font=("itallic",15,"bold"))
    label.place(x=30,y=300)

    name=Entry(window1,bd=4)
    name.place(x=150,y=300)

    def clear():
        inps.delete(0,END)
        name.delete(0,END)

    def Yt_Vdownloader():
        try:
            url=inps.get()
            get_name=name.get()+".mp3"
            if url=="":
                messagebox.showwarning("fill up url","NUll url  ")
            else:
                btn1.configure(state="disable",text="Downloading..")
                dir=filedialog.askdirectory()
                
                yt=YouTube(url)
                video=yt.streams.get_highest_resolution()
                
                video.download(output_path=dir,filename=get_name)
                messagebox.showinfo("Completed","200 ok video downloaded")
                clear()
                btn1.configure(state="active",text="Download_video")

        except:
            messagebox.showerror("Invalid Url","404 video not found")

    btn1=Button(window1,bd=4,text="Download_video",command=lambda:Yt_Vdownloader(),fg="white",bg="black",activebackground="navy",width=15)
                
    btn1.place(x=145,y=400)

    def Yt_Adownloader():

        try:
            url=inps.get()
            get_name=name.get()+".mp3"
            print(get_name)
            print(url)
            if url=="":
                messagebox.showwarning("fill up url","Null url")
            else:
                btn2.configure(state="disable",text="Downloading..")
                dir=filedialog.askdirectory()
                yt=YouTube(url)
                yt.streams.get_audio_only().download(output_path=dir,filename=get_name)
                messagebox.showinfo("Completed","200 ok audio downloaded")
                clear()
                btn2.configure(state="active",text="Download_audio")


        except:
            messagebox.showerror("Invalid Url","404 audio not found")


    btn2=Button(window1,text="Download_audio",bd=4,command=lambda:Yt_Adownloader(),fg="white",bg="black",activebackground="navy",width=15)
    btn2.place(x=145,y=450)
  
    window1.mainloop()

            
    

def Fb_Downloader():
    window1=Toplevel()
    window1.geometry("600x500")
    window1.title("Facebook_VDownloader")
    window1.config(bg="thistle2")
    window1.resizable(False,False)

    imgs=Image.open("logo/facebook.png")
    resize_img1=imgs.resize((200,150))
    logo=ImageTk.PhotoImage(resize_img1)

    labe=Label(window1,image=logo)

    labe.place(x=200,y=10)

    lab1=Label(window1,text="Url:",font=("arial",15))
    lab1.place(x=20,y=300)

    inps=Entry(window1,bd=4,width=100)
    inps.config(width=50)
    inps.place(x=70,y=300)

    d_btn=Button(window1,text="Download",command=lambda:Downloader(),fg="white",bg="black",activebackground="navy",width=15,bd=4)
    d_btn.place(x=90,y=350)

    def clear():
        inps.delete(0,END)

    def Downloader():
        try:
            url=inps.get()
            if url=="":
                messagebox.showerror("Error","Null url")
            else:
                html=req.get(url)
                v_url=re.search('hd_src:"(.+?)"',html.text)[1]
                d_btn.configure(state="disable",text="Downloading..")
                dir=filedialog.askdirectory()
                a_url=v_url.replace('hd_src:"','')
                video=wget.download(a_url,out=dir)
                messagebox.showinfo("Downloaded","200 ok Video Downloaded")
                clear()
                d_btn.configure(state="active",text="Download")
        except req.ConnectionError as e:
            messagebox.showerror("Error","Network Connection Error")
        except req.Timeout as e:
            messagebox.showerror("Time_out","Request timeout")
        except req.HTTPError as e:
            messagebox.showerror("Http error","404 not found")

    window1.mainloop()

    
    


