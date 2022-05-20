from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.widgets.core import HiddenInput
from wtforms.validators import DataRequired


class CartUpdateProductForm(FlaskForm):
    qty = StringField('Количество', )
    update = BooleanField('Обновление ко-ва', widget=HiddenInput())


class CartAddProductForm(FlaskForm):
    id_size = StringField('Добавление товара в корзину', widget=HiddenInput())
