from decouple import config


class Config():
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URI')
    DATABASE_TRACK_MODIFICATIONS = config('DATABASE_TRACK_MODIFICATIONS')
    SECRET_KEY = config('SECRET_KEY')
    FLASK_ADMIN_SWATCH = 'cerulean'
