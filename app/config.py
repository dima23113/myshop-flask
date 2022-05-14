import os
from dotenv import load_dotenv 

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Gre3QmyUu7PD-xvtBKmsow')
    UPLOAD_FOLDER = os.path.join(basedir, 'core/static/uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:11081998@localhost/flask-shop'
    FLASK_ADMIN_SWATCH = 'cerulean'