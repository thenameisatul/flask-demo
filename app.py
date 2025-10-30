from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_users():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

@app.route('/')
def home():
    users = get_users()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

    return redirect('/')  # Refresh the page to show the new user

if __name__ == '__main__':
    app.run(debug=True)
