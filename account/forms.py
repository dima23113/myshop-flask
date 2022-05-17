from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ChangeAddressForm(FlaskForm):
    country = StringField('Страна', validators=[DataRequired()])
    city = StringField('Город', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    zip_code = StringField('Индекс', validators=[DataRequired()])
