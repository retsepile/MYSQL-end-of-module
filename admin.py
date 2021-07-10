from tkinter import *
import mysql.connector
from tkinter import messagebox
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
        self.login = Button(window, text="LOGIN", command=self.login)
        self.login.place(x=0, y=200)

    def submit(self):

        self.username = self.name.get()
        self.password = self.code.get()

        print(f"The name entered by you is {self.username} {self.password}")

    def login(self):
        self.password = self.password
        self.username = self.name

        # If password is entered by the
        # user
        if self.password:
            mydb = mysql.connector.connect(user='Lifechoices',
                                         password='@Lifechoices1234',
                                         host='127.0.0.1',
                                         database='lifechoicesonline',
                                         auth_plugin='mysql_native_password',)
            mycursor = mydb.cursor()

        elif self.username:
            mydb = mysql.connector.connect(user='Lifechoices',
                                           password='@Lifechoices1234',
                                           host='127.0.0.1',
                                           database='lifechoicesonline',
                                           auth_plugin='mysql_native_password', )
            mycursor = mydb.cursor()

        # If no password is entered by the
        # user
        else:
            mydb = mysql.connector.connect(user='Lifechoices',
                                                 password='@Lifechoices',
                                                 host='127.0.0.1',
                                                 database='lifechoicesonline',
                                                 auth_plugin='mysql_native_password',)
            mycursor = mydb.cursor()

        # A Table in the database
        query = ("SELECT * from admin WHERE username = username AND password = password")
        val = (self.name.get(), self.code.get())

        try:
            mycursor.execute(query)
            mycursor = mycursor.fetchall()

            # Printing the result of the
            # query
            messagebox.showinfo("Status", "Query Executed successfully")
            window.destroy()
            import admin_second


        except mysql.connector.Error as err:
            messagebox.showinfo("ERROR", "Error occurred" + str(err))



x = AdminLogin()
window.mainloop()
