from tkinter import *
window = Tk()
window.geometry("500x600")
window.title("REGISTER")
window.config(bg="black")


class RegiSter:
    def __init__(self):
        self.name = Label(window, text="Name:")
        self.name.place(x=10, y=50)
        self.name_entry = Entry(window)
        self.name_entry.place(x=150, y=50)
        self.surname = Label(window, text="Surname:")
        self.surname.place(x=10, y=100)
        self.surname_entry = Entry(window)
        self.surname_entry.place(x=150, y=100)
        self.identity = Label(window, text="ID NO:")
        self.identity.place(x=10, y=150)
        self.identity_entry = Entry(window)
        self.identity_entry.place(x=150, y=150)
        self.number = Label(window, text="Cellphone number:")
        self.number.place(x=10, y=200)
        self.cell_entry = Entry(window)
        self.cell_entry.place(x=200, y=200)
        self.kin = Label(window, text="Next of Kin's Name:")
        self.kin.place(x=10, y=250)
        self.next_entry = Entry(window)
        self.next_entry.place(x=200, y=250)
        self.kin_no = Label(window, text="Next of Kin number:")
        self.kin_no.place(x=10, y=300)
        self.kin_entry = Entry(window)
        self.kin_entry.place(x=200, y=300)
        self.submit = Button(window, text="SUBMIT", borderwidth=25, bg="black", fg="white")
        self.submit.place(x=200, y=400)


x = RegiSter()
window.mainloop()
