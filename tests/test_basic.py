from app import create_app


def test_app_exists():
    """Uygulama factory'den app oluşturulabilmeli."""
    app = create_app('testing')
    assert app is not None


def test_app_is_testing():
    """Test konfigürasyonu doğru yüklenmeli."""
    app = create_app('testing')
    assert app.config['TESTING'] is True
