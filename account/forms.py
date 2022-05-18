from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class ChangeAddressForm(FlaskForm):
    country = StringField('Страна', validators=[DataRequired()])
    city = StringField('Город', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    zip_code = StringField('Индекс', validators=[DataRequired()])


class ChangeBioForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамилия', validators=[DataRequired()])


class ChangePhoneNumberForm(FlaskForm):
    phone = StringField('Номер телефона', validators=[DataRequired()])


class PasswordChangeForm(FlaskForm):
    password = StringField('Номер телефона', validators=[DataRequired()])
    password2 = StringField('Номер телефона', validators=[DataRequired()])


class MailingChangeForm(FlaskForm):
    mailing_yes = BooleanField('Рассылка e-mail уведомлений', validators=[DataRequired], default=True)


class ChangeEmailForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
