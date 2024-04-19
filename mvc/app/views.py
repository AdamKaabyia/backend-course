from flask import render_template, session, send_from_directory
from . import app
from .controllers import login_controller, sales_data_controller, logout_controller


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_login():
    return login_controller()


@app.route('/show-data')
def show_data():
    sales_data = sales_data_controller()
    if isinstance(sales_data, list):
        return render_template('show_data.html', sales=sales_data)
    return sales_data


@app.route('/logout')
def logout():
    return logout_controller()


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    return response
