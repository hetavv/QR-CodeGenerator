from tkinter import *
from tkinter import messagebox,Toplevel
import pyqrcode
import os
import png
root = Tk()
root.geometry('600x450')
root.title('QR CODE GENERATOR')
root.iconbitmap('logo.ico')
root.configure(bg='#B8DBEB')

def Generate_QR():
    QR_ID = QR_ID_Entry_Box.get()
    QR_NAME = QR_Name_Entry_Box.get()
    QR_URL = QR_URL_Entry_Box.get()

    File_name = 'NAME: '+QR_NAME+'\n'+'ID: '+QR_ID+'\n'+'QR_URL: '+QR_URL
    #print(Message)
    url = pyqrcode.create(File_name)
    path=r'C:\Users\HP\Desktop\QR_CODES'
    cc ='{}\{}{}.png'.format(path,QR_ID,QR_NAME)
    ll = os.listdir(path)
    if('{}{}.png'.format(QR_ID,QR_NAME) in ll ):
        messagebox.showinfo('Notification','PLease choose another ID and NAME')
    else:
        url.png(cc, scale=8)
        tempmsg = 'QR CODE GENERATED!'
        QR_Notification_message_label.configure(text=tempmsg)
        output = messagebox.askyesno('Notification','QR CODE SUCCESSFULLY GENERATED! If you want to see it YES : ')
        if(output==True):
            top =Toplevel()
            top.geometry('400x400')
            top.configure(bg='white')
            img = PhotoImage(file=cc)
            label1 = Label(top,image=img,bg='white')
            label1.place(x=10,y=10)
            top.mainloop()




def clear_program():
    QR_ID_Entry_Box.delete(0,'end')
    QR_Name_Entry_Box.delete(0,'end')
    QR_URL_Entry_Box.delete(0,'end')
    QR_Notification_message_label.configure(text='')




def quit_program():
    res = messagebox.askokcancel('Notification','Are you sure you want to quit? ')
    if(res==True):
        root.destroy()
    else:
        pass


#labels
QR_ID_Label = Label(master=root, text = 'Enter the ID', bg= '#5199B4',width=20,height=2, font=('arial',12,'bold'))
QR_ID_Label.place(x=10, y=20)

QR_Name_Label = Label(master=root, text = 'Enter the name ', bg= '#5199B4',width=20,height=2, font=('arial',12,'bold'))
QR_Name_Label.place(x=10, y=80)

QR_URL_Label = Label(master=root, text = 'Enter the URL or Text ', bg= '#5199B4',width=20,height=2, font=('arial',12,'bold'))
QR_URL_Label.place(x=10, y=140)

QR_Notification_label = Label(master=root, text = 'Status ', bg= '#5199B4',width=20,height=2, font=('arial',12,'bold'))
QR_Notification_label.place(x=10,y=370)

QR_Notification_message_label = Label(master=root,width=20,bd = 2,bg = '#96C9E6', font=('arial',18,'bold'))
QR_Notification_message_label.place(x=250,y=370)

#entry boxes
QR_ID_Entry_Box = Entry(master=root,width=20,bd = 2,bg = '#96C9E6', font=('arial',20,'bold'))
QR_ID_Entry_Box.place(x=250,y=20)

QR_Name_Entry_Box = Entry(master=root,width=20,bd = 2,bg = '#96C9E6', font=('arial',20,'bold'))
QR_Name_Entry_Box.place(x=250,y=80)

QR_URL_Entry_Box = Entry(master=root,width=20,bd = 2,bg = '#96C9E6', font=('arial',20,'bold'))
QR_URL_Entry_Box.place(x=250,y=140)

Generate_Image =PhotoImage(file='qr-code-scan.png')
Generate_Image = Generate_Image.subsample(2,2)

eraser_Image =PhotoImage(file='eraser.png')
eraser_Image = eraser_Image.subsample(2,2)

exit_Image =PhotoImage(file='exit.png')
exit_Image = exit_Image.subsample(2,2)

#buttons

Generate_QR_button = Button(master=root, text ='Generate QR', width= 140, font=('arial',12,'bold'), bd=5, activebackground='#F7E89B', image=Generate_Image, compound=RIGHT,command=Generate_QR)
Generate_QR_button.place(x=10, y=250)

Clear_button = Button(master=root, text ='Clear', width= 100, font=('arial',12,'bold'), bd=5, activebackground='#F7E89B', image=eraser_Image, compound=RIGHT, command=clear_program)
Clear_button.place(x=250, y=250)

Quit_button = Button(master=root, text ='Exit', width=100, font=('arial',12,'bold'), bd=5, activebackground='#F7E89B', image=exit_Image, compound=RIGHT,command=quit_program)
Quit_button.place(x=460, y=250)

def Generate_QR_buttonEnter(e):
    Generate_QR_button['bg'] = '#8C7D99'
def Generate_QR_buttonLeave(e):
    Generate_QR_button['bg'] = '#F7E89B'

def Clear_buttonEnter(e):
    Clear_button['bg'] = '#8C7D99'
def Clear_buttonLeave(e):
    Clear_button['bg'] = '#F7E89B'

def Quit_buttonEnter(e):
    Quit_button['bg'] = '#8C7D99'
def Quit_buttonLeave(e):
    Quit_button['bg'] = '#F7E89B'


Generate_QR_button.bind('<Enter>',Generate_QR_buttonEnter)
Generate_QR_button.bind('<Leave>',Generate_QR_buttonLeave)

Clear_button.bind('<Enter>',Clear_buttonEnter)
Clear_button.bind('<Leave>',Clear_buttonLeave)

Quit_button.bind('<Enter>',Quit_buttonEnter)
Quit_button.bind('<Leave>',Quit_buttonLeave)

root.mainloop()
