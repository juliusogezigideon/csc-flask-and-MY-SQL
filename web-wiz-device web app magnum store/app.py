from flask import Flask, render_template, request, jsonify
import flask_mysqldb

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'varchar'
app.config['MYSQL_PASSWORD'] = 'petty8888'
app.config['MYSQL_DB'] = 'flask_app'

mysql = MySQL(app)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html', use)

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'User added successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)