import os
import json
from flask import Flask, redirect, render_template, request, flash, session, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'some_secret'

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class SignupForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


def write_to_file(filename, data):
    #Handel the process of writing data to a text file
    with open(filename, "a") as file:
        file.writelines(data)


def registerUser():
    """
    Register users for our game, to users.txt
    """
    username = str(request.form['username'])
    password = str(request.form['password']) 

    file = open("data/users.txt", "a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()

def loginUser():
    """
    Login users for our game, verified from out users.txt
    """
    
    username = str(request.form['username'])
    password = str(request.form['password'])

    for line in open("data/users.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0] and password == login_info[1]:
            # If credentials are valid:
            return True
        else:
            # If credentials are invalid:  
            return False 
   


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


@app.route('/login')
def login(): 
    form = LoginForm()      
    return render_template('login.html', form = form)


@app.route('/signup')
def signup():
    form = SignupForm()
    return render_template('signup.html', form=form)
    

@app.route('/game')
def game():   
    return render_template("game.html")   


@app.route('/leaderboard')
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