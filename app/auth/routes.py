from flask import render_template, redirect, url_for, flash, request, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from flask_login import login_user, logout_user, current_user, login_required
from urllib.parse import urlsplit

from app import db
from app.auth import auth_bp
from app.auth.forms import RegistrationForm, LoginForm, ResetPasswordRequestForm, ResetPasswordForm, AvatarUploadForm
from app.models import User

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Kayıt başarılı! Şimdi giriş yapabilirsiniz.', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html', title='Kayıt Ol', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password_hash and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or urlsplit(next_page).netloc != '':
                if user.role in ['admin', 'yetkili']:
                    # TODO: İleride admin paneline yönlendirme yapılacak
                    next_page = url_for('main.index')
                else:
                    next_page = url_for('main.index')
            return redirect(next_page)
        else:
            flash('Geçersiz e-posta veya şifre', 'danger')
            
    return render_template('auth/login.html', title='Giriş Yap', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = AvatarUploadForm()
    if form.validate_on_submit():
        file = form.avatar.data
        if file:
            filename = secure_filename(file.filename)
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            if ext in ['.jpg', '.jpeg', '.png']:
                avatars_dir = os.path.join(current_app.root_path, 'static', 'avatars')
                os.makedirs(avatars_dir, exist_ok=True)
                
                # Delete any old avatar files with different extensions
                for existing_ext in ['.jpg', '.jpeg', '.png']:
                    existing_path = os.path.join(avatars_dir, f"user_{current_user.id}{existing_ext}")
                    if os.path.exists(existing_path):
                        try:
                            os.remove(existing_path)
                        except Exception:
                            pass
                
                new_filename = f"user_{current_user.id}{ext}"
                file_path = os.path.join(avatars_dir, new_filename)
                file.save(file_path)
                
                from flask import session
                lang = session.get('lang', 'tr')
                if lang == 'en':
                    flash('Profile picture successfully updated!', 'success')
                else:
                    flash('Profil resmi başarıyla güncellendi!', 'success')
                    
                return redirect(url_for('auth.profile'))
            else:
                from flask import session
                lang = session.get('lang', 'tr')
                if lang == 'en':
                    flash('Invalid file format!', 'danger')
                else:
                    flash('Geçersiz dosya formatı!', 'danger')
                    
    return render_template('auth/profile.html', title='Profilim', form=form)


@auth_bp.route('/remove_avatar', methods=['POST'])
@login_required
def remove_avatar():
    avatars_dir = os.path.join(current_app.root_path, 'static', 'avatars')
    deleted = False
    for ext in ['.jpg', '.jpeg', '.png']:
        file_path = os.path.join(avatars_dir, f"user_{current_user.id}{ext}")
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                deleted = True
            except Exception:
                pass
                
    from flask import session
    lang = session.get('lang', 'tr')
    
    if deleted:
        if lang == 'en':
            flash('Profile picture successfully removed!', 'success')
        else:
            flash('Profil fotoğrafı başarıyla kaldırıldı!', 'success')
    else:
        if lang == 'en':
            flash('No custom profile picture found to remove.', 'warning')
        else:
            flash('Kaldırılacak özel profil fotoğrafı bulunamadı.', 'warning')
            
    return redirect(url_for('auth.profile'))


@auth_bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = user.get_reset_password_token()
            reset_url = url_for('auth.reset_password', token=token, _external=True)
            print("\n" + "="*50)
            print("SafeZone Şifre Sıfırlama Talebi Alındı!")
            print(f"Kullanıcı: {user.username}")
            print(f"Sıfırlama Linki: {reset_url}")
            print("="*50 + "\n")
            flash('Şifre sıfırlama linki terminale başarıyla gönderildi (Geliştirici Modu). Lütfen terminal konsolunu kontrol edin.', 'success')
            return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html', title='Şifre Sıfırlama Talebi', form=form)


@auth_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        flash('Şifre sıfırlama linki geçersiz veya süresi dolmuş.', 'danger')
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.password_hash = generate_password_hash(form.password.data)
        db.session.commit()
        flash('Şifreniz başarıyla sıfırlandı! Yeni şifrenizle giriş yapabilirsiniz.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', title='Şifreyi Sıfırla', form=form)
