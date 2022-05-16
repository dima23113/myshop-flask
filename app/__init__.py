from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_debugtoolbar import DebugToolbarExtension
from flask_thumbnails import Thumbnail
import os

db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__name__))

def create_app():
    # Создаем приложение, добавляем переменные конфигурации

    app = Flask(__name__, static_folder='../static', template_folder='../template/')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:11081998@localhost/flask-shop'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['SECRET_KEY'] = "Gre3QmyUu7PD-xvtBKmsow"
    app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'app/static/uploads')
    app.debug = True
    app.config['THUMBNAIL_MEDIA_ROOT'] = '../media'
    app.config['THUMBNAIL_MEDIA_URL'] = '/static/'
    db.init_app(app)
    migrate = Migrate(app, db)
    toolbar = DebugToolbarExtension(app)
    thumb = Thumbnail(app)
    

    # Добавляем модели в админку и сортируем их по категориям

    from .admin import SetSlugField, SetEmptyProductField
    from model import User, Category, Subcategory, Subcategory_type, Brand, Product
    admin = Admin(app, name='MyshopFlask', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session, category='Account'))
    admin.add_view(SetSlugField(Category, db.session, category='Product'))
    admin.add_view(SetSlugField(Subcategory, db.session, category='Product'))
    admin.add_view(SetSlugField(Subcategory_type, db.session, category='Product'))
    admin.add_view(SetSlugField(Brand, db.session, category='Product'))
    admin.add_view(SetEmptyProductField(Product, db.session, category='Product'))

    # Регистрируем приложения

    from shop.shop import shop_bp
    app.register_blueprint(shop_bp, url_prefix='/')
    return app
