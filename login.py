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
        self.full_name = Label(window, text="Enter your username:")
        self.full_name.place(x=0, y=0)
        self.entry_user = Entry(window)
        self.entry_user.place(x=150, y=0)
        self.password = Label(window, text="Enter your password:")
        self.password.place(x=0, y=100)
        self.entry_password = Entry(window)
        self.entry_password.place(x=150, y=100)
        self.button = Button(window, text="Login", command=self.login)
        self.button.place(x=0, y=200)
        self.return_btn = Button(window, text="Return", command=self.back)
        self.return_btn.place(x=100, y=200)

    def login(self):
        self.password = self.password
        self.full_name = self.full_name

        # If password is entered by the
        # user
        if self.password:
            mydb = mysql.connector.connect(user='Lifechoices',
                                         password='@Lifechoices1234',
                                         host='127.0.0.1',
                                         database='lifechoicesonline',
                                         auth_plugin='mysql_native_password',)
            mycursor = mydb.cursor()

        elif self.full_name:
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
        query = ("SELECT * from users WHERE full_name = full_name AND password = password")
        val = (self.entry_user.get(), self.entry_password.get())

        try:
            mycursor.execute(query)
            mycursor = mycursor.fetchall()

            # Printing the result of the
            # query
            messagebox.showinfo("Status", "Query Executed successfully")
            window.destroy()
            import admin_page


        except mysql.connector.Error as err:
            messagebox.showinfo("ERROR", "Error occurred" + str(err))

    def back(self):
        self.window.destroy()
        import main_screen


x = LogIn()
window.mainloop()
