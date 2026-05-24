import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Temel konfigürasyon sınıfı."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'gizli-anahtar-degistir')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'safezone.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Geliştirme ortamı konfigürasyonu."""
    DEBUG = True


class TestingConfig(Config):
    """Test ortamı konfigürasyonu."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    """Üretim ortamı konfigürasyonu."""
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
