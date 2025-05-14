from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')  #route par défaut
def hello():
    return render_template('hello.html')

@app.route('/hello2')
def hello():
    return render_template('hello2.html')

@app.route('/hello3')
def hello():
    return render_template('hello2.html')

if __name__ == '__main__':
    app.run(debug=True)