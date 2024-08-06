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