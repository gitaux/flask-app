# -*- coding: utf-8 -*-
# app/home/views.py

from flask import abort, render_template
from flask_login import current_user, login_required

from . import home


@home.route('/')
def welcome():
    """
    Render the homepage template on the / route
    :return:
    """
    return render_template('home/welcome.html', title='Welcome')

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route.
    :return:
    """
    return render_template('home/dashboard.html', title='Dashboard')

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    return render_template('home/admin_dashboard.html', title='Dashboard')
