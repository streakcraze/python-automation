from flask import Flask, jsonify, request, g
from flask_httpauth import HTTPBasicAuth
import sqlite3

app = Flask(__name__)
auth = HTTPBasicAuth()

DATABASE = 'database.db'

users = {
    "user": "password"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return jsonify(message="Welcome to the public page!")

@app.route('/data', methods=['GET'])
@auth.login_required
def get_data():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    return jsonify(rows)

@app.route('/data', methods=['POST'])
@auth.login_required
def add_data():
    new_data = request.json
    cur = get_db().cursor()
    cur.execute("INSERT INTO data (name, value) VALUES (?, ?)", (new_data['name'], new_data['value']))
    get_db().commit()
    return jsonify(message="Data added successfully"), 201

if __name__ == '__main__':
    with app.app_context():
        db = get_db()
        db.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, value TEXT)')
        db.commit()
    app.run(debug=True)