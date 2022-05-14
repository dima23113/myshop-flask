from flask_admin.contrib.sqla import ModelView
from flask_wtf.file import FileField, FileAllowed, FileRequired
from decimal import Decimal
from slugify import slugify
from model import Product, ProductSize, ImageProduct
from flask_admin.model.form import InlineFormAdmin
from werkzeug.utils import secure_filename
import os 

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads')

class ProductSizesInlineForm(InlineFormAdmin):
    form_columns=['name', 'qty', 'id']

class ProductImgInlineForm(InlineFormAdmin):

    form_columns=['id']
    def postprocess_form(self, form):
        form.images_product = FileField('images_product', validators=[FileAllowed(['jpeg', 'png', 'webp'])])
        return super().postprocess_form(form)
    
    def on_model_change(self, form, model, is_created):
        img = form.images_product.data
        model.img = os.path.abspath(os.path.join(basedir, img.filename))
        model.name = secure_filename(img.filename)
        model.mimetype = img.mimetype
        img.save(os.path.join(basedir, img.filename))
        return super().on_model_change(form, model, is_created)

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
    form_excluded_columns = ('img', 'name_img', 'mimetype', 'price_discount', 'product_images', 'product_sizes', 'created')

    inline_models = (ProductImgInlineForm(ImageProduct), ProductSizesInlineForm(ProductSize))