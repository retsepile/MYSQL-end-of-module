# RETSEPIILE KOLOKO , CLASS2
#   !!!!!!!!!!!! #
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
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

def admin1(event):
    window.destroy()
    import admin


class MainScreen:

    def __init__(self):
        self.window = window
        self.login = Button(window, text="LOGIN", borderwidth=25, bg="lime", command=self.login)
        self.login.place(x=10, y=250)
        self.register = Button(window, text="REGISTER NEW USER", borderwidth=25, bg="lime", command=self.register)
        self.register.place(x=200, y=250)
        self.admin = Button(window, text="ADMINISTRATION", command=self.admin2, bg="lime", borderwidth=25)
        self.admin.place(x=500, y=250)
        self.exit = Button(window, text="EXIT", command=self.exit, bg="lime", borderwidth=25)
        self.exit.place(x=750, y=250)

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

    def admin2(self):
        messagebox.showinfo("Status", "You can access the admin page by pressing Control + a ")
        self.window.destroy()
        import admin

    def exit(self):
        self.ask = messagebox.askquestion("QUIT APPLICATION", "Do you really want to leave the page?")
        if self.ask == "yes":
            self.window.destroy()
window.bind("<Control-a>", admin1)
i = MainScreen()
window.mainloop()
