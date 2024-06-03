import tkinter as tk
from tkinter import messagebox, Toplevel, ttk
import mysql.connector
from tkinter import  *
from mysql.connector import Error
from tkinter import  font



pen = tk.Tk()
pen.title("Seyahat")
pen.configure(bg="#77e2f9")
pen.geometry("700x400+500+100")


label_description = Label(pen, text="", fg="gray", bg="#77e2f9")
label_description.pack(pady=10)

label_username = Label(pen, text="Kullanıcı Adı:", bg="#77e2f9")
label_username.pack()

entry_username = Entry(pen, bg="lightgray", fg="black")
entry_username.pack(pady=5)

label_password = Label(pen, text="Şifre:", bg="#77e2f9")
label_password.pack()

entry_password = Entry(pen, show="*", bg="lightgray", fg="black")
entry_password.pack(pady=5)

button_login = Button(pen, text="Giriş Yap",command=lambda: kullanıcı_giris(entry_username.get(), entry_password.get(), pen, db_connection),   bg="#00ccf9", fg="black", highlightbackground="black")
button_login.pack(pady=10)

button_open_register = Button(pen, text="Kayıt Ekranını Aç",command=lambda: kayıt_ol_ekranı(db_connection, pen),
                                 bg="#5F9EA0", fg="black", highlightbackground="black")
button_open_register.pack()




def kayıt(db_connection, new_username, new_password):
    if not new_username or not new_password:
        messagebox.showerror("Hata", "Kullanıcı adı ve şifre boş bırakılamaz")

        return

    cursor = db_connection.cursor()
    try:
        cursor.execute("INSERT INTO login (username, u_password) VALUES (%s, %s)", (new_username, new_password))
        db_connection.commit()
        messagebox.showinfo("Başarılı", "Kullanıcı kaydedildi: " + new_username)


    except Error as e:
        messagebox.showerror("Hata", f"Kullanıcı kaydedilemedi: {e}")

    finally:
        cursor.close()
def baglantıolusturma():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="seyahat"
        )
        print("Veritabanı bağlantısı başarılı")
        return db_connection
    except Error as e:
        print(f"Veritabanına bağlanırken hata oluştu: {e}")
        return None

def seyahatekle(db_connection, user_id, seyahat_ad, ulke, tarih):
    if not user_id or not seyahat_ad or not ulke or not tarih:
        messagebox.showerror("Hata", "Boş alan bırakmayınız")
        return

    cursor = db_connection.cursor()
    try:
        query = "INSERT INTO seyahat (user_id, seyahat_ad, ulke, tarih) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (user_id, seyahat_ad, ulke, tarih))
        db_connection.commit()
        messagebox.showinfo("Başarılı", "Seyahat kaydedildi")
    except Error as e:
        messagebox.showerror("Hata", f"Seyahat kaydedilemedi: {e}")
    finally:
        cursor.close()

def seyahat_düzenle(db_connection, seyahat_id, user_id, seyahat_ad, ulke, tarih):
    if not user_id or not seyahat_ad or not ulke or not tarih:
        messagebox.showerror("Hata", "Boş alan bırakmayınız")
        return

    cursor = db_connection.cursor()
    try:
        query = "UPDATE seyahat SET seyahat_ad = %s, ulke = %s, tarih = %s WHERE id = %s AND user_id = %s"
        cursor.execute(query, (seyahat_ad, ulke, tarih, seyahat_id, user_id))
        db_connection.commit()
        messagebox.showinfo("Başarılı", "Seyahat güncellendi")
    except Error as e:
        messagebox.showerror("Hata", f"Seyahat güncellenemedi: {e}")
    finally:
        cursor.close()

def open_edit_seyahat_window(db_connection, seyahat_id, user_id, seyahat_ad, ulke, tarih):
    edit_window = Toplevel()
    edit_window.title("Seyahat Düzenle")
    edit_window.geometry("700x400+500+100")
    edit_window.configure(bg="#77e2f9")

    label_seyahat_ad = Label(edit_window, text="Seyahat Adı:")
    label_seyahat_ad.pack()

    entry_seyahat_ad = Entry(edit_window)
    entry_seyahat_ad.insert(0, seyahat_ad)
    entry_seyahat_ad.pack(pady=5)

    label_ulke = Label(edit_window, text="Ülke:")
    label_ulke.pack()

    countries = ["Türkiye", "Almanya", "Fransa", "İtalya", "İngiltere", "ABD",]
    combo_ulke = ttk.Combobox(edit_window, values=countries)
    combo_ulke.set(ulke)
    combo_ulke.pack(pady=5)

    label_tarih = Label(edit_window, text="Tarih (YYYY-MM-DD):")
    label_tarih.pack()

    entry_tarih = Entry(edit_window)
    entry_tarih.insert(0, tarih)
    entry_tarih.pack(pady=5)

    def kaydet():
        seyahat_düzenle(db_connection, seyahat_id, user_id, entry_seyahat_ad.get(), combo_ulke.get(), entry_tarih.get())
        edit_window.destroy()

    button_kaydet = Button(edit_window, text="Seyahati Güncelle", command=kaydet)
    button_kaydet.pack(pady=10)


