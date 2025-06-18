# Otomasyon ve Parola Güvenliği Projesi

## Proje Hakkında
Bu proje, otomasyon ve parola güvenliği konularını birleştirerek kullanıcıların parolalarını kolayca kontrol etmelerini sağlayan bir **Parola Güçlülük Kontrol Aracı** geliştirmeyi amaçlamaktadır.  
Python ve Tkinter kullanılarak geliştirilmiş, parola güçlendirme, parola sızıntısı kontrolü ve hash eşleşme denetimi yapan kapsamlı bir masaüstü uygulamasıdır.

---

## Features / Özellikler

- Parola güçlülüğünü anlık olarak değerlendirme  
- Parolanın bilinen sızıntı listelerinde olup olmadığını kontrol etme  
- SHA1 hash karşılaştırması ile parolanın daha önce ele geçirilip geçirilmediğini denetleme  
- Dosya içinden çoklu parola kontrolü yapabilme  
- Güçlü, rastgele parola üretme fonksiyonu  
- Basit ve kullanıcı dostu grafiksel arayüz (GUI)  
- Sonuçların renklerle vurgulanması (Güçlü = yeşil, Zayıf = kırmızı vb.)

---

## Team / Ekip

| İsim           | Numara   | GitHub Profili                      |
|----------------|----------|-----------------------------------|
| Baran Kabçak   | 2320191061 | [GRoWNLie](https://github.com/GRoWNLie) |
| Yusuf Akel     | 2320191070 | [yyakell](https://github.com/yyakell)    |

---

## Roadmap / Yol Haritası

- [x] Parola güçlülük kontrol algoritması  
- [x] Parola sızıntı listesi ile karşılaştırma  
- [x] SHA1 hash kontrolü  
- [x] Dosyadan toplu parola kontrolü  
- [x] Parola üretici fonksiyon  
- [x] Tkinter tabanlı GUI geliştirme  
---

## Research / Araştırmalar

Proje kapsamında aşağıdaki konular araştırılmıştır:

- Parola güvenliği standartları ve en iyi uygulamalar  
- Parola sızıntısı veritabanlarının yapısı (örn. Have I Been Pwned)  
- SHA1 hash fonksiyonunun güvenlik durumu ve kullanımı  
- Python Tkinter kütüphanesi ile kullanıcı arayüzü tasarımı  
- Regex kullanımı ile güçlü parola kontrol kriterleri  

---

##Usage / Kullanım
-Program açıldığında, parolanızı giriş kutusuna yazın ve "Parolayı Kontrol Et" butonuna tıklayın.
-Parolanızın güç durumu, sızıntı durumu ve hash eşleşme durumu renklerle gösterilecektir.
-"Güçlü Parola Üret" butonuna basarak rastgele güçlü bir parola oluşturabilirsiniz.
-"Dosyadan Parola Kontrolü" butonuna basarak, içinde parolalar bulunan bir metin dosyası seçebilir ve toplu kontrol yapabilirsiniz.

---
## License / Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.
Detaylar için LICENSE dosyasına bakınız.

---
## Installation / Kurulum

1. Python 3 yüklü olmalı (tercihen 3.7 veya üstü)  
2. Gerekli Python kütüphanelerini yükleyin (örneğin, `pip install colorama`)  
3. Projeyi klonlayın veya zip olarak indirin:  
   ```bash
   git clone https://github.com/GRoWNLie/parola-guvenlik-araci.git
