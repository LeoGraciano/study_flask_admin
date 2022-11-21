from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from wtforms import fields
from app import db
from app.models import Profile, Task, User
from werkzeug.security import generate_password_hash, check_password_hash


class UserView(ModelView):
    column_editable_list = ('name', 'email', 'profile')
    form_edit_rules = ('name', 'email', 'tasks', 'profile')
    form_create_rules = ('name', 'email', 'password')
    column_exclude_list = ('password', 'tasks')
    column_searchable_list = ('name', 'email')
    details_modal = True
    create_modal = True
    edit_modal = True

    column_display_all_relations = True
    column_filters = ('name', 'email', 'profile')

    form_extra_fields = {
        "password": fields.PasswordField("Password"),
    }

    column_list = ['name', 'email', 'profile', 'tasks', ]
    inline_models = [Profile]

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(form.password.data)


def init_app(admin):

    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Task, db.session))
    admin.add_view(ModelView(Profile, db.session))
