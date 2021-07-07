from tkinter import *
window = Tk()
window.geometry("500x600")
window.title("REGISTER")



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
        self.submit = Button(window, text="SIGNUP", borderwidth=15)
        self.submit.place(x=0, y=400)
        self.clear = Button(window, text="CLEAR", borderwidth=15, command=self.clear)
        self.clear.place(x=250, y=400)

    def clear(self):
        self.name_entry.delete(0, END)
        self.surname_entry.delete(0, END)
        self.identity_entry.delete(0, END)
        self.cell_entry.delete(0, END)
        self.next_entry.delete(0, END)
        self.kin_entry.delete(0, END)
        self.cell_entry.delete(0, END)



x = RegiSter()
window.mainloop()
