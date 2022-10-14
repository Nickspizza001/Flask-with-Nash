from app import app
from flask import render_template

@app.route('/admin')
def adminDashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/about')
def admin_about():
    return render_template('admin/about.html')


@app.route('/admin/profile')
def profile():
    return render_template('/admin/profile.html')


