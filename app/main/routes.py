from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
import random
from app import db
from app.main import main_bp
from app.main.forms import IncidentForm
from app.models import Incident

@main_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    all_incidents = Incident.query.order_by(Incident.created_at.desc()).all()
    pagination = Incident.query.order_by(Incident.created_at.desc()).paginate(page=page, per_page=5, error_out=False)
    incidents = pagination.items
    return render_template('main/index.html', incidents=incidents, pagination=pagination, all_incidents=all_incidents)

@main_bp.route('/incident/new', methods=['GET', 'POST'])
@login_required
def new_incident():
    form = IncidentForm()
    if form.validate_on_submit():
        incident = Incident(
            title=form.title.data,
            description=form.description.data,
            category=form.category.data,
            neighborhood_name=form.neighborhood_name.data,
            latitude=form.latitude.data,
            longitude=form.longitude.data,
            author=current_user
        )
        db.session.add(incident)
        db.session.commit()
        flash('Olay başarıyla bildirildi!', 'success')
        return redirect(url_for('main.index'))
    return render_template('main/create_incident.html', form=form)

@main_bp.route('/incident/fake', methods=['POST'])
@login_required
def create_fake_incident():
    # Çankaya boundaries
    lat = round(random.uniform(39.8800, 39.9500), 6)
    lng = round(random.uniform(32.8000, 32.8800), 6)
    
    neighborhoods = ["Kızılay", "Çankaya", "Tunalı Hilmi", "Bahçelievler", "Ayrancı", "Yıldız", "Maltepe", "Esat", "Söğütözü", "Odtü"]
    
    fake_data = [
        {
            "category": "Asayiş",
            "titles": ["Şüpheli Çanta İhbarı", "Sokak Kavgası", "Gürültü ve Taşkınlık", "Market Hırsızlığı Girişimi"],
            "descriptions": [
                "Park bankının altında sahipsiz bir sırt çantası tespit edildi. Güvenlik çemberi oluşturulması talep ediliyor.", 
                "Mahalle arasında iki grup arasında fiziksel arbede yaşandı. Çevre sakinleri huzursuz.",
                "Gece geç saatlerde sokak ortasında yüksek sesli müzik ve taşkınlık yapıldı. Kolluk birimleri bilgilendirildi.",
                "Süpermarket çıkışında şüpheli bir şahsın reyondan ürün sakladığı fark edildi, devriye ekipleri müdahale etti."
            ]
        },
        {
            "category": "Trafik",
            "titles": ["Maddi Hasarlı Kaza", "Hatalı Park / Yol Kapanması", "Sinyalizasyon Arızası", "Aşırı Hız ve Yarış"],
            "descriptions": [
                "İki binek araç kavşakta çarpıştı, yaralı yok. Araçlar yolun tek şeridini kapatıyor.",
                "Sokak girişine çift sıra park eden bir araç nedeniyle çöp kamyonu ve ambulans geçiş yapamıyor.",
                "Ana cadde üzerindeki trafik ışıkları çalışmıyor, trafikte yoğun aksama ve tehlike mevcut.",
                "Bulvar üzerinde gece yarısı makas atan ve aşırı hız yapan modifiyeli araçlar bildirildi."
            ]
        },
        {
            "category": "Şüpheli Durum",
            "titles": ["Plakasız Araç Gözlemi", "Şüpheli Şahıs Devriyesi", "Boş Binada Hareketlilik", "Dolandırıcılık Şüphesi"],
            "descriptions": [
                "Ara sokakta 2 saattir park halinde bekleyen plakasız ve camları siyah filmli bir araç ihbar edildi.",
                "Apartman girişlerini gözetleyen ve kapıları zorlayan kapüşonlu bir şüpheli şahıs görüldü.",
                "Kentsel dönüşüm nedeniyle boşaltılan binada gece saatlerinde el feneri ışıkları ve sesler fark edildi.",
                "Mahalle esnafını dolaşarak sahte vakıf adına yardım toplayan şüpheli şahıslar gözlemlendi."
            ]
        },
        {
            "category": "Genel",
            "titles": ["Logar Kapağı Çökmesi", "Sokak Lambası Arızası", "Su Patlağı / Boru Sızıntısı", "Sokak Hayvanı Acil Durum"],
            "descriptions": [
                "Ana yol üzerinde bulunan logar kapağı çökmüş durumda, sürücüler için ciddi kaza riski var.",
                "Park içindeki aydınlatma direklerinin hiçbiri çalışmıyor, bölge tamamen karanlıkta kalmış.",
                "Kaldırım kenarındaki şebeke borusundan yoğun su sızıntısı var, yol göle dönmek üzere.",
                "Yaralı ve halsiz durumda sokak köşesinde yatan bir sokak köpeği için belediye ekiplerine haber verildi."
            ]
        }
    ]
    
    selected_option = random.choice(fake_data)
    category = selected_option["category"]
    
    idx = random.randint(0, len(selected_option["titles"]) - 1)
    title = selected_option["titles"][idx]
    description = selected_option["descriptions"][idx]
    
    neighborhood = random.choice(neighborhoods)
    
    incident = Incident(
        title=title,
        description=description,
        category=category,
        neighborhood_name=neighborhood,
        latitude=lat,
        longitude=lng,
        author=current_user
    )
    
    db.session.add(incident)
    db.session.commit()
    
    return {"status": "success", "message": "Simülasyon ihbarı başarıyla tetiklendi!"}, 200
