from PIL import ImageTk
from tkinter import *
import mysql.connector

from tkinter import messagebox


def sign_in():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Enter all fields')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='asad23', database='customerdata')
            cur = con.cursor()
        except:
            messagebox.showerror('Error', 'Error in database connection')
            return

        cur.execute('select *from data where username=%s and password=%s', (usernameEntry.get(), passwordEntry.get()))
        row = cur.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username password')
        else:
            messagebox.showinfo('Success', 'Login Successfully')


window = Tk()
window.title("Signin page")
window.geometry('925x500+300+200')
background = ImageTk.PhotoImage(file="C:\Users\DELL\Desktop\download.jpeg")
backgroundLabel = Label(window, image=background, )
window.resizable(False, False)
backgroundLabel.grid()
frame = Frame(window)
frame.place(x=500, y=350)
heading = Label(frame, text="Signup", font=('Microsoft YaHei UI Light', 18, 'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)
usernamelabel = Label(frame, text='Username', font=('Arial ', 10, 'bold'), bg='white', fg='firebrick1')
usernamelabel.grid(row=1, column=0, padx=10, pady=10, sticky='W')
usernameEntry = Entry(frame, width=20)
usernameEntry.grid(row=1, column=0, padx=10)
passwordlabel = Label(frame, text='Password', font=('Arial ', 10, 'bold'), bg='white', fg='firebrick1')
passwordlabel.grid(row=3, column=0, padx=10, pady=10, sticky='W')
passwordEntry = Entry(frame, width=20)
passwordEntry.grid(row=3, column=0, padx=10, pady=10)
signinbutton = Button(frame, text='Sign in', font=('Arial', 14, 'bold'), fg='firebrick1', command=sign_in)
signinbutton.grid(row=5, column=0, padx=10, pady=10)

window.mainloop()
