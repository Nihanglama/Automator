import pyttsx3 as p
import PyPDF2 as pd
from tkinter import Button, Canvas, Entry, Label,END, messagebox, READABLE,filedialog,Toplevel
from PIL import Image,ImageTk

def Reader():

    window1=Toplevel()
    window1.geometry("900x800")
    window1.title("Reader")
    window1.resizable(False,False)
    canvas=Canvas(window1,width=700,height=600)
    canvas.pack(fill="both",expand=True)
    img=Image.open("logo/bg.jpg")
    logo=img.resize((900,800))
    bg=ImageTk.PhotoImage(logo)
    canvas.create_image(0,0,image=bg,anchor='nw')
    btn=Button(window1,text="OpenPdf",bd=4,command=lambda:open())
    canvas.create_window(700,200,window=btn,anchor='w')

    def open():
        try:
            file=filedialog.askopenfilename(title="CHOSSE FILE")
            if file=='':
                messagebox.showwarning(" NO file",'File not selected')
            else:
                lab=Label(window1,text="File Name: ",fg="black",bg='green',font=("arial",15,'bold'))
                name=Label(window1,text=file,bd=4)
                canvas.create_window(500,250,window=lab,anchor='w')
                canvas.create_window(650,250,window=name,anchor='w')
                scan=pd.PdfFileReader(file)
                num=scan.getNumPages()
                lab1=Label(window1,text="N0.PAGES:",fg="black",bg='green',font=("arial",15,'bold'))
                pages=Label(window1,bd=4,text=num)
                canvas.create_window(500,300,window=lab1,anchor='w')
                canvas.create_window(650,300,window=pages,anchor='w')
                lab2=Label(window1,text="StartingPage:",fg="black",bg='green',font=("arial",15,'bold'))
                get_page=Entry(window1,bd=3) 

                canvas.create_window(500,350,window=lab2,anchor='w')  
                canvas.create_window(650,350,window=get_page,anchor='w')

                # num1=get_page.get()
                # int_num=int(num1)
                get_page= scan.getPage(2)
        
                words=get_page.extractText()
                btn1=Button(window1,text="Read",bd=3,command=lambda:speak(words))
                canvas.create_window(700,400,window=btn1,anchor='w')
        except FileNotFoundError as e:
            messagebox.showerror("no file","404 file not found")
        except PermissionError as e:
            messagebox.showerror('permission denied',e)
            

    def speak(words):
        robot=p.init()

        rate=robot.getProperty('rate')

        robot.setProperty("rate",rate+10)

        robot.say(words)


        robot.runAndWait()


   





    window1.mainloop()

