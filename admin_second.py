from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(user='Lifechoices',
                               password='@Lifechoices1234',
                               host='127.0.0.1',
                               database='lifechoicesonline',
                               auth_plugin='mysql_native_password')

window = Tk()
window.title("Login Page")
window.geometry("1200x1200")
window.config(bg='hot pink')

# first tree view

trv2 = ttk.Treeview(window, selectmode='browse')
trv2.grid(row=2, column=1)

trv2["columns"] = ("1", "2", "3", "4")
trv2['show'] = 'headings'

trv2.column("1", width=100, anchor='c')
trv2.column("2", width=100, anchor='c')
trv2.column("3", width=100, anchor='c')
trv2.column("4", width=100, anchor='c')


trv2.heading("1", text="id")
trv2.heading("2", text="full_name")
trv2.heading("3", text="surname")
trv2.heading("4", text="password")


mycursor = mydb.cursor()
xy = mycursor.execute('SELECT * FROM users')


for dt in mycursor:
    trv2.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1], dt[2], dt[3]))


# Logins tree view
trv = ttk.Treeview(window, selectmode='browse')
trv.grid(row=1, column=1, pady=40)

trv["columns"] = ("1", "2", "3", "4")
trv['show'] = 'headings'

trv.column("1", width=100, anchor='c')
trv.column("2", width=100, anchor='c')
trv.column("3", width=100, anchor='c')
trv.column("4", width=100, anchor='c')



trv.heading("1", text="id")
trv.heading("2", text="full_name")
trv.heading("3", text="username")
trv.heading("4", text="password")


mycursor = mydb.cursor()
xy = mycursor.execute('SELECT * from users')

for dt in mycursor:
    trv.insert("", 'end', iid=dt[0], text=dt[0],
               values=(dt[0], dt[1], dt[2], dt[3]))


def delete():

    selected = trv.focus()
    values = trv.item(selected, 'values')
    mydb = mysql.connector.connect(user='Lifechoices',
                                   password='@Lifechoices021',
                                   host='127.0.0.1',
                                   database='Registration',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    sql = "DELETE FROM new WHERE id = %s"
    val = (values[0],)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo('Deleted', 'Deleted successfully.')


def update():
    update = Label(window, text='Field to update:')
    update.place(x=750, y=350)
    update_entry = Entry(window)
    update_entry.place(x=860, y=350)
    update2_label = Label(window, text='Update: ')
    update2_label.place(x=750, y=400)
    update2_entry = Entry(window)
    update2_entry.place(x=860, y=400)
    into = Label(window, text='update to:')
    into.place(x=750, y=450)
    into_entry = Entry(window)
    into_entry.place(x=860, y=450)
    # update2 = Button(root, text ='update', command =update)
    # update2.place(x=870, y=500)

    if update_entry.get() == 'name':
        mydb = mysql.connector.connect(user='Lifechoices',
                                       password='@Lifechoices',
                                       host='127.0.0.1',
                                       database='Registration',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE new SET name = %s WHERE name = %s"
        val = (into_entry.get(), update2_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()
    elif update_entry.get() == 'surname':

        mydb = mysql.connector.connect(user='Lifechoices',
                                       password='@Lifechoices',
                                       host='127.0.0.1',
                                       database='Registration',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE new SET surname = %s WHERE surname = %s"
        val = (into_entry.get(), update2_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()

    elif update_entry.get() == 'cellphone':
        mydb = mysql.connector.connect(user='Lifechoices',
                                       password='@Lifechoices1234',
                                       host='127.0.0.1',
                                       database='Registration',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE new SET cellphone = %s WHERE password = %s"
        val = (into_entry.get(), update2_entry.get())
        mycursor.execute(sql, val)
        mydb.commit()


def add_admin():
    selected = trv.focus()
    values = trv.item(selected, 'values')
    mydb = mysql.connector.connect(user='Lifechoices',
                                   password='@Lifechoices1234',
                                   host='127.0.0.1',
                                   database='lifechoicesonline',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    sql = "INSERT INTO admin (name, surname, password) VALUES (%s, %s , %s)"
    val = (values[1], values[2], values[3],)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo('Added', 'User is now admin.')


def logout_user():
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    selected = trv2.focus()
    values = trv2.item(selected, 'values')
    mydb = mysql.connector.connect(user='Lifechoices',
                                   password='@Lifechoices134',
                                   host='127.0.0.1',
                                   database='lifechoicesonline',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    sql = "UPDATE LOGIN_OUT SET time = %s WHERE username = %s AND password = %s"
    val = (formatted_date, values[0], values[3],)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo(title='Logged Out', message='User is now logged out.')


def view_admin():

    trv2 = ttk.Treeview(window, selectmode='browse')
    trv2.grid(row=3, column=1, padx=20, pady=20)

    trv2["columns"] = ("1", "2", "3", "4")
    trv2['show'] = 'headings'

    trv2.column("1", width=30, anchor='c')
    trv2.column("2", width=100, anchor='c')
    trv2.column("3", width=100, anchor='c')
    trv2.column("4", width=100, anchor='c')

    trv2.heading("1", text="id")
    trv2.heading("2", text="name")
    trv2.heading("3", text="surname")
    trv2.heading("4", text="password")

    mycursor = mydb.cursor()
    x = mycursor.execute('SELECT * FROM admin')

    for dt in mycursor:
        trv2.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1], dt[2], dt[3]))


def add_record():
    window.destroy()
    import second_screen


def exit():
    window.destroy()
    import main_screen


del_btn = Button(window, text='Delete selected row', command=delete)
del_btn.place(x=850, y=50)

up_date_btn = Button(window, text='Update', command=update)
up_date_btn.place(x=870, y=500)

add_button = Button(window, text='Add new user')
add_button.place(x=850, y=150)

logout_btn = Button(window, text='Logout user', command=logout_user)
logout_btn.place(x=850, y=200)

exit_btn = Button(window, text='Go to main page', command=exit)
exit_btn.place(x=850, y=250)

view_admin_btn = Button(window, text='View Admin users', command=view_admin)
view_admin_btn.place(x=850, y=100)


window.mainloop()
