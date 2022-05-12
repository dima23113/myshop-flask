from mimetypes import init
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:11081998@localhost/flask-shop'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['SECRET_KEY'] = "Gre3QmyUu7PD-xvtBKmsow"
    db.init_app(app)   
    migrate = Migrate(app, db)
    from .admin import SetSlugField
    from model import User, Category, Subcategory, Subcategory_type, Brand
    admin = Admin(app, name='MyshopFlask', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session, category='Account'))
    admin.add_view(SetSlugField(Category, db.session, category='Product'))
    admin.add_view(SetSlugField(Subcategory, db.session, category='Product'))
    admin.add_view(SetSlugField(Subcategory_type, db.session, category='Product'))
    admin.add_view(SetSlugField(Brand, db.session, category='Product'))


    from shop.shop import shop_bp
    app.register_blueprint(shop_bp, url_prefix='/shop')
    return app
