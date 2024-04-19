from flask import session, redirect, url_for, request, jsonify, render_template
from .models import get_sales_data, check_user_credentials


def login_controller():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username and password and check_user_credentials(username, password):
        session['logged_in'] = True
        return jsonify({'success': True}), 200
    return jsonify({'error': 'Invalid credentials'}), 400


def sales_data_controller():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return get_sales_data()  # This should return a list of sales data


def logout_controller():
    session.pop('logged_in', None)
    # This will now render the logout page template
    return render_template('logout.html')

