# File: app/routes/dashboard.py

from flask import render_template
from app import app
from flask_login import login_required

@app.route('/dashboard')
@login_required
def dashboard():
    # Your logic to fetch user-specific data goes here
    return render_template('dashboard.html')
