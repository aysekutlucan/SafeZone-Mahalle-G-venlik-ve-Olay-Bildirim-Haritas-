# AI Geliştirme Günlüğü - Oturum 1

**Tarih:** 24.05.2026
**Kullanılan Model:** Claude Sonnet 4.6 (Thinking)

### Yapılan İşlemler:
1. GitHub Desktop üzerinde 'SafeZone-Mahalle-Guvenlik-ve-Olay-Bildirim-Haritasi' adında yerel ve uzak depo ayağa kaldırıldı.
2. Antigravity IDE Sandbox ve Onay (Request Review) modları aktif edilerek güvenli geliştirme ortamı kuruldu.
3. Ajan modele 'Application Factory Pattern' ve 'Blueprint' kısıtları verilerek projenin temel klasör yapısı (app/, config.py, run.py, requirements.txt) Plan Modunda oluşturuldu.
4. Oluşturulan altyapı kodları anlamlı commit mesajıyla GitHub'a başarıyla gönderildi.

# AI Geliştirme Günlüğü - Oturum 2

**Tarih:** 25.05.2026
**Kullanılan Model:** Gemini 3.1 Pro (High)

### Yapılan İşlemler:
1. **Kimlik Doğrulama (Auth) Altyapısı:** `Flask-WTF` kütüphanesi ile `RegistrationForm` ve `LoginForm` doğrulama formları oluşturuldu. `/register`, `/login` ve `/logout` rotaları yazılarak `werkzeug.security` üzerinden güvenli şifre saklama işlemleri entegre edildi.
2. **Ham Arayüz İskeletleri (Sıfır Tasarım):** Arayüz tasarımı 4. Güne bırakılarak, yalnızca sistemin fonksiyonel çalışmasını doğrulayacak ham `base.html`, `index.html`, `login.html` ve `register.html` şablonları inşa edildi.
3. **Olay Bildirim (Incident) Altyapısı:** Kullanıcıların mahallelerinde gerçekleşen olayları bildirebileceği `IncidentForm` hazırlandı. Eksik olan `latitude` ve `longitude` sütunları `app/models.py` içerisine eklenerek veritabanı göç (migration) işlemleri (`flask db init/migrate/upgrade`) başarıyla tamamlandı. `/incident/new` rotası ile veri akışı sağlandı.
4. **Kullanıcı Profil Paneli (Dashboard):** `@login_required` ile korunan `/profile` rotası kurularak, kullanıcıların bildirdikleri geçmiş olayların `current_user.incidents` üzerinden dökümü yapıldı.

# AI Geliştirme Günlüğü - Oturum 3

**Tarih:** 26.05.2026
**Kullanılan Model:** Gemini 3.1 Pro (High)

### Yapılan İşlemler:
1. **Harita Entegrasyonu ve Dinamik Veri:** "Sıfır tasarım, sıfır CSS" prensibi doğrultusunda Leaflet.js CDN üzerinden projeye dahil edildi. `app/templates/main/index.html` ve `app/templates/main/create_incident.html` dosyalarına harita konteynerleri eklendi.
2. **Haritadan Koordinat Yakalama:** Olay bildirim sayfasında kullanıcıların haritaya tıklayarak koordinat seçmesini sağlayan ve seçilen enlem/boylam değerlerini form alanlarına aktaran bir JavaScript olay dinleyicisi entegre edildi.
3. **JSON Veri Adası (Data Island) Mimarisi:** IDE'lerin Jinja2 syntax'ını JavaScript hatası olarak işaretlemesini engellemek için, veritabanından çekilen olay verileri doğrudan JavaScript bloğuna değil, `type="application/json"` olan bir veri adasına yazdırıldı. JavaScript'in bu veriyi `JSON.parse()` ile güvenli şekilde tüketmesi sağlandı.