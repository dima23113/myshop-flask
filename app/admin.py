from flask_admin.contrib.sqla import ModelView
from flask_wtf.file import FileField, FileAllowed, FileRequired
from decimal import Decimal
from slugify import slugify


class SetSlugField(ModelView):

    def on_model_change(self, form, model, is_created):
        model.slug = slugify(model.name)
        return super().on_model_change(form, model, is_created)

class SetEmptyProductField(ModelView):
    def on_model_change(self, form, model, is_created):
        model.slug = slugify(model.name)
        model.price = Decimal(model.price).quantize(Decimal('1.00'))
        model.price_discount = model.price
        return super().on_model_change(form, model, is_created)

    form_extra_fields = {
        'Изображение': FileField('image', validators=[FileAllowed(['jpeg', 'png', 'webp'])])
    }