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
## AI Geliştirme Günlüğü - Oturum 4
**Tarih:** 28.05.2026  
**Kullanılan Model:** Gemini 3.1 Pro (High) & Manuel Müdahale  

### Yapılan İşlemler:
1. **Kurumsal Tasarım Altyapısı (Base UI):** Projenin istatistiki analiz ve haritalandırma amacına uygun, devlet/emniyet ciddiyetinde, güven veren bir "Kurumsal Dark-Blue" tema altyapısı kuruldu. Arka plan `#1e293b` tonlarına çekildi, yazı fontu olarak `Roboto` entegre edildi.
2. **Emniyet Navbar & Kalkan Logosu:** Bootstrap Icons projeye dahil edilerek sol üst köşeye güveni temsil eden bir kalkan simgesi yerleştirildi.
3. **Bağımlılık Çözümü:** Kayıt ve giriş formlarındaki e-posta validasyonu için eksik olan `email_validator` Python kütüphanesi sisteme yüklendi ve çalışma ortamı hatasız hale getirildi.

## AI Geliştirme Günlüğü - Oturum 5
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **Harita Alanı Sınırlandırılması:** Harita Ankara (Çankaya/Kızılay odaklı) simülasyon alanıyla (`southWest: 39.8800, 32.8000`, `northEast: 39.9500, 32.8800`) sınırlandırıldı. `maxBounds`, `minZoom` ve `maxBoundsViscosity` eklenerek kullanıcının sınır dışına kayması engellendi.
2. **Simülasyon Paneli Arayüzü (Hybrid Grid):** `app/templates/main/index.html` dosyası tamamen yenilenerek jürinin beğeneceği modern bir simülasyon paneline dönüştürüldü.
   - Sol tarafa kategorilerine göre renkli kenarlık/rozetler içeren kaydırılabilir interaktif ihbar kartları yerleştirildi.
   - Sağ tarafa **CartoDB Dark Matter** tabanlı taktiksel karanlık harita katmanı entegre edildi.
   - Üst tarafa dinamik ihbar sayısı ve sistem durumu rozetleri içeren kurumsal bir karşılama bandı yerleştirildi.
3. **İnteraktif Harita Odaklanma:** Sol listedeki ihbar kartlarına tıklandığında haritanın pürüzsüz animasyonla o koordinata odaklanmasını ve marker balonunun (popup) otomatik açılmasını sağlayan dinamik JavaScript mekanizması yazıldı.
4. **Sayfalama (Pagination) Altyapısı:** Ana sayfa ihbar listesinde `Flask-SQLAlchemy`'nin `paginate()` yöntemi kullanılarak sayfa başına 5 ihbar sınırı getirildi. Sol ihbar listesinin altına kurumsal temayla uyumlu Bootstrap 5 sayfalama navigasyonu entegre edilerek hem backend hem frontend tarafında sayfalama gereksinimi tamamlandı.

## AI Geliştirme Günlüğü - Oturum 6
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **Hata Yönetimi Altyapısı (Global Error Handling):** `app/main/errors.py` oluşturuldu. `main_bp.app_errorhandler` dekoratörleri kullanılarak 404 (Sayfa Bulunamadı) ve 500 (Sunucu Hatası) HTTP durum kodları için global hata yakalayıcıları tanımlandı ve `app/main/__init__.py` üzerinden Blueprint'e bağlandı.
2. **404 Hata Arayüzü (`404.html`):** `app/templates/errors/404.html` dosyası oluşturuldu. `base.html` şablonundan miras alınarak projenin kurumsal koyu lacivert kimliğine uygun, açıklayıcı ve kullanıcının ana sayfaya güvenle dönmesini sağlayan estetik bir arayüz tasarlandı.
3. **500 Hata Arayüzü (`500.html`):** `app/templates/errors/500.html` dosyası oluşturuldu. `base.html` şablonundan miras alınarak kurumsal koyu lacivert temalı, teknik destek/kurtarma yönlendirmeli profesyonel bir sistem hatası arayüzü tasarlandı.

