# coding=utf-8
from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'name': 'Vasya', 'age': 21},
    {'name': 'Petya', 'age': 22},
    {'name': 'Tolya', 'age': 20}
]

@app.route('/users')
def hello_world():
    return render_template('template1.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
