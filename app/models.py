from datetime import datetime
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app

from flask_login import UserMixin

from app import db


class User(UserMixin, db.Model):
    """Kullanıcı modeli. Flask-Login için UserMixin'den türer."""

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    role = db.Column(db.String(20), nullable=False, default='user')

    # İlişkiler
    incidents = db.relationship('Incident', backref='author', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def get_reset_password_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_password_token(token, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token, max_age=expires_sec)
        except Exception:
            return None
        return User.query.get(data['user_id'])


class Incident(db.Model):
    """Olay bildirim modeli."""

    __tablename__ = 'incident'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)
    neighborhood_name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Incident {self.title}>'


class Neighborhood(db.Model):
    """Mahalle modeli. Güvenlik puanı ve olay sayısını tutar."""

    __tablename__ = 'neighborhood'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    safety_score = db.Column(db.Integer, nullable=False, default=100)
    total_incidents = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'<Neighborhood {self.name}>'
