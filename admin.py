from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app
from model import *



admin = Admin(app, name='MyshopFlask', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session, category='Account'))
admin.add_view(ModelView(Category, db.session, category='Product'))
admin.add_view(ModelView(Subcategory, db.session, category='Product'))
admin.add_view(ModelView(Subcategory_type, db.session, category='Product'))
admin.add_view(ModelView(Brand, db.session, category='Product'))