## AI Geliştirme Günlüğü - Oturum 7
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **Docker Altyapısı Entegrasyonu:** Projeyi her ortamda sorunsuz şekilde çalıştırabilmek ve dağıtmak amacıyla Dockerizasyon altyapısı hazırlandı.
   - `python:3.12-slim` tabanlı, Gunicorn WSGI sunucusu ile uygulamayı ayağa kaldıran optimize edilmiş bir `Dockerfile` oluşturuldu.
   - Geliştirme ve yayına alma aşamalarında kolaylık sağlaması için, ortam değişkenlerini (environment) ve `5000:5000` port yönlendirmesini barındıran `docker-compose.yml` dosyası yazıldı.
   - `.venv`, `__pycache__`, yerel sqlite veritabanı dosyaları ve yedeklerin konteyner içerisine kopyalanmasını önleyerek imaj boyutunu küçülten `.dockerignore` dosyası eklendi.
2. **Büyük Tasarım Maratonu ve Kapanış Değerlendirmesi:**
   - **Genel Değerlendirme:** Proje, başlangıçtaki "sıfır tasarım, salt fonksiyonel altyapı" yaklaşımından, jüri önünde tam not alacak kurumsal kalitede bir komuta/simülasyon paneline dönüştürüldü.
   - **Kazanımlar ve Öğrenilenler:**
     - **Hibrit Tasarım ve Veri Entegrasyonu:** Jinja2 JSON veri adası mimarisi sayesinde JavaScript ile sunucu verisi sıfır hata ve yüksek güvenlik ile eşleştirildi.
     - **Etkileşimli Harita Kontrolleri:** Harita sınırlandırma ve interaktif odaklanma mekanizması, hem taktiksel görünümü zenginleştirdi hem de kullanıcı deneyimini (UX) üst seviyeye taşıdı.
     - **Mimarinin Gücü:** Application Factory Pattern ve Blueprint yapısının, projenin büyüdüğü aşamalarda (Örn: Hata yönetimi, sayfalama ve Dockerization) ne kadar modüler ve sürdürülebilir bir geliştirme sağladığı bizzat tecrübe edildi. SafeZone artık üretime (production) hazır, kusursuz bir proje haline geldi!

## AI Geliştirme Günlüğü - Oturum 8
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **Şifre Sıfırlama Formları Altyapısı:** `app/auth/forms.py` dosyasına e-posta talebi için `ResetPasswordRequestForm` ve yeni şifre tanımlama için `ResetPasswordForm` formları eklendi.
2. **Güvenli Token Oluşturma ve Doğrulama (itsdangerous):** `app/models.py` içindeki `User` modeline Flask'ın güvenli serializer mimarisini (`itsdangerous.URLSafeTimedSerializer`) kullanan `get_reset_password_token` ve `verify_reset_password_token` metotları eklenerek güvenli, süreli şifre sıfırlama token yapısı entegre edildi.
3. **Şifre Sıfırlama Rotaları ve Geliştirici Modu:** `app/auth/routes.py` içine `/reset_password_request` ve `/reset_password/<token>` rotaları eklendi. Geliştirici dostu simülasyon ortamında linkin terminale (`print()`) basılması ve arayüzde Türkçe bilgilendirici flash mesaj gösterilmesi sağlandı.
4. **Şifre Sıfırlama Arayüz Şablonları:** `app/templates/auth/login.html` sayfasına şık bir "Şifremi Unuttum" bağlantısı eklendi. Kurumsal koyu lacivert temamıza uygun `reset_password_request.html` ve `reset_password.html` form sayfaları tasarlanıp oluşturuldu.

