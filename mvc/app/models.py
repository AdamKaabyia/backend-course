users_db = {
    'admin': {
        'username': 'admin',
        'password': 'admin',  # In a real app, passwords should be hashed!
    }
}


sales_db = [
    {'date': '2023-01-01', 'item': 'Widget A', 'cost': 100},
    {'date': '2023-01-02', 'item': 'Widget B', 'cost': 200},
    {'date': '2023-01-02', 'item': 'Widget B', 'cost': 300},
    {'date': '2023-01-01', 'item': 'Widget A', 'cost': 400},
    {'date': '2023-01-02', 'item': 'Widget B', 'cost': 500},
    {'date': '2023-01-02', 'item': 'Widget B', 'cost': 600},
    {'date': '2023-01-01', 'item': 'Widget A', 'cost': 700},
    {'date': '2023-01-02', 'item': 'Widget B', 'cost': 800},
    {'date': '2023-01-02', 'item': 'Widget B', 'cost': 900},
    {'date': '2023-01-01', 'item': 'Widget A', 'cost': 1000},
    {'date': '2023-01-02', 'item': 'Widget B', 'cost': 1100},
    {'date': '2023-01-02', 'item': 'Widget B', 'cost': 1700},
]


def check_user_credentials(username, password):
    user = users_db.get(username)
    if user and user['password'] == password:
        return True
    return False


def get_sales_data():
    return sales_db
