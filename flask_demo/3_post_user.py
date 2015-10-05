# coding=utf-8
from flask import Flask, render_template, request, Response

app = Flask(__name__)

users = [
    {'name': 'Vasya', 'age': 21},
    {'name': 'Petya', 'age': 22},
    {'name': 'Tolya', 'age': 20}
]

@app.route('/users', methods=['GET'])
def print_user():
    return render_template('template1.html', users=users)

@app.route('/users', methods=['POST'])
def add_user():
    user = {'name': request.form['name'], 'age': int(request.form['age'])}
    users.append(user)
    return str(user), 201

if __name__ == '__main__':
    app.run(debug=True)
