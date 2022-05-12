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
    slug = db.Column(db.String(55))
    subcategories = relationship('Subcategory', backref='category')

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
    slug = db.Column(db.String(55))
    category_id = db.Column(db.Integer, ForeignKey('category.id'))
    subcategories_type = relationship('Subcategory_type', backref='subcategorytype')

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
    slug = db.Column(db.String(55))
    subcategory_id = db.Column(db.Integer, ForeignKey('subcategory.id'))

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
    slug = db.Column(db.String(256))
    description = db.Column(db.Text)

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
    category_id = db.Column(db.Integer, ForeignKey('category.id'))
    subcategory_id = db.Column(db.Integer, ForeignKey('subcategory.id'))
    subcategory_type_id = db.Column(db.Integer, ForeignKey('subcategory_type.id'))
    brand_id = db.Column(db.Integer, ForeignKey('brand.id'))
    name = db.Column(db.String(256))
    slug = db.Column(db.String(256))
    description = db.Column(db.Text)
    specifications = db.Column(db.Text)
    price = db.Column(db.Float(decimal_return_scale=2))
    available = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    article = db.Column(db.String(256))
    image = db.Column(db.Text)
    price_discount = db.Column(db.Float(decimal_return_scale=2))

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        if not 'price_discount' in kwargs:
            kwargs['price_discount'] = self.price
        return super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'Product id: {self.id}, product_name: {self.name}'