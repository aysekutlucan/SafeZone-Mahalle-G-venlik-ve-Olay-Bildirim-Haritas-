# 🛡️ SafeZone: Çankaya Bölgesi Güvenlik Simülasyon Paneli

<p align="center">
  <img src="https://img.shields.io/badge/Flask-v3.0+-1e293b?style=for-the-badge&logo=flask" alt="Flask" />
  <img src="https://img.shields.io/badge/Bootstrap-v5.3-563d7c?style=for-the-badge&logo=bootstrap" alt="Bootstrap" />
  <img src="https://img.shields.io/badge/Leaflet-v1.9-green?style=for-the-badge&logo=leaflet" alt="Leaflet" />
  <img src="https://img.shields.io/badge/Docker-Ready-2496ed?style=for-the-badge&logo=docker" alt="Docker" />
</p>

---

## 📖 Proje Hakkında

**SafeZone**, modern kent yaşamında mahalle düzeyindeki asayiş, trafik, şüpheli durum ve altyapı sorunlarının anlık olarak izlenmesi, konumlandırılması ve taktiksel bir harita üzerinden simüle edilmesi amacıyla geliştirilmiş kurumsal bir güvenlik panelidir. 

Ankara Çankaya ve Kızılay bölgelerine kilitlenmiş simülasyon haritası, karanlık tema uyumlu **CartoDB Dark Matter** katmanları ve interaktif olay odaklama yeteneğiyle jüri önünde sunulmaya hazır, tam kapsamlı bir komuta arayüzüdür.

### ✨ Temel Özellikler
*   **📍 Kilitli Coğrafi Sınırlar:** Ankara Kızılay/Çankaya sınırlarına kilitli harita sayesinde sınır dışına çıkılması tamamen engellenmiş gerçekçi simülasyon alanı.
*   **📊 Komuta Paneli Arayüzü:** Koyu lacivert kurumsal tema, hareketli yayın sinyalleri, toplam ihbar ve sistem durumu göstergeleri.
*   **📜 İnteraktif İhbar Kartları:** Kategorilerine göre renk kodlu (Asayiş: Kırmızı, Trafik: Sarı, Şüpheli Durum: Mavi vb.) sol tarafta yer alan olay listesi.
*   **⚡ Pürüzsüz Harita Odaklanma:** Sol listedeki karta tıklandığında haritanın otomatik olarak ilgili koordinata kayması ve popup bilgilendirme balonunu açması.
*   **📑 Sayfalama (Pagination):** Hem backend (SQLAlchemy) hem frontend (Bootstrap 5) seviyesinde sayfa başına 5 ihbar sınırı.
*   **🛡️ Global Hata Yönetimi:** Kalkan logolu ve animasyonlu kurumsal 404 (Sınır İhlali) ve 500 (Sistem Hatası) hata sayfaları.
*   **🐳 Dockerizasyon:** `Dockerfile` ve `docker-compose.yml` altyapısı sayesinde tek komutla veri kalıcılığını (SQLite Volume Mount) koruyarak ayağa kalkma özelliği.

---

## 🛠️ Yerel Kurulum ve Çalıştırma Adımları

Uygulamayı yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları sırayla takip ediniz:

### 1. Projeyi Klonlayın ve Sanal Ortam Oluşturun
```bash
# Proje dizinine girin
cd SafeZone-Mahalle-Guvenlik-ve-Olay-Bildirim-Haritasi

# Python sanal ortamı (venv) oluşturun
python -m venv .venv

# Sanal ortamı aktif edin (Windows)
.venv\Scripts\activate

# Sanal ortamı aktif edin (macOS/Linux)
source .venv/bin/activate
```

### 2. Bağımlılıkları Yükleyin
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Veritabanı Göç Dosyalarını ve Şemayı Kurun
Uygulama SQLite kullanmaktadır. Veritabanını hazırlamak için:
```bash
# Veritabanını ilklendirin (Eğer migrations klasörü yoksa)
flask db init

# Göç dosyalarını hazırlayın
flask db migrate -m "init database schema"

# Şemayı uygulayın
flask db upgrade
```

### 4. Uygulamayı Başlatın
```bash
python run.py
```
Uygulama yerelde **`http://127.0.0.1:5000`** adresinde çalışmaya başlayacaktır.

---

## 🐳 Docker ile Çalıştırma Adımları

SafeZone, Docker ve Docker Compose ile üretime (production) hazır halde paketlenmiştir. Docker kullanarak tek bir komutla uygulamayı ayağa kaldırabilirsiniz:

```bash
# Docker konteynerini derleyin ve arka planda çalıştırın
docker-compose up --build -d
```
*   Uygulamaya **`http://localhost:5000`** adresinden erişebilirsiniz.
*   **Veri Kalıcılığı:** SQLite veritabanı dosyanız (`safezone.db`), `docker-compose.yml` içindeki volume eşleştirmesi sayesinde host makineye bağlıdır. Konteyner silinse bile ihbar verileriniz kaybolmaz.
*   Konteyneri durdurmak için: `docker-compose down`

---

## 🎥 Proje Tanıtım ve Demo Videosu

SafeZone Güvenlik Simülasyon Paneli'nin tüm interaktif özelliklerini, kilitli harita sınırlarını ve hata sayfalarını çalışır halde izlemek için aşağıdaki demo video alanını kullanabilirsiniz:

[🚀 SafeZone Proje Demo ve Sunum Videosunu İzlemek İçin Tıklayın (Drive/YouTube Linki)](https://github.com/aysekutlucan/SafeZone-Mahalle-G-venlik-ve-Olay-Bildirim-Haritas-)

---

## 📁 Dosya Yapısı Özet

```text
├── app/
│   ├── auth/           # Kayıt, Giriş ve Profil Modülleri (Blueprint)
│   ├── main/           # Ana Panel, Olay Bildirimi ve Hata Yönetimi (Blueprint)
│   ├── templates/      # Jinja2 HTML Şablonları (errors/ ve main/ alt dizinleriyle)
│   ├── models.py       # SQLAlchemy Veritabanı Modelleri (User, Incident, Neighborhood)
│   └── __init__.py     # Application Factory & Eklenti Başlatma
├── docs/
│   ├── ai-gunlugu.md   # Geliştirme Sürecinin Adım Adım Kronolojik Yapay Zeka Günlüğü
│   └── rapor.md        # Detaylı Akademik/Kurumsal Teknik Proje Raporu
├── run.py              # Uygulama Giriş Noktası (Entrypoint)
├── Dockerfile          # Optimize Edilmiş Docker Yapılandırması
├── docker-compose.yml  # Hacim Mount Destekli Docker Orchestration Dosyası
└── requirements.txt    # Tüm Python Kütüphane Bağımlılıkları Listesi
```

---

🛡️ *SafeZone, mahallenizin güvenliği için 7/24 aktif siber koruma simülasyonudur.*
