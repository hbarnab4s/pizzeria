import tkinter as tk
from tkinter import messagebox as MessageBox
import mysql.connector as mysql

if __name__ == "__main__":
    dbhost = 'localhost'
    dbuser = "test1"
    dbpass = 'test123'
    dbname = "pizzeria"

    root = tk.Tk()
    root.geometry("1100x600")
    root.title("Pizzéria")


    def clear_frame():
        for widgets in root.winfo_children():
            if (widgets != pizza_button and widgets != ugyfel_button and widgets != futar_button and widgets != szakacs_button and widgets != rendeles_button and widgets != szallitas_button):
                widgets.destroy()

#           ...:::          PIZZA           :::...

    def megjelenites_pizza():
        clear_frame()
        def atlagar_pizza():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('SELECT AVG(pizza.pizza_ar) FROM pizza')
            rows = cursor.fetchall()
            list_atlagar.delete(0, list_atlagar.size())
            for row in rows:
                insertData = 'A pizzák átlagára: {}'.format(row[0])
                list_atlagar.insert(list_atlagar.size() + 1, insertData)
            con.close()
        def get_pizza():
            if e_pizza_id.get() == "":
                MessageBox.showinfo("Info", "Az azonosító mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('select * from pizza where pizza_id={}'.format(e_pizza_id.get()))
                rows = cursor.fetchmany(1)
                for row in rows:
                    e_pizza_name.insert(0, row[1])
                    e_pizza_ar.insert(0, row[2])
                    e_pizza_meret.insert(0, row[3])
                    e_pizza_vega.insert(0, row[4])
                    e_pizza_hozzavalo.insert(0, row[5])
                con.close()
                show_pizza()
                atlagar_pizza()
        def insert_pizza():
            if e_pizza_id.get() == "" or e_pizza_name.get() == "" or e_pizza_ar.get() == "" or e_pizza_meret == "" or e_pizza_vega.get() == "" or e_pizza_hozzavalo.get() == "":
                MessageBox.showinfo("Info", "Minden mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute(
                    'insert into pizza values("{}","{}","{}","{}","{}","{}")'.format(e_pizza_id.get(), e_pizza_name.get(),e_pizza_ar.get(), e_pizza_meret.get(), e_pizza_vega.get(), e_pizza_hozzavalo.get()))
                cursor.execute('commit')
                e_pizza_id.delete(0, 'end')
                e_pizza_name.delete(0, 'end')
                e_pizza_ar.delete(0, 'end')
                e_pizza_meret.delete(0, 'end')
                e_pizza_vega.delete(0, 'end')
                e_pizza_hozzavalo.delete(0, 'end')
                MessageBox.showinfo("Info", "Sikeres beszúrás")
                con.close()
                show_pizza()
                atlagar_pizza()
        def update_pizza():
            if e_pizza_id.get() == "" or e_pizza_name.get() == "" or e_pizza_ar.get() == "" or e_pizza_meret.get() == "" or e_pizza_vega.get() == "" or e_pizza_hozzavalo.get() == "":
                MessageBox.showinfo("Info", "Minden mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('update pizza set pizza_nev="{}", pizza_ar="{}", pizza_meret={}, vegetarianus="{}", hozzavalok="{}" where pizza_id={}'.format(e_pizza_name.get(), e_pizza_ar.get(), e_pizza_meret.get(), e_pizza_vega.get(), e_pizza_hozzavalo.get(), e_pizza_id.get()))
                cursor.execute('commit')
                e_pizza_id.delete(0, 'end')
                e_pizza_name.delete(0, 'end')
                e_pizza_ar.delete(0, 'end')
                e_pizza_meret.delete(0, 'end')
                e_pizza_vega.delete(0, 'end')
                e_pizza_hozzavalo.delete(0, 'end')
                MessageBox.showinfo('Info', 'Sikeres frissítés')
                con.close()
                show_pizza()
                atlagar_pizza()
        def delete_pizza():
            if e_pizza_id.get() == "":
                MessageBox.showinfo("Info", "Azonosító mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('delete from pizza where pizza_id="{}"'.format(e_pizza_id.get()))
                cursor.execute('commit')
                e_pizza_id.delete(0, 'end')
                e_pizza_name.delete(0, 'end')
                e_pizza_ar.delete(0, 'end')
                e_pizza_meret.delete(0, 'end')
                e_pizza_vega.delete(0, 'end')
                e_pizza_hozzavalo.delete(0, 'end')
                MessageBox.showinfo('Info', 'Törlés végrehajtva')
                con.close()
                show_pizza()
                atlagar_pizza()
        def show_pizza():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from pizza')
            rows = cursor.fetchall()
            list1.delete(0, list1.size())
            for row in rows:
                insertData = '{}  |  {}  |  {}  |  {}  |  {}  |  {}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
                list1.insert(list1.size() + 1, insertData)
            con.close()

        pizza_kiiras = tk.Label(root, text="Pizzák", font=('bold', 18))
        pizza_kiiras.pack()

        pizza_id = tk.Label(root, text='Pizza azonosítója', font=('bold', 10))
        pizza_id.place(x=20, y=30)

        pizza_name = tk.Label(root, text="Pizza neve", font=('bold', 10))
        pizza_name.place(x=20, y=60)

        pizza_ar = tk.Label(root, text='Pizza ára', font=('bold', 10))
        pizza_ar.place(x=20, y=90)

        pizza_meret = tk.Label(root, text='Pizza mérete', font=('bold', 10))
        pizza_meret.place(x=20, y=120)

        pizza_vega = tk.Label(root, text="Vegetáriánus?", font=('bold', 10))
        pizza_vega.place(x=20, y=150)

        pizza_hozzavalo = tk.Label(root, text='Hozzávalók', font=('bold', 10))
        pizza_hozzavalo.place(x=20,y=180)

        e_pizza_id = tk.Entry()
        e_pizza_id.config(width=6)
        e_pizza_id.place(x=150, y=30)

        e_pizza_name = tk.Entry()
        e_pizza_name.config(width=35)
        e_pizza_name.place(x=150, y=60)

        e_pizza_ar = tk.Entry()
        e_pizza_ar.config(width=6)
        e_pizza_ar.place(x=150, y=90)

        e_pizza_meret = tk.Entry()
        e_pizza_meret.config(width=6)
        e_pizza_meret.place(x=150, y=120)

        e_pizza_vega = tk.Entry()
        e_pizza_vega.config(width=6)
        e_pizza_vega.place(x=150, y=150)

        e_pizza_hozzavalo = tk.Entry()
        e_pizza_hozzavalo.config(width=80)
        e_pizza_hozzavalo.place(x=150,y=180)

        pizza_insert_button = tk.Button(root, text="Beszúr", font=('italic', 10), fg='black', command=insert_pizza)
        pizza_insert_button.place(x=20, y=210)

        pizza_update_button = tk.Button(root, text="Frissít", font=('italic', 10,), fg='black', command=update_pizza)
        pizza_update_button.place(x=100, y=210)

        pizza_delete_button = tk.Button(root, text="Töröl", font=('italic', 10), fg='black', command=delete_pizza)
        pizza_delete_button.place(x=180, y=210)

        pizza_get_button = tk.Button(root, text="Lekér", font=('italic', 10), fg='black', command=get_pizza)
        pizza_get_button.place(x=260, y=210)

        list1 = tk.Listbox(root, width=120, height=15, borderwidth=5)
        list1.place(x=20, y=250)
        show_pizza()

        list_atlagar = tk.Listbox(root, width=35, height=1)
        list_atlagar.place(x=20,y=510)
        atlagar_pizza()


    pizza_button = tk.Button(root, text="Pizzák", font=('italic', 10), command=megjelenites_pizza)
    pizza_button.place(x=0, y=0)

#           ...:::          UGYFEL           :::...

    def megjelenites_ugyfel():
        clear_frame()
        def get_ugyfel():
            if e_ugyfel_email.get() == "":
                MessageBox.showinfo("Info", "Email mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('select * from ugyfel where email="{}"'.format(e_ugyfel_email.get()))
                rows = cursor.fetchmany(1)
                for row in rows:
                    e_ugyfel_nev.insert(0, row[1])
                    e_ugyfel_telefonszam.insert(0, row[2])
                    e_ugyfel_varos.insert(0, row[3])
                    e_ugyfel_utca.insert(0, row[4])
                    e_ugyfel_hazszam.insert(0, row[5])
                con.close()
                show_ugyfel()

        def insert_ugyfel():
            if e_ugyfel_email.get() == "" or e_ugyfel_nev.get() == "" or e_ugyfel_telefonszam.get() == "" or e_ugyfel_varos.get() == "" or e_ugyfel_utca.get() == "" or e_ugyfel_hazszam.get() == "":
                MessageBox.showinfo("Info", "Minden mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('insert into ugyfel values("{}","{}","{}", "{}", "{}", "{}")'.format(e_ugyfel_email.get(), e_ugyfel_nev.get(), e_ugyfel_telefonszam.get(), e_ugyfel_varos.get(), e_ugyfel_utca.get(), e_ugyfel_hazszam.get()))
                cursor.execute('commit')
                e_ugyfel_email.delete(0, 'end')
                e_ugyfel_nev.delete(0, 'end')
                e_ugyfel_telefonszam.delete(0, 'end')
                e_ugyfel_varos.delete(0, 'end')
                e_ugyfel_utca.delete(0, 'end')
                e_ugyfel_hazszam.delete(0, 'end')
                MessageBox.showinfo("Info", "Sikeres beszúrás")
                con.close()
                show_ugyfel()

        def delete_ugyfel():
            if e_ugyfel_email.get() == "":
                MessageBox.showinfo("Info", "Email mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('delete from ugyfel where email="{}"'.format(e_ugyfel_email.get()))
                cursor.execute('commit')
                e_ugyfel_email.delete(0, 'end')
                e_ugyfel_nev.delete(0, 'end')
                e_ugyfel_telefonszam.delete(0, 'end')
                e_ugyfel_varos.delete(0, 'end')
                e_ugyfel_utca.delete(0, 'end')
                e_ugyfel_hazszam.delete(0, 'end')
                MessageBox.showinfo('Info', 'Törlés végrehajtva')
                con.close()
                show_ugyfel()

        def delete_not_szedegi_ugyfel():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from ugyfel where varos !="Szeged"'.format(e_ugyfel_varos.get()))
            cursor.execute('commit')
            e_ugyfel_email.delete(0, 'end')
            e_ugyfel_nev.delete(0, 'end')
            e_ugyfel_telefonszam.delete(0, 'end')
            e_ugyfel_varos.delete(0, 'end')
            e_ugyfel_utca.delete(0, 'end')
            e_ugyfel_hazszam.delete(0, 'end')
            MessageBox.showinfo('Info', 'Törlés végrehajtva')
            con.close()
            show_ugyfel()

        def update_ugyfel():
            if e_ugyfel_email.get() == "" or e_ugyfel_nev.get() == "" or e_ugyfel_telefonszam.get() == "" or e_ugyfel_varos.get() == "" or e_ugyfel_utca.get() == "" or e_ugyfel_hazszam.get() == "":
                MessageBox.showinfo("Info", "Minden mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('update ugyfel set nev="{}", telefonszam="{}", varos="{}", utca="{}", hazszam="{}" where email="{}"'.format(e_ugyfel_nev.get(),e_ugyfel_telefonszam.get(),e_ugyfel_varos.get(),e_ugyfel_utca.get(),e_ugyfel_hazszam.get(), e_ugyfel_email.get()))
                cursor.execute('commit')
                e_ugyfel_email.delete(0, 'end')
                e_ugyfel_nev.delete(0, 'end')
                e_ugyfel_telefonszam.delete(0, 'end')
                e_ugyfel_varos.delete(0, 'end')
                e_ugyfel_utca.delete(0, 'end')
                e_ugyfel_hazszam.delete(0, 'end')
                MessageBox.showinfo('Info', 'Sikeres frissítés')
                con.close()
                show_ugyfel()

        def show_ugyfel():
            con2 = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor2 = con2.cursor()
            cursor2.execute('select * from ugyfel')
            rows2 = cursor2.fetchall()
            list2.delete(0, list2.size())
            for row in rows2:
                insertData2 = '{}  |  {}  |  {}  |  {}  {}  {}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
                list2.insert(list2.size() + 1, insertData2)
            con2.close()

        ugyfel_kiiras = tk.Label(root, text="Ügyfelek", font=('bold', 18))
        ugyfel_kiiras.pack()

        ugyfel_email = tk.Label(root, text="Ügyfél email-címe", font=('bold', 10))
        ugyfel_email.place(x=20, y=30)

        ugyfel_nev = tk.Label(root, text='Ügyfél neve', font=('bold', 10))
        ugyfel_nev.place(x=20, y=60)

        ugyfel_telfonszam = tk.Label(root, text='Ügyfél telefonszáma', font=('bold', 10))
        ugyfel_telfonszam.place(x=20, y=90)

        ugyfel_lakcim = tk.Label(root, text="Lakcím(város, utca, házszám)", font=('bold', 10))
        ugyfel_lakcim.place(x=20, y=120)

        e_ugyfel_email = tk.Entry(width=35)
        e_ugyfel_email.place(x=200, y=30)

        e_ugyfel_nev = tk.Entry(width=35)
        e_ugyfel_nev.place(x=200, y=60)

        e_ugyfel_telefonszam = tk.Entry()
        e_ugyfel_telefonszam.place(x=200, y=90)

        e_ugyfel_varos = tk.Entry()
        e_ugyfel_varos.place(x=200, y=120)

        e_ugyfel_utca = tk.Entry()
        e_ugyfel_utca.place(x=370, y=120)

        e_ugyfel_hazszam = tk.Entry()
        e_ugyfel_hazszam.place(x=540, y=120)

        ugyfel_insert_button = tk.Button(root, text="Beszúr", font=('italic', 10), fg='black', command=insert_ugyfel)
        ugyfel_insert_button.place(x=20, y=180)

        ugyfel_update_button = tk.Button(root, text="Frissít", font=('italic', 10,), fg='black', command=update_ugyfel)
        ugyfel_update_button.place(x=100, y=180)

        ugyfel_delete_button = tk.Button(root, text="Töröl", font=('italic', 10), fg='black', command=delete_ugyfel)
        ugyfel_delete_button.place(x=180, y=180)

        ugyfel_get_button = tk.Button(root, text="Lekér", font=('italic', 10), fg='black', command=get_ugyfel)
        ugyfel_get_button.place(x=260, y=180)

        ugyfel_not_szeged_delete_button = tk.Button(root, text="Nem szedegi lakosok törlése", font=('italic', 10), command=delete_not_szedegi_ugyfel)
        ugyfel_not_szeged_delete_button.place(x=440, y=180)

        global list2
        list2 = tk.Listbox(root, width=100, height=15, borderwidth=5)
        list2.place(x=20, y=220)
        show_ugyfel()


    ugyfel_button = tk.Button(root, text="Ügyfelek", font=('italic', 10), command=megjelenites_ugyfel)
    ugyfel_button.place(x=52, y=0)


#           ...:::          FUTAR           :::...

    def megjelenites_futar():
        clear_frame()
        def get_futar():
            if e_futar_id.get() == "":
                MessageBox.showinfo("Info", "Azonosító mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('select * from futar where futar_id={}'.format(e_futar_id.get()))
                rows = cursor.fetchmany(1)
                for row in rows:
                    e_futar_nev.insert(0, row[1])
                    e_futar_jarmu.insert(0, row[2])
                    e_futar_ertekeles.insert(0, row[3])
                con.close()
                show_futar()

        def update_futar():
            if e_futar_id.get() == "" or e_futar_nev.get() == "" or e_futar_jarmu.get() == "" or e_futar_ertekeles.get() == "":
                MessageBox.showinfo("Info", "Minden mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute(
                    'update futar set futar_nev="{}", futar_jarmu="{}", futar_ertekeles="{}" where futar_id={}'.format(e_futar_nev.get(),e_futar_jarmu.get(),e_futar_ertekeles.get(),e_futar_id.get()))
                cursor.execute('commit')
                e_futar_id.delete(0, 'end')
                e_futar_nev.delete(0, 'end')
                e_futar_jarmu.delete(0, 'end')
                e_futar_ertekeles.delete(0, 'end')
                MessageBox.showinfo('Info', 'Sikeres frissítés')
                con.close()
                show_futar()

        def insert_futar():
            if e_futar_id.get() == "" or e_futar_nev.get() == "" or e_futar_jarmu.get() == "" or e_futar_ertekeles.get() == "":
                MessageBox.showinfo("Info", "Minden mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('insert into futar values("{}","{}","{}","{}")'.format(e_futar_id.get(), e_futar_nev.get(),e_futar_jarmu.get(), e_futar_ertekeles.get()))
                cursor.execute('commit')
                e_futar_id.delete(0, 'end')
                e_futar_nev.delete(0, 'end')
                e_futar_jarmu.delete(0, 'end')
                e_futar_ertekeles.delete(0, 'end')
                MessageBox.showinfo("Info", "Sikeres beszúrás")
                con.close()
                show_futar()

        def delete_futar():
            if e_futar_id.get() == "":
                MessageBox.showinfo("Info", "Azonosító mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('delete from futar where futar_id="{}"'.format(e_futar_id.get()))
                cursor.execute('commit')
                e_futar_nev.delete(0, 'end')
                e_futar_jarmu.delete(0, 'end')
                e_futar_id.delete(0, 'end')
                e_futar_ertekeles.delete(0, 'end')
                MessageBox.showinfo('Info', 'Törlés végrehajtva')
                con.close()
                show_futar()

        def delete_futarUnder3():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from futar where futar_ertekeles<3'.format(e_futar_ertekeles.get()))
            cursor.execute('commit')
            e_futar_nev.delete(0, 'end')
            e_futar_jarmu.delete(0, 'end')
            e_futar_id.delete(0, 'end')
            e_futar_ertekeles.delete(0, 'end')
            MessageBox.showinfo('Info', 'Törlés végrehajtva')
            con.close()
            show_futar()

        def show_futar():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from futar')
            rows = cursor.fetchall()
            list3.delete(0, list3.size())
            for row in rows:
                insertData = '{}  |  {}  |  {}  |  {}'.format(row[0], row[1], row[2], row[3])
                list3.insert(list3.size() + 1, insertData)
            con.close()

        futar_kiiras = tk.Label(root, text="Futárok", font=('bold', 18))
        futar_kiiras.pack()

        futar_id = tk.Label(root, text='Futár azonosító', font=('bold', 10))
        futar_id.place(x=20, y=30)

        futar_nev = tk.Label(root, text="Futár neve", font=('bold', 10))
        futar_nev.place(x=20, y=60)

        futar_jarmu = tk.Label(root, text='Futár járműve', font=('bold', 10))
        futar_jarmu.place(x=20, y=90)

        futar_ertekeles = tk.Label(root, text="Futár értékelése", font=('bold', 10))
        futar_ertekeles.place(x=20, y=120)

        e_futar_id = tk.Entry(width=7)
        e_futar_id.place(x=150, y=30)

        e_futar_nev = tk.Entry(width=35)
        e_futar_nev.place(x=150, y=60)

        e_futar_jarmu = tk.Entry()
        e_futar_jarmu.place(x=150, y=90)

        e_futar_ertekeles = tk.Entry(width=7)
        e_futar_ertekeles.place(x=150, y=120)

        futar_insert_button = tk.Button(root, text="Beszúr", font=('italic', 10), fg='black', command=insert_futar)
        futar_insert_button.place(x=20, y=180)

        futar_update_button = tk.Button(root, text="Frissít", font=('italic', 10,), fg='black', command=update_futar)
        futar_update_button.place(x=100, y=180)

        futar_delete_button = tk.Button(root, text="Töröl", font=('italic', 10), fg='black', command=delete_futar)
        futar_delete_button.place(x=180, y=180)

        futar_get_button = tk.Button(root, text="Lekér", font=('italic', 10), fg='black',command=get_futar)
        futar_get_button.place(x=260, y=180)

        futar_deleteUnder3_button = tk.Button(root, text="Rossz értékelésű futárok elbocsájtása",font=('italic', 10), command=delete_futarUnder3)
        futar_deleteUnder3_button.place(x=440, y=180)

        list3 = tk.Listbox(root, width=100, height=15, borderwidth=5)
        list3.place(x=20, y=220)
        show_futar()


    futar_button = tk.Button(root, text="Futárok", font=('italic', 10), command=megjelenites_futar)
    futar_button.place(x=114, y=0)

#           ...:::          SZAKACS           :::...

    def megjelenites_szakacs():
        clear_frame()
        def get_szakacs():
            if e_szakacs_id.get() == "":
                MessageBox.showinfo("Info", "Azonosító mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('select * from szakacs where szakacs_id={}'.format(e_szakacs_id.get()))
                rows = cursor.fetchmany(1)
                for row in rows:
                    e_szakacs_nev.insert(0, row[1])
                    e_szakacs_fizetes.insert(0, row[2])
                    e_szakacs_ertekeles.insert(0, row[3])
                con.close()
                show_szakacs()

        def insert_szakacs():
            if e_szakacs_id.get() == "" or e_szakacs_nev.get() == "" or e_szakacs_fizetes.get() == "" or e_szakacs_ertekeles.get() == "":
                MessageBox.showinfo("Info", "Minden mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('insert into szakacs values("{}","{}","{}","{}")'.format(e_szakacs_id.get(), e_szakacs_nev.get(),e_szakacs_fizetes.get(), e_szakacs_ertekeles.get()))
                cursor.execute('commit')
                e_szakacs_id.delete(0, 'end')
                e_szakacs_nev.delete(0, 'end')
                e_szakacs_fizetes.delete(0, 'end')
                e_szakacs_ertekeles.delete(0, 'end')
                MessageBox.showinfo("Info", "Sikeres beszúrás")
                con.close()
                show_szakacs()

        def update_szakacs():
            if e_szakacs_id.get() == "" or e_szakacs_nev.get() == "" or e_szakacs_fizetes.get() == "" or e_szakacs_ertekeles.get() == "":
                MessageBox.showinfo("Info", "Minden mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('update szakacs set szakacs_nev="{}", szakacs_fizetes="{}", szakacs_ertekeles="{}" where szakacs_id={}'.format(e_szakacs_nev.get(), e_szakacs_fizetes.get(), e_szakacs_ertekeles.get(), e_szakacs_id.get()))
                cursor.execute('commit')
                e_szakacs_id.delete(0, 'end')
                e_szakacs_nev.delete(0, 'end')
                e_szakacs_fizetes.delete(0, 'end')
                e_szakacs_ertekeles.delete(0, 'end')
                MessageBox.showinfo('Info', 'Sikeres frissítés')
                con.close()
                show_szakacs()

        def update_szakacs_minimalber():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute(
                'update szakacs set szakacs_fizetes=200000 where szakacs_fizetes<200000'.format(e_szakacs_fizetes.get(), e_szakacs_fizetes.get()))
            cursor.execute('commit')
            e_szakacs_id.delete(0, 'end')
            e_szakacs_nev.delete(0, 'end')
            e_szakacs_fizetes.delete(0, 'end')
            e_szakacs_ertekeles.delete(0, 'end')
            MessageBox.showinfo('Info', 'Sikeres frissítés')
            con.close()
            show_szakacs()

        def delete_szakacs():
            if e_szakacs_id.get() == "":
                MessageBox.showinfo("Info", "Azonosító mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('delete from szakacs where szakacs_id="{}"'.format(e_szakacs_id.get()))
                cursor.execute('commit')
                e_szakacs_id.delete(0, 'end')
                e_szakacs_nev.delete(0, 'end')
                e_szakacs_fizetes.delete(0, 'end')
                e_szakacs_ertekeles.delete(0, 'end')
                MessageBox.showinfo('Info', 'Törlés végrehajtva')
                con.close()
                show_szakacs()

        def delete_szakacs_under3():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from szakacs where szakacs_ertekeles<3'.format(e_szakacs_ertekeles.get()))
            cursor.execute('commit')
            e_szakacs_id.delete(0, 'end')
            e_szakacs_nev.delete(0, 'end')
            e_szakacs_fizetes.delete(0, 'end')
            e_szakacs_ertekeles.delete(0, 'end')
            MessageBox.showinfo('Info', 'Törlés végrehajtva')
            con.close()
            show_szakacs()

        def show_szakacs():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from szakacs')
            rows = cursor.fetchall()
            list4.delete(0, list4.size())
            for row in rows:
                insertData = 'Azonosító: {}  | Név: {}  | Fizetés: {}  | Értékelés: {}'.format(row[0], row[1], row[2], row[3])
                list4.insert(list4.size() + 1, insertData)
            con.close()

        szakacs_kiiras = tk.Label(root, text="Szakácsok", font=('bold', 18))
        szakacs_kiiras.pack()

        szakacs_id = tk.Label(root, text="Szakács azonosítója", font=('bold', 10))
        szakacs_id.place(x=20, y=30)

        szakacs_nev = tk.Label(root, text="Szakács neve", font=('bold', 10))
        szakacs_nev.place(x=20, y=60)

        szakacs_fizetes = tk.Label(root, text="Szakács fizetése", font=('bold', 10))
        szakacs_fizetes.place(x=20, y=90)

        szakacs_ertekeles = tk.Label(root, text="Szakács értékelése", font=('bold', 10))
        szakacs_ertekeles.place(x=20, y=120)

        e_szakacs_id = tk.Entry(width=7)
        e_szakacs_id.place(x=150, y=30)

        e_szakacs_nev = tk.Entry(width=35)
        e_szakacs_nev.place(x=150, y=60)

        e_szakacs_fizetes = tk.Entry(width=10)
        e_szakacs_fizetes.place(x=150, y=90)

        e_szakacs_ertekeles = tk.Entry(width=7)
        e_szakacs_ertekeles.place(x=150, y=120)

        szakacs_insert_button = tk.Button(root, text="Beszúr", font=('italic', 10), fg='black', command=insert_szakacs)
        szakacs_insert_button.place(x=20, y=180)

        szakacs_update_button = tk.Button(root, text="Frissít", font=('italic', 10,), fg='black', command=update_szakacs)
        szakacs_update_button.place(x=100, y=180)

        szakacs_delete_button = tk.Button(root, text="Töröl", font=('italic', 10), fg='black', command=delete_szakacs)
        szakacs_delete_button.place(x=180, y=180)

        szakacs_get_button = tk.Button(root, text="Lekér", font=('italic', 10), fg='black', command=get_szakacs)
        szakacs_get_button.place(x=260, y=180)

        szakacs_deleteUnder3_button = tk.Button(root, text="Rossz értékelésű szakácsok elbocsájtása", font=('italic', 10), command=delete_szakacs_under3)
        szakacs_deleteUnder3_button.place(x=340, y=180)

        szakacs_minimalber_button = tk.Button(root, text="Minimálbér kifizetése", font=('italic', 10), command=update_szakacs_minimalber)
        szakacs_minimalber_button.place(x=600,y=180)

        list4 = tk.Listbox(root, width=100, height=15, borderwidth=5)
        list4.place(x=20, y=220)
        show_szakacs()


    szakacs_button = tk.Button(root, text="Szakácsok", font=('italic', 10), command=megjelenites_szakacs)
    szakacs_button.place(x=170, y=0)

#           ...:::          RENDELES           :::...
    def megjelenites_rendeles():
        clear_frame()
        def insert_rendeles():
            if e_rendeles_id.get() == "" or value_inside.get() == "" or value_inside_ev.get() == "" or value_inside_honap.get() == "" or value_inside_nap.get()=="":
                MessageBox.showinfo("Info", "Minden mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('INSERT INTO RENDELES(rendeles_id, email, pizza_nev, rendeles_ev, rendeles_honap, rendeles_nap) VALUES("{}","{}","{}","{}","{}","{}")'.format(e_rendeles_id.get(),value_inside.get(),value_inside_pizza.get(),value_inside_ev.get(),value_inside_honap.get(),value_inside_nap.get()))
                #cursor.execute(
                 #   'insert into rendeles set email="{}" where rendeles_id={} where values("{}","{}","{}","{}","{}")'.format(e_rendeles_id.get(),value_inside.get(),value_inside_ev.get(),value_inside_honap.get(),value_inside_nap.get()))
                cursor.execute('commit')
                e_rendeles_id.delete(0, 'end')
                value_inside.set("Válasszon a lehetőségek közül!")
                value_inside_pizza.set("Válasszon az alábbi pizzák közül!")
                value_inside_ev.set('Évszám')
                value_inside_honap.set("Hónap")
                value_inside_nap.set("Nap")
                MessageBox.showinfo("Info", "Sikeres beszúrás")
                con.close()
                show_rendeles()
                show_lekerdezes()
        def delete_rendeles():
            if e_rendeles_id.get() == "":
                MessageBox.showinfo("Info", "Azonosító mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('delete from rendeles where rendeles_id="{}"'.format(e_rendeles_id.get()))
                cursor.execute('commit')
                e_rendeles_id.delete(0, 'end')
                value_inside.set("Válasszon a lehetőségek közül!")
                value_inside_pizza.set("Válasszon az alábbi pizzák közül!")
                value_inside_ev.set('Évszám')
                value_inside_honap.set("Hónap")
                value_inside_nap.set("Nap")
                MessageBox.showinfo('Info', 'Törlés végrehajtva')
                con.close()
                show_rendeles()
                show_lekerdezes()
        def show_lekerdezes():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select ugyfel.email from ugyfel join rendeles on ugyfel.email = rendeles.email where rendeles.pizza_nev = "Négysajtos pizza"')
            rows = cursor.fetchall()
            list_lek.delete(0, list_lek.size())
            for row in rows:
                insertData = 'Email: {}'.format(row[0])
                list_lek.insert(list_lek.size() + 1, insertData)
            con.close()

        def show_rendeles():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from rendeles')
            rows = cursor.fetchall()
            list5.delete(0, list5.size())
            for row in rows:
                insertData = 'Azonosító: {}  | Email: {}  |  Pizza: {}  | Dátum: {}. {} {}.'.format(row[0], row[1], row[2], row[3], row[4], row[5])
                list5.insert(list5.size() + 1, insertData)
            con.close()

        rendeles_kiiras = tk.Label(root, text="Rendelések", font=('bold', 18))
        rendeles_kiiras.pack()

        rendeles_id = tk.Label(root, text="Rendelés azonosítója", font=('bold', 10))
        rendeles_id.place(x=20,y=30)

        ugyfel_email = tk.Label(root, text="Ügyfél email-címe", font=('bold', 10))
        ugyfel_email.place(x=20, y=60)

        pizza_nev = tk.Label(root, text="Választott pizza", font=('bold',10))
        pizza_nev.place(x=20,y=100)

        rendeles_ev = tk.Label(root, text="Rendelés dátuma(év, hónap, nap)", font=('bold', 10))
        rendeles_ev.place(x=20, y=140)

        e_rendeles_id=tk.Entry(width=7)
        e_rendeles_id.place(x=155, y=30)

        value_inside = tk.StringVar(root)
        con2 = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor2 = con2.cursor()
        cursor2.execute('select * from ugyfel')
        rows2 = cursor2.fetchall()
        # list2.delete(0, list2.size())
        option_list = []
        for row in rows2:
            insertData2 = '{}'.format(row[0])
            option_list += [insertData2]
        con2.close()

        value_inside_pizza = tk.StringVar(root)
        con3 = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor3 = con3.cursor()
        cursor3.execute('select * from pizza')
        rows3 = cursor3.fetchall()
        option_list3 = []
        for row in rows3:
            insertData3 = '{}'.format(row[1])
            option_list3 += [insertData3]
        con3.close()

        value_inside_pizza.set("Válasszon az alábbi pizzák közül!")
        e_pizza_nev = tk.OptionMenu(root, value_inside_pizza, *option_list3)
        e_pizza_nev.place(x=155,y=100)
        value_inside.set("Válasszon a lehetőségek közül!")
        e_ugyfel_email = tk.OptionMenu(root, value_inside, *option_list)
        e_ugyfel_email.place(x=155, y=60)


        value_inside_ev = tk.StringVar(root)
        value_inside_honap = tk.StringVar(root)
        value_inside_nap = tk.StringVar(root)
        option_list_ev = [2018, 2019,2020,2021,2022]
        option_list_honap = ["Január", "Február", "Március","Április","Május","Június","Július","Augusztus","Szeptember","Október","November","December"]
        option_list_nap= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        value_inside_ev.set('Évszám')
        value_inside_honap.set("Hónap")
        value_inside_nap.set("Nap")
        e_rendeles_ev = tk.OptionMenu(root,value_inside_ev,*option_list_ev)
        e_rendeles_ev.place(x=225, y=140)
        e_rendeles_honap = tk.OptionMenu(root, value_inside_honap, *option_list_honap)
        e_rendeles_honap.place(x=325, y=140)
        e_rendeles_nap = tk.OptionMenu(root, value_inside_nap, *option_list_nap)
        e_rendeles_nap.place(x=425, y=140)

        rendeles_insert_button = tk.Button(root, text="Beszúr", font=('italic', 10), command=insert_rendeles)
        rendeles_insert_button.place(x=20, y=180)

        rendeles_delete_button = tk.Button(root, text="Töröl", font=('italic', 10), command=delete_rendeles)
        rendeles_delete_button.place(x=100, y=180)


        list5 = tk.Listbox(root, width=100, height=15, borderwidth=5)
        list5.place(x=20, y=220)
        show_rendeles()


        list_lek_szoveg = tk.Label(root, text="Azon ügyfelek, akik négysajtos pizzát rendeltek", font=('bold',10))
        list_lek_szoveg.place(x=650,y=200)
        list_lek = tk.Listbox(root, width=60,height=15,borderwidth=5)
        list_lek.place(x=650,y=220)
        show_lekerdezes()


    rendeles_button = tk.Button(root, text="Rendelések", font=('italic', 10), command=megjelenites_rendeles)
    rendeles_button.place(x=248, y=0)

#               .........:::::::: SZÁLLÍTÁS :::::::...........
    def megjelenites_szallitas():
        clear_frame()

        def get_szallitas():
            if e_szallitas_id.get() == "":
                MessageBox.showinfo("Info", "Azonosító mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('select * from szallitas where szallitas_id={}'.format(e_szallitas_id.get()))
                rows = cursor.fetchmany(1)
                for row in rows:
                    e_pizza_id.insert(0, row[1])
                    e_futar_id.insert(0, row[2])
                con.close()
                show_szallitas()
                show_lekerdezes()

        def insert_szallitas():
            if e_szallitas_id.get() == "" or e_pizza_id.get() == "" or e_futar_id.get() == "":
                MessageBox.showinfo("Info", "Minden mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('insert into szallitas values("{}","{}","{}")'.format(e_szallitas_id.get(),e_pizza_id.get(),e_futar_id.get()))
                cursor.execute('commit')
                e_szallitas_id.delete(0,'end')
                e_pizza_id.delete(0,'end')
                e_futar_id.delete(0,'end')
                MessageBox.showinfo("Info", "Sikeres beszúrás")
                con.close()
                show_szallitas()
                show_lekerdezes()
        def update_szallitas():
            if e_szallitas_id.get() == "" or e_pizza_id.get() == "" or e_futar_id.get() == "":
                MessageBox.showinfo("Info", "Minden mező kitöltése kötelező")
            else:
                con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
                cursor = con.cursor()
                cursor.execute('update szallitas set pizza_id={}, futar_id={} where szallitas_id={}'.format(e_pizza_id.get(),e_futar_id.get(),e_szallitas_id.get()))
                cursor.execute('commit')
                e_szallitas_id.delete(0,'end')
                e_pizza_id.delete(0,'end')
                e_futar_id.delete(0,'end')
                MessageBox.showinfo("Info", "Sikeres beszúrás")
                con.close()
                show_szallitas()
                show_lekerdezes()
        def show_szallitas():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from szallitas')
            rows = cursor.fetchall()
            list6.delete(0, list6.size())
            for row in rows:
                insertData = 'Szállítás azonosító: {}   |   Pizza azonosító: {}   |   Futár azonosító: {}'.format(row[0], row[1], row[2])
                list6.insert(list6.size() + 1, insertData)
            con.close()

        def show_pizza():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from pizza')
            rows = cursor.fetchall()
            list_pizza.delete(0, list_pizza.size())
            for row in rows:
                insertData = '{}  |  {}'.format(row[0], row[1])
                list_pizza.insert(list_pizza.size() + 1, insertData)
            con.close()

        def show_futar():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from futar')
            rows = cursor.fetchall()
            list_futar.delete(0, list_futar.size())
            for row in rows:
                insertData = '{}  |  {}'.format(row[0], row[1])
                list_futar.insert(list_futar.size() + 1, insertData)
            con.close()

        def show_lekerdezes():
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select futar.futar_nev from futar join szallitas on futar.futar_id = szallitas.futar_id where futar.futar_ertekeles<3 ORDER BY futar.futar_ertekeles')
            rows = cursor.fetchall()
            list_lek.delete(0, list_lek.size())
            for row in rows:
                insertData = 'Rossz értékelésű futár, aki szállított: {}'.format(row[0])
                list_lek.insert(list_lek.size() + 1, insertData)
            con.close()

        szallitas_kiiras = tk.Label(root, text="Szállítások", font=('bold', 18))
        szallitas_kiiras.pack()

        szallitas_id = tk.Label(root, text="Szállítás azonosító",font=('bold', 10))
        szallitas_id.place(x=20, y=30)

        pizza_id = tk.Label(root, text="Pizza azonosító",font=('bold', 10))
        pizza_id.place(x=20, y=60)

        futar_id = tk.Label(root, text="Futár azonosító",font=('bold', 10))
        futar_id.place(x=20,y=90)

        e_szallitas_id = tk.Entry(width=7)
        e_szallitas_id.place(x=150,y=30)

        e_pizza_id = tk.Entry(width=7)
        e_pizza_id.place(x=150,y=60)

        e_futar_id = tk.Entry(width=7)
        e_futar_id.place(x=150,y=90)

        szallitas_insert_button = tk.Button(root, text="Beszúr", font=('italic', 10), fg='black', command=insert_szallitas)
        szallitas_insert_button.place(x=20, y=180)

        szallitas_update_button = tk.Button(root, text="Frissít", font=('italic', 10), fg='black',command=update_szallitas)
        szallitas_update_button.place(x=100, y=180)

        szallitas_get_button = tk.Button(root, text="Lekér", font=('italic', 10), fg='black', command=get_szallitas)
        szallitas_get_button.place(x=180, y=180)

        list6 = tk.Listbox(root, width=100, height=15, borderwidth=5)
        list6.place(x=20, y=220)
        show_szallitas()

        list_pizza = tk.Listbox(root, width=30, height=7, borderwidth=5)
        list_pizza.place(x=650, y=220)
        show_pizza()

        list_futar = tk.Listbox(root, width=30, height=7,borderwidth=5)
        list_futar.place(x=860,y=220)
        show_futar()

        list_lek = tk.Listbox(root, width=65, height=7, borderwidth=5)
        list_lek.place(x=650, y=350)
        show_lekerdezes()

    szallitas_button = tk.Button(root, text="Szállítások", font=('italic', 10), command=megjelenites_szallitas)
    szallitas_button.place(x=328,y=0)



    root.mainloop()