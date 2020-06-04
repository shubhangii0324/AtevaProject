from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about-us')
def aboutus():
    return render_template('about-us.html')

@app.route('/reset-password')
def resetpassword():
    return render_template('reset-password.html')

if __name__ == '__main__':
    app.run()
