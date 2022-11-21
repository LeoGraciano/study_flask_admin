import os

from decouple import config
from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy

from app.config import Config

ROOT_DIR = os.path.dirname(__file__)
db = SQLAlchemy()
admin = Admin(name='SuporteBan', template_mode="bootstrap4")
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = "info"


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)

    # DATABASE
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # ADMIN
    from app import dashboard
    admin.init_app(app)
    dashboard.init_app(admin)

    # ROUTERS
    @ app.route('/')
    def index():
        return 'Hello World'

    @ app.route('/login')
    def login():
        return 'Login Page'

    return app
