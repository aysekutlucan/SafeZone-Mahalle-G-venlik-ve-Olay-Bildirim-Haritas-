from flask import render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from urllib.parse import urlsplit

from app import db
from app.auth import auth_bp
from app.auth.forms import RegistrationForm, LoginForm
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

@auth_bp.route('/profile')
@login_required
def profile():
    # current_user is already available in the template, we can just pass it implicitly
    # The incidents will be accessible via current_user.incidents
    return render_template('auth/profile.html', title='Profilim')