## AI Geliştirme Günlüğü - Oturum 9
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **CSS Variables (:root) ile Çift Tema Yapısı:** `app/templates/base.html` içerisine açık (krem `#fdfbf7` & toz pembe `#db7093`) ve koyu (derin siyah `#0a0a0a` & su yeşili `#00fa9a`) temaları yöneten kapsamlı bir `:root` CSS değişken yapısı eklendi.
2. **Navbar Tema Değiştirme Butonu:** Üst navigasyon barının sağ kısmına şık bir Güneş/Ay (`bi-sun-fill`/`bi-moon-stars-fill`) ikonu olan dinamik bir tema seçici butonu yerleştirildi.
3. **JS LocalStorage ve Tema Senkronizasyonu:** Kullanıcının seçtiği temanın tarayıcı hafızasında saklanması (`localStorage`) ve sayfa geçişlerinde ekranın anlık titremesini engellemek için `<head>` içine anlık tema yükleme scripti entegre edildi.
4. **Dinamik Coğrafi Harita Katmanı Değişimi:** Tema toggled olduğunda tetiklenen özel `themeChanged` JS olayı sayesinde, Leaflet harita katmanının CartoDB Voyager (Açık) ve CartoDB Dark Matter (Koyu) harita görselleriyle anında ve pürüzsüzce yer değiştirmesi sağlandı. Harita marker popup balonları ve diğer tüm bileşenler değişkenlere bağlanarak mükemmel renk uyumu elde edildi.

## AI Geliştirme Günlüğü - Oturum 10
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **Harita Taktik Mavi Filtresi:** Koyu modda haritanın zifiri siyah olmasını önlemek ve sokak hatlarının daha net seçilmesini sağlamak amacıyla, `.leaflet-layer` katmanına koyu mavi / taktiksel bir ton kazandıran özel bir CSS `filter` (`hue-rotate(200deg) saturate(1.4) brightness(0.85) contrast(1.2)`) uygulandı.
2. **Kedi İkonu (bi-cat-fill) Marker Tasarımı:** Harita üzerindeki standart pin ikonları kaldırılarak, Bootstrap Icons kedi simgesini (`bi-cat-fill`) kullanan yuvarlak, modern ve parlayan özel Leaflet `L.divIcon` yapısı tanımlandı.
3. **Kategorilere Göre Dinamik Renk/Glow Kontrolü:** Kedi ikonlarının, ihbar kategorisine göre dinamik renklerde neon ışıklarla parlaması sağlandı:
   - Kritik/Asayiş İhbarları: Parlayan Neon Kırmızı Kedi (`cat-kirmizi`)
   - Trafik/Kaza İhbarları: Parlayan Limon Sarısı Kedi (`cat-sari`)
   - Şüpheli Durum İhbarları: Parlayan Siber Cyan Kedi (`cat-cyan`)
   - Genel/Diğer İhbarlar: Parlayan Su Yeşili Kedi (`cat-yesil`)
   - İkonlar üzerine gelindiğinde büyüme (`transform: scale(1.15)`) ve daha şiddetli parlama (`box-shadow`) animasyonları entegre edildi.

## AI Geliştirme Günlüğü - Oturum 11
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **Sahte Simülasyon İhbar Rotaları (/incident/fake):** `app/main/routes.py` içerisine yalnızca giriş yapmış kullanıcıların (`@login_required`) erişebileceği `/incident/fake` POST rotası eklendi.
   - Ankara/Çankaya sınırları içerisinde (`39.8800` - `39.9500` enlem, `32.8000` - `32.8800` boylam) rastgele koordinatlar üreten bir algoritma yazıldı.
   - Kategorilere (Asayiş, Trafik, Şüpheli Durum, Genel) uygun rastgele başlıklar, detaylı Türkçe açıklamalar ve Çankaya'ya uygun mahalle isimleri üreten bir mock generator entegre edilerek `Incident` modeliyle veritabanına kayıt sağlandı.
2. **AJAX Tetikleme Butonu Entegrasyonu:** Sol panelde (col-lg-4) ihbar listesinin hemen üzerine şık, kurumsal temamıza uygun (Açık modda pembe, koyu modda neon su yeşili parlayan) `"🚨 Simülasyon İhbarı Tetikle"` butonu eklendi.
3. **AJAX (Fetch API) ve Dinamik Yenileme:** Buton tetiklendiğinde sayfa yenilenmeden arka planda istek göndermesini sağlayan Fetch API JS kodu yazıldı. İhbar başarıyla oluşturulduktan sonra ekranın otomatik tazelenerek yeni ihbarın kedi ikonuyla haritaya yerleşmesi sağlandı.

