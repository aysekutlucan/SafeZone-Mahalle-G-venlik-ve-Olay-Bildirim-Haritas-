from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.main import main_bp
from app.main.forms import IncidentForm
from app.models import Incident

@main_bp.route('/')
def index():
    incidents = Incident.query.order_by(Incident.created_at.desc()).all()
    return render_template('main/index.html', incidents=incidents)

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
