import smtplib
from tkinter import Button, Label, LabelFrame, Tk, Toplevel,Entry,messagebox
from email import message
from tkinter.constants import END
from typing import Text
from PIL import Image,ImageTk
from email.message import EmailMessage

def email():
    window1=Toplevel()
    window1.geometry("800x700")
    window1.title("Send_mail")
    window1.configure(bg="black")
    img=Image.open("logo/email.png")
    resized_img=img.resize((200,150))
    logo=ImageTk.PhotoImage(resized_img)
    img_frame=Label(window1,image=logo)
    img_frame.place(x=230,y=20)
    lab1=Label(window1,text="Sender_address:",fg="white",bg="black")
    Sender_address=Entry(window1,bd=4,fg="black",bg="white")
    lab1.place(x=50,y=250)
    Sender_address.place(x=200,y=250)

    txt=Label(window1,text="(single/multiple)",fg="white",bg="black")
    txt.place(x=50,y=280)
    lab2=Label(window1,text="Receiver_address:",fg="white",bg="black")
    rec_address=Entry(window1,bd=4,fg="black",bg="white",width=30)
    lab2.place(x=50,y=300)
    rec_address.place(x=200,y=300)

    lab3=Label(window1,text="Subject:",fg="white",bg="black")
    sub=Entry(window1,bd=4,fg="black",bg="white",width=40)
    lab3.place(x=50,y=350)
    sub.place(x=200,y=350)

    lab4=Label(window1,text="Message_body:",fg="white",bg="black")
    body1=Entry(window1,bd=4,fg="black",bg="white",width=40)
    lab4.place(x=50,y=400)
    body1.place(x=200,y=400)    

    pas=Label(window1,text="Enter password :",fg="white",bg="black")
    pas.place(x=50,y=550)
    psw=Entry(window1,fg="black",bg="white",bd=4)
    psw.place(x=200,y=550)
    
    Send=Button(window1,text="Send",bd=4,activebackground="pink",command=lambda:send())
    Send.place(x=250,y=600)
    def clear():
        Sender_address.delete(0,END)
        rec_address.delete(0,END)
        sub.delete(0,END)
        body1.delete(0,END)
        psw.delete(0,END)
    

    def send(): 
        sender=Sender_address.get()
        reciver=rec_address.get()
        subject=sub.get()
        password=psw.get()
        body=body1.get()
        if password==''or sender=='' or reciver=='' or subject=='' or body=='':
            messagebox.showerror("Error","Field Null !!")
        else: 
            try:
                my_server =smtplib.SMTP("smtp.gmail.com",587)
                my_server.starttls()
                my_server.login(sender,password)
                email=EmailMessage()
                email['From']=sender
                email["Subject"]=subject
                email.set_content(body)
                lis=[x for x in reciver.split(",")]
                for i in lis:
                    email["To"]=i
                    print(i)
                    Send.configure(text="Sending",state='disable')
                    my_server.send_message(email)
                    
                    del email["To"]
                clear()
                Send.configure(text="send",state='normal')

            except smtplib.SMTPAuthenticationError as e:
                messagebox.showerror("Error",e)
                clear()
            except smtplib.SMTPConnectError as e1:
                messagebox.showerror("Error",e1)
                clear()
            except smtplib.SMTPConnectError as e2:
                messagebox.showerror("Error",e2)
                clear()

          
    window1.mainloop()







