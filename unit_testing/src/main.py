from flask import Flask, jsonify, request, g
from flask_httpauth import HTTPBasicAuth
import sqlite3

app = Flask(__name__)
auth = HTTPBasicAuth()

DATABASE = 'database.db'

# Dictionary to store user credentials
users = {
    "user": "password"
}

# Function to get the password for a given username
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

# Function to get the database connection from g
# g = Flask global namespace for storing data during a request
# or create one if it does not exist
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Function to close the database connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Public route
@app.route('/')
def index():
    # Return a welcome message for the public page
    return jsonify(message="Welcome to the public page!")

# Protected route to get data from the database
@app.route('/data', methods=['GET'])
@auth.login_required
def get_data():
    # Query the database for all rows in the data table
    cur = get_db().cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    # Return the rows as a JSON response
    return jsonify(rows)

# Protected route to add data to the database
@app.route('/data', methods=['POST'])
@auth.login_required
def add_data():
    # Get the new data from the request body
    new_data = request.json
    # Insert the new data into the database
    cur = get_db().cursor()
    cur.execute("INSERT INTO data (name, value) VALUES (?, ?)", (new_data['name'], new_data['value']))
    get_db().commit()
    # Return a success message
    return jsonify(message="Data added successfully"), 201

if __name__ == '__main__':
    # Create the database table if it doesn't exist using application context
    with app.app_context():
        db = get_db()
        db.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, value TEXT)')
        db.commit()
    # Run the Flask app in debug mode
    app.run(debug=True)
