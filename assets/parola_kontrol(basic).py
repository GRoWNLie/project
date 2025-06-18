import re
import hashlib
import random
import string
from colorama import Fore, Style, init

init(autoreset=True)  # Renkler otomatik sıfırlansın

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
    with open(dosya_adi, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

# Kullanıcıdan Parola Al ve Test Et
def kullanici_parola_testi(sızıntı_listesi, hash_listesi):
    while True:
        parola = input("\nTest etmek istediğiniz parolayı girin (çıkmak için 'q'): ")
        if parola.lower() == 'q':
            break

        guc = parola_gucu_kontrol(parola)
        if guc == "Zayıf":
            print(Fore.RED + f"Güç Durumu: {guc}")
        elif guc == "Orta":
            print(Fore.YELLOW + f"Güç Durumu: {guc}")
        else:
            print(Fore.GREEN + f"Güç Durumu: {guc}")

        if sızıntı_kontrol(parola, sızıntı_listesi):
            print(Fore.RED + "Sızıntı Durumu: Sızıntıda Bulundu!")
        else:
            print(Fore.GREEN + "Sızıntı Durumu: Güvenli")

        if hash_kontrol(parola, hash_listesi):
            print(Fore.RED + "Hash Eşleşmesi: Hash veritabanında eşleşti!")
        else:
            print(Fore.GREEN + "Hash Eşleşmesi: Güvenli")

        print("-" * 40)

# Dosyadaki Parolaları Test Et ve Sonucu Kaydet
def dosya_parola_testi(parolalar, sızıntı_listesi, hash_listesi):
    with open("sonuc.txt", "w", encoding="utf-8") as dosya:
        for parola in parolalar:
            print(f"Parola: {parola}")
            dosya.write(f"Parola: {parola}\n")

            guc = parola_gucu_kontrol(parola)
            if guc == "Zayıf":
                print(Fore.RED + f"Güç Durumu: {guc}")
            elif guc == "Orta":
                print(Fore.YELLOW + f"Güç Durumu: {guc}")
            else:
                print(Fore.GREEN + f"Güç Durumu: {guc}")
            dosya.write(f"Güç Durumu: {guc}\n")

            if sızıntı_kontrol(parola, sızıntı_listesi):
                print(Fore.RED + "Sızıntı Durumu: Sızıntıda Bulundu!")
                dosya.write("Sızıntı Durumu: Sızıntıda Bulundu!\n")
            else:
                print(Fore.GREEN + "Sızıntı Durumu: Güvenli")
                dosya.write("Sızıntı Durumu: Güvenli\n")

            if hash_kontrol(parola, hash_listesi):
                print(Fore.RED + "Hash Eşleşmesi: Hash veritabanında eşleşti!")
                dosya.write("Hash Eşleşmesi: Hash veritabanında eşleşti!\n")
            else:
                print(Fore.GREEN + "Hash Eşleşmesi: Güvenli")
                dosya.write("Hash Eşleşmesi: Güvenli\n")

            print("-" * 40)
            dosya.write("-" * 40 + "\n")

# Güçlü Parola Üretici
def parola_uret(uzunluk=12):
    karakterler = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    parola = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return parola

# Ana Menü
def menu():
    parolalar = dosyadan_oku("parolalar.txt")
    sızıntı_listesi = dosyadan_oku("sızıntı_listesi.txt")
    hash_listesi = dosyadan_oku("hash_listesi.txt")

    while True:
        print("\n--- Parola Güvenlik Kontrol Menüsü ---")
        print("1. Dosyadaki Parolaları Kontrol Et")
        print("2. Manuel Parola Testi Yap")
        print("3. Güçlü Parola Üret")
        print("4. Çıkış")

        secim = input("Seçiminizi girin (1-4): ")

        if secim == '1':
            dosya_parola_testi(parolalar, sızıntı_listesi, hash_listesi)
        elif secim == '2':
            kullanici_parola_testi(sızıntı_listesi, hash_listesi)
        elif secim == '3':
            yeni_parola = parola_uret()
            print(Fore.GREEN + f"Otomatik Üretilen Parola: {yeni_parola}")
        elif secim == '4':
            print("Programdan çıkılıyor...")
            break
        else:
            print(Fore.RED + "Geçersiz seçim, lütfen 1-4 arasında bir değer girin!")

if __name__ == "__main__":
    menu()
