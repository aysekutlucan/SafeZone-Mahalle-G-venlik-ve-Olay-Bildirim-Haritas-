from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired, Optional

class IncidentForm(FlaskForm):
    title = StringField('Başlık', validators=[DataRequired()])
    description = TextAreaField('Açıklama')
    category = SelectField('Kategori', choices=[
        ('hirsizlik', 'Hırsızlık'),
        ('kaza', 'Kaza'),
        ('supheli', 'Şüpheli Durum'),
        ('diger', 'Diğer')
    ], validators=[DataRequired()])
    neighborhood_name = StringField('Mahalle Adı', validators=[DataRequired()])
    latitude = FloatField('Koordinat Enlemi (Latitude)', validators=[Optional()])
    longitude = FloatField('Koordinat Boylamı (Longitude)', validators=[Optional()])
    submit = SubmitField('Olay Bildir')
