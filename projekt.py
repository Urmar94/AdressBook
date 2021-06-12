#Marek Urbański 54604
from sqlite3.dbapi2 import Row
from tkinter import *
import sqlite3

root = Tk()
root.title('Książka adresowa')
root.geometry("350x550")


#tworzenie tabeli
'''
conn = sqlite3.connect('address_book.db')

c = conn.cursor()

c.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    zipcode text,
    phone_number text,
    email text
    )""")
conn.commit()

conn.close()
'''
#funkcje
def save():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    record_id= del_box.get()
    c.execute("""UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    zipcode = :zipcode,
    phone_number = :phone,
    email = :email

    WHERE oid = :oid""",
    {
        'first':first_name_edit.get(),
        'last':last_name_edit.get(),
        'address':address_edit.get(),
        'city':city_edit.get(),
        'zipcode':zipcode_edit.get(),
        'phone':phone_number_edit.get(),
        'email':email_edit.get(),

        'oid':record_id
    })
      
                    
    conn.commit()

    conn.close()

    editor.destroy()

def delete():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid="+ del_box.get())

    conn.commit()

    conn.close()

    del_box.delete(0,END)

def edit():
    global editor

    editor = Tk()
    editor.title('Edytor wpisu')
    editor.geometry("350x300")
    
    global first_name_edit
    global last_name_edit
    global address_edit
    global city_edit
    global zipcode_edit
    global phone_number_edit
    global email_edit

    #Text boxes
    first_name_edit= Entry(editor,width=30)
    first_name_edit.grid(row=0, column=1, padx=20, pady=(10,0))

    last_name_edit= Entry(editor,width=30)
    last_name_edit.grid(row=1, column=1)

    address_edit= Entry(editor,width=30)
    address_edit.grid(row=2, column=1)

    city_edit= Entry(editor,width=30)
    city_edit.grid(row=3, column=1)

    zipcode_edit= Entry(editor,width=30)
    zipcode_edit.grid(row=4, column=1)

    phone_number_edit= Entry(editor,width=30)
    phone_number_edit.grid(row=5, column=1)

    email_edit= Entry(editor,width=30)
    email_edit.grid(row=6, column=1)

    
    #text boxes  label
    first_name_edit_label = Label(editor, text="Imię")
    first_name_edit_label.grid(row=0,column=0, pady=(10,0))

    last_name_edit_label = Label(editor, text="Nazwisko")
    last_name_edit_label.grid(row=1,column=0)

    address_edit_label = Label(editor, text="Adress")
    address_edit_label.grid(row=2,column=0)

    city_edit_label = Label(editor, text="Miasto")
    city_edit_label.grid(row=3,column=0)

    zipcode_edit_label = Label(editor, text="Kod pocztowy")
    zipcode_edit_label.grid(row=4,column=0)

    phone_number_edit_label = Label(editor, text="Telefon")
    phone_number_edit_label.grid(row=5,column=0)

    email_edit_label = Label(editor, text="Email")
    email_edit_label.grid(row=6,column=0)
    #button
    save_edit_btn=Button(editor, text="Zapisz zmiany", command=save)
    save_edit_btn.grid( row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    #uzupełnianie textboxów
    
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    record_id = del_box.get()

    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
    records=c.fetchall()
            
    for record in records:
        first_name_edit.insert(0, record[0])
        last_name_edit.insert(0, record[1])
        address_edit.insert(0, record[2])
        city_edit.insert(0, record[3])
        zipcode_edit.insert(0, record[4])
        phone_number_edit.insert(0, record[5])
        email_edit.insert(0, record[6])


    conn.commit()

    conn.close()

    del_box.delete(0,END)

def show():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    record_id = del_box.get()

    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
    records=c.fetchall()
    print_record=''
    for record in records:
        print_record= str(record[7])+".  "+str(record[0]) + " " + str(record[1]) + "\n" + str(record[2])+ "\n" + str(record[3])+ "\n" + str(record[4])+ "\n" + str(record[5])+ "\n" + str(record[6])
    
    show_label = Label(root, text=print_record)
    show_label.grid(row=13, column=0,columnspan=2)

    conn.commit()

    conn.close()

def submit():
    
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :zipcode, :phone_number, :email)",
            {
                'first_name': first_name.get(),
                'last_name': last_name.get(),
                'address': address.get(),
                'city': city.get(),
                'zipcode':zipcode.get(),
                'phone_number':phone_number.get(),
                "email": email.get()
            }
            )
            
    conn.commit()

    conn.close()

    #Czyszczenie
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)
    phone_number.delete(0,END)
    email.delete(0,END)

def query():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records=c.fetchall()
    
    print_records=''
    
    for record in records:
        print_records += str(record[7])+".  "+ str(record[0]) + " " + str(record[1]) + "\n"
       

    query_label = Label(root, text=print_records)
    query_label.grid(row=13, column=0,columnspan=2)

    conn.commit()

    conn.close()


#GUI
#Text boxes
first_name= Entry(root,width=30)
first_name.grid(row=0, column=1, padx=20, pady=(10,0))

last_name= Entry(root,width=30)
last_name.grid(row=1, column=1)

address= Entry(root,width=30)
address.grid(row=2, column=1)

city= Entry(root,width=30)
city.grid(row=3, column=1)

zipcode= Entry(root,width=30)
zipcode.grid(row=4, column=1)

phone_number= Entry(root,width=30)
phone_number.grid(row=5, column=1)

email= Entry(root,width=30)
email.grid(row=6, column=1)

del_box= Entry(root,width=30)
del_box.grid(row=9, column=1)

#text boxes  label
first_name_label = Label(root, text="Imię")
first_name_label.grid(row=0,column=0, pady=(10,0))

last_name_label = Label(root, text="Nazwisko")
last_name_label.grid(row=1,column=0)

address_label = Label(root, text="Adress")
address_label.grid(row=2,column=0)

city_label = Label(root, text="Miasto")
city_label.grid(row=3,column=0)

zipcode_label = Label(root, text="Kod pocztowy")
zipcode_label.grid(row=4,column=0)

phone_number_label = Label(root, text="Telefon")
phone_number_label.grid(row=5,column=0)

email_label = Label(root, text="Email")
email_label.grid(row=6,column=0)

sel_label = Label(root, text="ID")
sel_label.grid(row=9,column=0)

#button
submit_btn=Button(root, text="Dodaj wpis", command=submit)
submit_btn.grid( row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn=Button(root, text="Pokaż wpisy", command=query)
query_btn.grid(row=8,column=0,columnspan=2,padx=10,pady=10,ipadx=95)

ed_btn=Button(root, text="Edytuj wpis", command=edit)
ed_btn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=96)

del_btn=Button(root, text="Usuń wpis", command=delete)
del_btn.grid(row=12,column=0,columnspan=2,padx=10,pady=10,ipadx=98)

show_btn=Button(root, text="Pokaż wpis o podanym ID", command=show)
show_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=59)

root.mainloop()