## AI Geliştirme Günlüğü - Oturum 12
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **404 Sayfasında Nostaljik Tuğla Kırma (DX-Ball) Entegrasyonu:** `app/templates/errors/404.html` sayfası jüriyi eğlendirecek interaktif bir oyun alanına dönüştürüldü.
2. **HTML5 Canvas ve Dinamik Temalı Tasarım:** Sayfaya 400x300px boyutlarında şık bir `<canvas>` alanı yerleştirildi. Canvas'ın arka planı ve kenarlıkları sistem değişkenlerimize (`var(--card-bg)`, `var(--accent-color)`) bağlanarak, açık modda toz pembe/krem, koyu modda ise parlayan neon su yeşili kenarlıklı siyah renkte açılması sağlandı.
3. **Vanilla JS Oyun Algoritması:** Top fiziği, klavye/fare dinleyicileriyle kontrol edilen raket (paddle), çarptığında kırılan renkli tuğla (brick) dizilimleri saf JavaScript ile kodlandı.
4. **Akıllı Yönlendirme (Auto-Redirect):** Oyun sonlandığında (Kazanma veya Kaybetme durumunda) canvas ekranında şık bir "Sınır İhlali Çözüldü" veya "Bağlantı Kesildi" mesajı basılması ve 3 saniye sonra kullanıcının otomatik olarak güvenli alana (Ana Sayfa) yönlendirilmesi sağlandı. Aynı zamanda yedek olarak alttaki "Güvenli Bölgeye Dön" butonu aktif bırakıldı.

## AI Geliştirme Günlüğü - Oturum 13
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **Haritadan Tıklama ile Koordinat Alma (UX Modernizasyonu):** `app/templates/main/create_incident.html` dosyası tamamen yenilenerek form ve harita yan yana gelecek şekilde modern bir siber konsol düzenine kavuşturuldu.
2. **Readonly Koordinat Alanları:** Enlem (latitude) ve boylam (longitude) girdi alanları `readonly` yapılarak el ile veri girişi kapatıldı, tasarımsal olarak arka plana itilerek form bütünlüğü sağlandı.
3. **Çankaya Coğrafi Sınır Güvenlik Duvarı:** Leaflet harita tıklama dinleyicisine (`map.on("click")`) koordinat filtreleme mantığı eklendi:
   - Seçilen konum Çankaya simülasyon sınırları (`39.8800` - `39.9500` enlem, `32.8000` - `32.8800` boylam) içerisindeyse enlem/boylam alanları otomatik doldurulur ve haritaya yeşil bir "Seçilen Konum" markeri yerleştirilir.
   - Sınırlar dışına tıklanırsa, form güncellenmez ve ekranda şık, parlayan Bootstrap Toast/Alert benzeri özel bir *"Sınır İhlali: Sadece SafeZone Güvenli Bölge (Çankaya) sınırları içerisine ihbar bırakabilirsiniz!"* uyarısı fırlatılır.
4. **Dinamik Harita Temaları:** Olay bildirme haritası da temaya göre otomatik olarak değişecek şekilde `themeChanged` olay dinleyicisi ile CartoDB Voyager ve CartoDB Dark Matter katmanlarıyla senkronize edildi.

## AI Geliştirme Günlüğü - Oturum 14
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **Harita Görünürlük İyileştirmesi:** `app/templates/main/create_incident.html` dosyasındaki koyu mod harita katmanı filteri hafifletilerek (`brightness(0.95)`, `contrast(1.1)`) sokakların (Bahçelievler, Mebusevleri vb.) ve etiketlerin çok daha net görünmesi sağlandı.
2. **Mahalle Seçimli 'flyTo' Mekanizması:** 'Mahalle Adı' girdi alanı açılır liste (`<select>`) haline getirildi. Kızılay, Bahçelievler, Tunalı Hilmi, Anıttepe, Maltepe mahalleleri eklendi. Kullanıcı mahalle seçtiği an haritanın o konuma pürüzsüzce uçmasını sağlayan `map.flyTo()` kodu yazıldı ve koordinatlar otomatik dolduruldu.
3. **Kedi Maskot Estetikleri:**
   - **Ana Sayfa (breathe):** `base.html` Navbar marka adının yanına hafifçe nefes alarak uyuyan sempatik bir kedi ikonu (`bi-cat` + `animate-breathe`) yerleştirildi.
   - **Olay Bildir Sayfası (glowing-cat):** `create_incident.html` sayfa başlığının yanına gözleri neon ışıkla parlayan, tetikte duran bir kedi maskotu (`bi-cat-fill` + `glowing-cat-header`) yerleştirildi.

