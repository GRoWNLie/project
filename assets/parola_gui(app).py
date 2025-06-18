import re
import hashlib
import random
import string
from tkinter import *
from tkinter import messagebox, filedialog

# Parola Güç Kontrolü
def parola_gucu_kontrol(parola):
    puan = 0
    if len(parola) >= 8:
        puan += 1
    if re.search(r"[A-Z]", parola):
        puan += 1
    if re.search(r"[a-z]", parola):
        puan += 1
    if re.search(r"[0-9]", parola):
        puan += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", parola):
        puan += 1

    if puan <= 2:
        return "Zayıf"
    elif puan == 3 or puan == 4:
        return "Orta"
    else:
        return "Güçlü"

# Sızıntı Kontrolü
def sızıntı_kontrol(parola, sızıntı_listesi):
    return parola in sızıntı_listesi

# Hash Kontrolü
def sha1_hash(parola):
    return hashlib.sha1(parola.encode()).hexdigest()

def hash_kontrol(parola, hash_listesi):
    parola_hash = sha1_hash(parola)
    return parola_hash in hash_listesi

# Dosya Okuma
def dosyadan_oku(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except:
        return []

# Güçlü Parola Üretici
def parola_uret(uzunluk=12):
    karakterler = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    parola = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return parola

# Parola Kontrol Fonksiyonu
def parola_kontrol():
    parola = parola_entry.get()
    if not parola:
        messagebox.showwarning("Uyarı", "Lütfen bir parola girin!")
        return

    guc = parola_gucu_kontrol(parola)
    if guc == "Zayıf":
        guc_label.config(text=f"Güç Durumu: {guc}", fg="red")
    elif guc == "Orta":
        guc_label.config(text=f"Güç Durumu: {guc}", fg="orange")
    else:
        guc_label.config(text=f"Güç Durumu: {guc}", fg="green")

    if sızıntı_kontrol(parola, sızıntı_listesi):
        sızıntı_label.config(text="Sızıntı Durumu: Sızıntıda Bulundu!", fg="red")
    else:
        sızıntı_label.config(text="Sızıntı Durumu: Güvenli", fg="green")

    if hash_kontrol(parola, hash_listesi):
        hash_label.config(text="Hash Eşleşmesi: Eşleşti!", fg="red")
    else:
        hash_label.config(text="Hash Eşleşmesi: Güvenli", fg="green")

# Dosyadan Parola Kontrolü
def dosya_parola_kontrol():
    dosya_yolu = filedialog.askopenfilename(title="Parola Dosyasını Seçin",
                                            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if not dosya_yolu:
        return

    parolalar = dosyadan_oku(dosya_yolu)
    if not parolalar:
        messagebox.showwarning("Uyarı", "Dosya boş ya da okunamadı!")
        return

    # Sonuçları temizle
    sonuc_text.delete(1.0, END)

    for parola in parolalar:
        guc = parola_gucu_kontrol(parola)
        sızıntı = "Sızıntıda Bulundu!" if sızıntı_kontrol(parola, sızıntı_listesi) else "Güvenli"
        hash_durum = "Eşleşti!" if hash_kontrol(parola, hash_listesi) else "Güvenli"

        sonuc_text.insert(END, f"Parola: {parola}\n")
        sonuc_text.insert(END, f"  Güç Durumu: {guc}\n")
        sonuc_text.insert(END, f"  Sızıntı Durumu: {sızıntı}\n")
        sonuc_text.insert(END, f"  Hash Eşleşmesi: {hash_durum}\n")
        sonuc_text.insert(END, "-"*40 + "\n")

# GUI Başlangıç
sızıntı_listesi = dosyadan_oku("sızıntı_listesi.txt")
hash_listesi = dosyadan_oku("hash_listesi.txt")

pencere = Tk()
pencere.title("Parola Güvenlik Kontrol Aracı")
pencere.geometry("500x500")

baslik = Label(pencere, text="Parola Güvenlik Kontrolü", font=("Arial", 16))
baslik.pack(pady=10)

parola_entry = Entry(pencere, width=30, font=("Arial", 14))
parola_entry.pack(pady=5)

kontrol_btn = Button(pencere, text="Parolayı Kontrol Et", command=parola_kontrol)
kontrol_btn.pack(pady=5)

uret_btn = Button(pencere, text="Güçlü Parola Üret", command=lambda: parola_entry.insert(0, parola_uret()))
uret_btn.pack(pady=5)

dosya_kontrol_btn = Button(pencere, text="Dosyadan Parola Kontrolü", command=dosya_parola_kontrol)
dosya_kontrol_btn.pack(pady=5)

guc_label = Label(pencere, text="Güç Durumu: ", font=("Arial", 12))
guc_label.pack(pady=5)

sızıntı_label = Label(pencere, text="Sızıntı Durumu: ", font=("Arial", 12))
sızıntı_label.pack(pady=5)

hash_label = Label(pencere, text="Hash Eşleşmesi: ", font=("Arial", 12))
hash_label.pack(pady=5)

sonuc_text = Text(pencere, height=10, width=60)
sonuc_text.pack(pady=10)

pencere.mainloop()
