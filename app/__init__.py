from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import config

# Eklenti nesneleri (app dışında oluşturulur, init_app ile bağlanır)
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app(config_name='default'):
    """Application Factory: Flask uygulamasını oluşturur ve yapılandırır."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Eklentileri başlat
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Blueprint'leri kaydet
    from app.main import main_bp
    app.register_blueprint(main_bp)

    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Flask-Login: oturumdan kullanıcıyı yükle
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
