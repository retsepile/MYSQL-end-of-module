from tkinter import *
import mysql.connector
from tkinter import messagebox
window = Tk()
window.geometry("500x500")
window.title("LOGIN INFO")
window.config(bg="lime")


class LogIn:
    def __init__(self):
        self.window = window
        self.username = Label(window, text="Enter your username:")
        self.username.place(x=0, y=0)
        self.entry_user = Entry(window)
        self.entry_user.place(x=150, y=0)
        self.password = Label(window, text="Enter your password:")
        self.password.place(x=0, y=100)
        self.entry_password = Entry(window)
        self.entry_password.place(x=150, y=100)
        self.button = Button(window, text="Login", command=self.connect)
        self.button.place(x=0, y=200)
        self.return_btn = Button(window, text="Return", command=self.back)
        self.return_btn.place(x=100, y=200)

    def connect(self):
        self.username = self.entry_user.get()
        self.password = self.entry_password.get()
        if self.username == "" or self.password == "":
            messagebox.showinfo("Error", "Invalid characters inserted!!!")
        else:
            self.mysql = mysql.connector.connect(user='sql6423546',
                                                 password='AQ15mTbUCB',
                                                 host='sql6.freesqldatabase.com',
                                                 database='sql6423546',
                                                 auth_plugin='mysql_native_password',
                                                 port='3306')
            mycursor = self.mysql.cursor()
            mycursor = mycursor.execute('Select * from users('+self.username+', '+self.password+')')
            mycursor.execute("commit")

            messagebox.showinfo("Access Granted", "Login successful")

    def back(self):
        self.window.destroy()
        import main_screen


x = LogIn()
window.mainloop()
