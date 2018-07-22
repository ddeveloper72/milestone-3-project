import os
import json
from flask import Flask, redirect, render_template, request, flash, session, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.secret_key = 'some_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
Bootstrap(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class SignUpForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    

def write_to_file(filename, data):
    #Handel the process of writing data to a text file
    with open(filename, "a") as file:
        file.writelines(data)


def loadUsers():
    """ 
    Lets get our player names from our databse file: 
    """
    with open("data/users.txt", "r") as file:
        data = json.load(file)
        return data

def loadRiddles():
    """ 
    Read the riddles from the riddles txt: 
    """
    with open("data/riddles.json", "r") as file:
        data = json.load(file)
        return data

def validateAnswer(riddle, answer):
    """
    check the player's answer against our own
    """
    return riddle["answer"] in answer.lower()

""" def addOnScore(username): 

"""



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm() 

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('game'))

        return '<h1>invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form = form)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
     
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1> The data is confimred </h1>'

    return render_template('signup.html', form=form)
    

@app.route('/game')
@login_required
def game():   
    return render_template("game.html")   


@app.route('/leaderboard')
@login_required
def leaderboard():
    return render_template("leaderboard")



if __name__ == '__main__':
    """
    assign a port ID works with both vscode
    and Heroku
    """
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            #debug set to true to help during development
            debug=True)