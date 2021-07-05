from tkinter import *
import mysql.connector
window = Tk()
window.geometry("500x500")
window.title("LOGIN INFO")
window.config(bg="lime")


class LogIn:
    def __init__(self):
        self.username = Label(window, text="Enter your name:")
        self.username.place(x=0, y=0)
        self.entry_user = Entry(window)
        self.entry_user.place(x=150, y=0)
        self.password = Label(window, text="Enter password:")
        self.password.place(x=0, y=100)
        self.entry_password = Entry(window)
        self.entry_password.place(x=150, y=100)

    def connect(self):
        self.lifechoicesonline = mysql.connector.connect(user='Lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoicesonline', auth_plugin='mysql_native_password')
        mycursor = self.lifechoicesonline.cursor()
        xy = mycursor.execute('Select * from mytable')
        for i in mycursor:
            pass
x = LogIn()
window.mainloop()
