from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
window = Tk()
window.geometry("500x600")
window.title("Welcome to Life Choices")
window.geometry("900x900")
loader = Image.open("LIFE-CHOICES-ICON-ON-GREEN.jpeg")
render = ImageTk.PhotoImage(loader)
image = Label(window, image=render)
image.place(x=0, y=0)
loader2 = Image.open("Lifechoices-300x91.jpg")
render2 = ImageTk.PhotoImage(loader2)
image = Label(window, image=render2)
image.place(x=0, y=0)


class MainScreen:

    def __init__(self):
        self.window = window
        self.login = Button(window, text="LOGIN", borderwidth=25, bg="lime", command=self.login)
        self.login.place(x=10, y=250)
        self.register = Button(window, text="REGISTER NEW USER", borderwidth=25, bg="lime", command=self.register)
        self.register.place(x=300, y=250)

    def login(self):
        self.ask = messagebox.askquestion("LOGIN", "Proceed to login?")
        if self.ask == "yes":
            self.window.destroy()
            import login

    def register(self):
        self.ask = messagebox.askquestion("REGISTRATION", "Would you like to register?")
        if self.ask == "yes":
            self.window.destroy()
            import second_screen


    def connect(self):
        self.lifechoicesonline = mysql.connector.connect(user='Lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoicesonline', auth_plugin='mysql_native_password')
        mycursor = self.lifechoicesonline.cursor()
        xy = mycursor.execute('Select * from mytable')
        for i in mycursor:
            pass

i = MainScreen()
window.mainloop()
