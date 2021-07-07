from tkinter import *
import mysql.connector
window = Tk()
window.geometry("500x500")


class AdminLogin:
    def __init__(self):
        self.username = Label(window, text="USERNAME:")
        self.username.place(x=0, y=0)
        self.name = Entry(window)
        self.name.place(x=100, y=0)
        self.password = Label(window, text="PASSWORD:")
        self.password.place(x=0, y=100)
        self.code = Entry(window)
        self.code.place(x=100, y=100)
        self.login = Button(window, text="LOGIN")
        self.login.place(x=0, y=200)

    def submit(self):

        self.username = self.name.get()
        self.password = self.code.get()

        print(f"The name entered by you is {self.username} {self.password}")

    def login(self, fullname, password):

        # If password is entered by the
        # user
        if password:
            mydb = mysql.connector.connect(user='sql6423546',
                                         password='AQ15mTbUCB',
                                         host='sql6.freesqldatabase.com',
                                         database='sql6423546',
                                         auth_plugin='mysql_native_password',
                                         port='3306')
            mycursor = mydb.cursor()

        # If no password is entered by the
        # user
        else:
            mydb = mysql.connector.connect(user='sql6423546',
                                                 password='AQ15mTbUCB',
                                                 host='sql6.freesqldatabase.com',
                                                 database='sql6423546',
                                                 auth_plugin='mysql_native_password',
                                                 port='3306')
            mycursor = mydb.cursor()

        # A Table in the database
        savequery = "select * from user"

        try:
            mycursor.execute(savequery)
            mycursor = mycursor.fetchall()

            # Printing the result of the
            # query
            for x in mycursor:
                print(x)
            print("Query Executed successfully")

        except:
            mydb.rollback()
            print("Error occurred")


x = AdminLogin()
window.mainloop()