def seyahatler_goruntule(db_connection, user_id):
    seyahat_window = Toplevel()
    seyahat_window.title("Seyahatler")
    seyahat_window.geometry("700x400+500+100")
    seyahat_window.configure(bg="#77e2f9")

    tree = ttk.Treeview(seyahat_window, columns=("ID", "Seyahat Adı", "Ülke", "Tarih", "Düzenle"))

    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("ID", anchor=tk.CENTER, width=80)
    tree.column("Seyahat Adı", anchor=tk.W, width=120)
    tree.column("Ülke", anchor=tk.W, width=100)
    tree.column("Tarih", anchor=tk.W, width=100)
    tree.column("Düzenle", anchor=tk.W, width=80)

    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("ID", text="ID", anchor=tk.CENTER)
    tree.heading("Seyahat Adı", text="Seyahat Adı", anchor=tk.W)
    tree.heading("Ülke", text="Ülke", anchor=tk.W)
    tree.heading("Tarih", text="Tarih", anchor=tk.W)
    tree.heading("Düzenle", text="Düzenle", anchor=tk.W)

    cursor = db_connection.cursor()
    query = "SELECT * FROM seyahat WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    results = cursor.fetchall()

    for row in results:
        tree.insert("", tk.END, values=(row[0], row[2], row[3], row[4], ),
                    tags=(row[0],))  

    def secim(event):
        item = tree.selection()[0]
        seyahat_id = tree.item(item, "values")[0]
        seyahat_ad = tree.item(item, "values")[1]
        ulke = tree.item(item, "values")[2]
        tarih = tree.item(item, "values")[3]
        open_edit_seyahat_window(db_connection, seyahat_id, user_id, seyahat_ad, ulke, tarih)

    tree.bind("<Double-1>", secim)
    tree.pack(pady=10)



def pencere_ac(pen, user_id, db_connection):
    pen.destroy()
    main_window = tk.Tk()
    main_window.title("Ana Pencere")
    main_window.configure(bg="#77e2f9")
    main_window.geometry("700x400+500+100")

    label_user_id = Label(main_window, text=f"Kullanıcı ID: {user_id}" )
    label_user_id.pack(pady=10)

    label_seyahat_ad = Label(main_window, text="Seyahat Adı:")
    label_seyahat_ad.pack()

    entry_seyahat_ad = Entry(main_window)
    entry_seyahat_ad.pack(pady=5)

    label_ulke = Label(main_window, text="Ülke:")
    label_ulke.pack()

    countries = ["Türkiye", "Almanya", "Fransa", "İtalya", "İngiltere", "ABD"]
    combo_ulke = ttk.Combobox(main_window, values=countries)
    combo_ulke.pack(pady=5)

    label_tarih = Label(main_window, text="Tarih (YYYY-MM-DD):")
    label_tarih.pack()

    entry_tarih = Entry(main_window)
    entry_tarih.pack(pady=5)

    view_button = Button(main_window, text="Seyahatleri Görüntüle", command=lambda: seyahatler_goruntule(db_connection, user_id))


    def kaydet():
        seyahatekle(db_connection, user_id, entry_seyahat_ad.get(), combo_ulke.get(), entry_tarih.get())
        view_button.pack(pady=10)

    button_kaydet = Button(main_window, text="Seyahati Kaydet", command=kaydet)
    button_kaydet.pack(pady=10)


def kayıt_ol_ekranı(db_connection, pen):
    register_window = Toplevel(pen)
    register_window.title("Kayıt Ol")
    register_window.geometry("700x400+500+100")
    register_window.configure(bg="#77e2f9")

    label_new_username = Label(register_window, text="Yeni Kullanıcı Adı:", bg="#77e2f9")
    label_new_username.pack()

    entry_new_username = Entry(register_window)
    entry_new_username.pack(pady=5)

    label_new_password = Label(register_window, text="Yeni Şifre:", bg="#77e2f9")
    label_new_password.pack()

    entry_new_password = Entry(register_window, show="*")
    entry_new_password.pack(pady=5)

    button_register = Button(register_window, text="Kayıt Ol",command=lambda: kayıt(db_connection, entry_new_username.get(),entry_new_password.get()), bg="#5F9EA0", fg="black", highlightbackground="black")
    button_register.pack()


def baglantı_kapama(db_connection):
    if db_connection:
        db_connection.close()
        print("Veritabanı bağlantısı kapatıldı")

def kullanıcı_giris(username, password, pen, db_connection):
    cursor = db_connection.cursor()
    try:
        query = "SELECT id FROM login WHERE username = %s AND u_password = %s"
        cursor.execute(query, (username, password))
        results = cursor.fetchall()
        if results:
            result = results[0]
            messagebox.showinfo("Başarılı", "Giriş yapıldı: " + username)
            pencere_ac(pen, result[0], db_connection)
        else:
            messagebox.showerror("Hata", "Yanlış kullanıcı adı veya şifre")
    except Error as e:
        messagebox.showerror("Hata", f"Giriş yapılırken hata oluştu: {e}")
    finally:
        cursor.close()


db_connection = baglantıolusturma()


pen.mainloop()

baglantı_kapama(db_connection)