## AI Geliştirme Günlüğü - Oturum 15
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **Açılır Liste (select/option) Okunabilirlik Düzeltmesi:** `app/templates/main/create_incident.html` dosyasında yer alan mahalle seçim listesi (`<select>` ve altındaki `<option>` elemanları) için tarayıcı varsayılanlarını ezen özel CSS kuralları tanımlandı. Koyu modda arka planın temiz bir koyu gri (`#1a1a1a`) ve yazıların beyaz (`#ffffff`), açık modda ise arka planın krem ve yazıların koyu kahve olması sağlanarak okunabilirlik sorunu tamamen çözüldü.
2. **Gönder Butonu (Submit) Konum ve Hizalama Düzeltmesi:** Formun en altındaki 'Olay Bildir' butonunun alt kısımdan kesilmesini önlemek amacıyla, kartın alt boşlukları (`margin-bottom: 2rem`) artırıldı, kartın taşma kontrolü (`overflow: visible`) düzenlendi ve butonun üst boşluğu (`mt-4`) optimize edilerek sayfada tam ve pürüzsüz görünmesi sağlandı.

## AI Geliştirme Günlüğü - Oturum 16
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **Akıllı Metin Girdili Mahalle Seçimi (select -> input):** `create_incident.html` sayfasındaki Mahalle Adı açılır menüsü (`select`) tamamen kaldırılarak yerine klavyeden serbestçe yazılabilir, koyu/açık temayla tam uyumlu standart bir `<input type="text">` alanı yerleştirildi.
2. **JavaScript Dinamik Coğrafi Akıllı Eşleştirme:** Kullanıcının bu alana yazı yazarken veya odaktan çıktığında (`oninput`/`onblur`) çalışacak bir JS mekanizması geliştirildi. Girilen metin Türkçe karakter duyarsız veya küçük harfe çevrilerek analiz edilir; eğer 'kızılay', 'bahçeli', 'tunalı', 'anıttepe' veya 'maltepe' ifadelerini içeriyorsa harita anında o mahallenin koordinatlarına pürüzsüzce uçar (`map.flyTo`), koordinat alanlarını (readonly) otomatik doldurur ve haritada yeşil konum marker'ını günceller.

## AI Geliştirme Günlüğü - Oturum 17
**Tarih:** 30.05.2026  
**Kullanılan Model:** Gemini 3.5 Flash (Medium)  

### Yapılan İşlemler:
1. **Çoklu Dil Desteği (TR/EN Localization) Altyapısı:** Uygulamaya tam uyumlu, dinamik bir dil desteği entegre edildi. Dil verilerini Türkçe ve İngilizce karşılıklarıyla (Navbar linkleri, ihbar formları, simülasyon butonu, sınır uyarısı, oyun metinleri vb.) yöneten `app/main/translations.py` modülü sıfırdan oluşturuldu.
2. **Dil Değiştirme Rotası ve Küresel Jinja2 Context Processor:** `app/main/routes.py` dosyasına, kullanıcının dil tercihini `session['lang']` üzerinde saklayan `/set_language/<lang>` rotası eklendi. Tüm şablonların ek işleme gerek kalmadan dil verilerini tüketebilmesi için `@main_bp.app_context_processor` dekoratörü tanımlanarak `_` çeviri fonksiyonu ve seçili dil değişkeni küresel hale getirildi (Varsayılan: Türkçe - `tr`).
3. **Arayüz Entegrasyonları (Jinja2 & HTML/JS Güncellemeleri):**
   - `base.html` navigasyon barına şık ve kurumsal bir dil değiştirme butonu ("TR" veya "EN") eklendi.
   - `base.html`, `index.html`, `create_incident.html` ve `404.html` şablonlarındaki tüm kritik başlık, etiket, buton, uyarı metinleri ve mini DX-Ball oyun içi durum mesajları dinamik çeviri yapısına bağlandı.