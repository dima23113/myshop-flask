from slugify import slugify
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    first_name = db.Column(db.String(120), nullable=True)
    second_name = db.Column(db.String(120), nullable=True)
    zip_code = db.Column(db.String(20), nullable=True)
    email_mailing = db.Column(db.Boolean, default=False)
    phone = db.Column(db.String(120), nullable=True)
    birthday = db.Column(db.Date, nullable=True)
    address = db.Column(db.String(120), nullable=True)
    city = db.Column(db.String(120), nullable=True)
    country = db.Column(db.String(120), nullable=True)
    amount_of_purchases = db.Column(db.Integer, default=0)

    def __repr__(self) -> str:
        return f'User id: {self.id}, email: {self.email}'



class Category(db.Model):
    __tablename__ = 'category'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55), nullable=False)
    slug = db.Column(db.String(55), unique=True)
    subcategories = relationship('Subcategory', backref='category')
    products = relationship('Product', backref='category_products')

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        return super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'Category id: {self.id}, category_name: {self.name}'

class Subcategory(db.Model):
    __tablename__ = 'subcategory'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55), nullable=False)
    slug = db.Column(db.String(55), unique=True)
    category_slug = db.Column(db.String(55), ForeignKey('category.slug'))
    subcategories_type = relationship('Subcategory_type', backref='subcategorytype')
    products = relationship('Product', backref='subcategory_products')

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        return super().__init__(*args, **kwargs)
    
    def __repr__(self) -> str:
        return f'Subcategory id: {self.id}, subcategory_name: {self.name}'

class Subcategory_type(db.Model):
    __tablename__ = 'subcategory_type'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55), nullable=False)
    slug = db.Column(db.String(55), unique=True)
    subcategory_slug = db.Column(db.String(55), ForeignKey('subcategory.slug'))
    products = relationship('Product', backref='subcategory_type_products')

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        return super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'Subcategory_type id: {self.id}, subcategory_type_name: {self.name}'

class Brand(db.Model):
    __tablename__ = 'brand'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    slug = db.Column(db.String(256), unique=True)
    description = db.Column(db.Text)
    products = relationship('Product', backref='brand_products')
    img = db.Column(db.Text, unique=True, nullable=True)
    name_img = db.Column(db.Text, nullable=True)
    mimetype = db.Column(db.Text, nullable=True)

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        return super().__init__(*args, **kwargs)
    
    def __repr__(self) -> str:
        return f'Brand id: {self.id}, brand_name: {self.name}'


class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    category_slug = db.Column(db.String(256), ForeignKey('category.slug'))
    subcategory_slug = db.Column(db.String(256), ForeignKey('subcategory.slug'))
    subcategory_type_slug = db.Column(db.String(256), ForeignKey('subcategory_type.slug'))
    brand_slug = db.Column(db.String(256), ForeignKey('brand.slug'))
    name = db.Column(db.String(256))
    slug = db.Column(db.String(256))
    description = db.Column(db.Text)
    specifications = db.Column(db.Text)
    price = db.Column(db.Float(decimal_return_scale=2))
    available = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    article = db.Column(db.String(256))
    img = db.Column(db.Text, unique=True, nullable=True,)
    name_img = db.Column(db.Text, nullable=True)
    mimetype = db.Column(db.Text, nullable=True)
    price_discount = db.Column(db.Float(decimal_return_scale=2))
    product_images = relationship('ImageProduct', backref='image_products')
    product_sizes= relationship('ProductSize', backref='prouduct_sizes')
    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        if not 'price_discount' in kwargs:
            kwargs['price_discount'] = self.price
        return super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'Product id: {self.id}, product_name: {self.name}'
    

class ImageProduct(db.Model):
    __tablename__ = 'image_product'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=True)
    name = db.Column(db.Text, nullable=True)
    mimetype = db.Column(db.Text, nullable=True)
    product = db.Column(db.Integer, ForeignKey('product.id'))

    def __repr__(self) -> str:
            return f'Image id: {self.id}, : {self.name}'


class ProductSize(db.Model):
    __tablename__ = 'prouduct_size'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=True)
    qty = db.Column(db.Integer, nullable=True)
    product = db.Column(db.Integer, ForeignKey('product.id'))