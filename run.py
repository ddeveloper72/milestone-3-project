#!/usr/bin/env python3.6
"""
The login system for players uses SQLAlchemy.  The code has been adapted and 
reworked from a tutorial by PrettyPrinted to suit this game environment.  
Exception handling was added to def signup() function to inform a player 
that a user name has already been taken.  The username for the game is pulled
from the SQL database and pushed to the game.html
"""
import os
import os.path
os.path.exists('player-scores.txt')
import glob
import shutil
import json
import datetime
from shutil import copyfile
from pathlib import Path
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask import Flask, redirect, render_template, request, flash, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.validators import InputRequired, Length
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm
from functools import wraps


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Flask LoginManager Models and FlaskForms                                                                 #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('username', validators=[
                           InputRequired(), Length(min=3, max=15)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class SignUpForm(FlaskForm):
    username = StringField('username', validators=[
                           InputRequired(), Length(min=3, max=15)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=8, max=80)])


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# App Views                                                                                                #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# 1

def loginRequired(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('To access this, please log in first', 'bg-danger')
            return redirect(url_for('login'))
    
    return wrap

# 2

def write_to_file(filename, data):
    """
    Handel multiple function calls to write data to a text file
    """
    with open(filename, "a") as file:
        file.writelines(data)

# 3

def write_to_json(filename, data):
    """
    Handel multiple function calls to write data to a json file
    """
    with open(filename, 'w+') as json_data:
        json.dump(data, json_data)

# 4

def loadRiddles():
    """ 
    Read the riddles from the riddles txt: 
    """
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
        return data

# 5

def validateAnswer(riddle, answer):
    """
    check the player's answer against our own
    """
    answer_given = request.form["answer"].lower()
    return answer_given


# 6

def countRiddles():
    """
    Count the number or riddle in out list so we can keep score! This makes our count dynamic.
    """
    numRiddles = len(loadRiddles())
    return numRiddles

# 7

def newUserScore(username, score):
    """
    User's inital score has to be created. This is set to 0 and the score file is
    created on successful login. The file is stored in a directory consisting of the
    user's name, which will allow unique instances of the game, so long as the 
    player names are unique. This is insured but the login registration form, which 
    specifies unique registration names. 
    """
    data = {}
    data['game'] = []
    data['game'].append({
        'date': datetime.now().strftime("%d/%m/%Y"),
        'username': f'{username}',
        'score': (score)
    })

    """
    Every instance of the game, requiers a dedicated score board for the game. A pre-existing scoreboard json file is
    removed at login, if it is already present.  The users score alwasy starts from 0.
    """
    dir = f'data/player_data/{username}/'
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        shutil.rmtree(dir)  
        os.makedirs(dir)

    """ 
    The score board will alwasy write over itself, permitting the score to increase. 
    """
    write_to_json(f'data/player_data/{username}/scores.json', data)


# 8

def writeScore(username, score):
    """
    User's score has to be saved after answering each riddle.  To do this, we rewrite the JSON file.
    """
    data = {}
    data['game'] = []
    data['game'].append({
        'date': datetime.now().strftime("%d/%m/%Y"),
        'username': f'{username}',
        'score': (score)
    })

    write_to_json(f'data/player_data/{username}/scores.json', data)


# 9

def loadScore(username):
    """ 
    Read player score: 
    """
    with open(f'data/player_data/{username}/scores.json', 'r') as json_data:
        data = json.load(json_data)
        return data

# 10

def leaderborardCheck():
    """
    The game requires at least 3 scores to exist, to carry out the top 3 scores
    function, scores_list() at the end of the game for the first ever player. 
    As a work around, a scores-template.txt file is used to create the 
    player-scores.txt file, on first login of the first
    player.
    """
    import os
    try:
        if os.stat('data/player-scores.txt'):
            os.stat('data/player-scores.txt')
    except:
        shutil.copyfile('data/score_template/player-scores.txt',
                        'data/player-scores.txt')
        # only if the file doesn't exist


# 11

def write_LeaderboardScores(score, username, date):
    """
    Writes all the different payer's score to player-scores.txt
    """
    file = open('data/player-scores.txt', 'a')
    file.write(f"\nScore: {(score)}, Player: {username}, Date: {date}")
    file.close()


# 12

def scores_list():
    """
    Get player-scores.txt and convert to tuples.  Sort the score in each tuple 
    to return the top 3 scores to the leader board.
    """
    li = [i.replace(",", "").replace("'", "").split()
          for i in open('data/player-scores.txt').readlines()]
    # picks out the score from (Score:, 10, Player:, MyName, Date:, 16/08/2018)
    li.sort(key=lambda tup: tup[1])
    li.sort(reverse=True)  # sorts scores from highest to lowest

    # Cleanup the tuple data by striping and replacing unwanted characters, for rendering to html
    first = str(li[0])[1:-1].replace("'", " ").replace(",", " ")
    second = str(li[1])[1:-1].replace("'", " ").replace(",", " ")
    third = str(li[2])[1:-1].replace("'", " ").replace(",", " ")
    fourth = str(li[3])[1:-1].replace("'", " ").replace(",", " ")
    fith = str(li[4])[1:-1].replace("'", " ").replace(",", " ")
    return first, second, third, fourth, fith


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Security Conscious Views for Session, Login, Register. Logout & 404                                      #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

@app.route('/')
def index():
    score = 0   # our score is set to 0
    if 'username' in session:
        username = session['username']
        newUserScore(session['username'], score)  # Create a score tracker.
        flash('You are logged in as ' + username)
        return redirect(url_for('game', username=session['username']))

    return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('You are currently logged out', 'alert-success')
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    score = 0   

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                session['username'] = (form.username.data)
                session['logged_in'] = True
                # Create a leaderboard if one doesn't already exist.
                leaderborardCheck()
                # Create a score tracker.
                newUserScore(form.username.data, score)
                return redirect(url_for('game', username=session['username']))

        flash('This is an invalid username or password', 'alert-danger')

    return render_template('login.html', form=form, error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ 
    Register a new user.  On successful registration, create user name and password in database.
    creat a new user score card.  If a duplicate username from session is prepped for write to the
    database, Exception calls a session rollback to prevent duplicate username and prompts a warning.  
    """

    form = SignUpForm()
    error = None
    score = 0 

    try:
        if form.validate_on_submit():  
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            user = User(username=form.username.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            session['username'] = (form.username.data)
            session['logged_in'] = True 
            leaderborardCheck()
            newUserScore(form.username.data, score)  

            flash('You are now loged in', 'alert-success')
            return redirect(url_for('game', username = session['username']))
            
    except Exception:
        db.session.rollback()
        flash('This username already exists. Please choose again', 'alert-danger')
    
    return render_template('signup.html', form = form, error = error)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Game and Leader-board Views                                                                              #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


@app.route('/game/<username>', methods=["GET", "POST"])
@loginRequired
def game(username):

    # riddles are stored in JSON file and are indexed
    data = []

    # Load JSON data from riddles.json
    data = loadRiddles()

    # Set the first riddle
    riddleNumber = 0

    # Get the current score from the scores json file
    score = (loadScore(username)['game'][0]['score'])

    # Get the current date for logging with the score at the end of our game
    date = datetime.now().strftime("%d/%m/%Y")

    if request.method == "POST":

        # post riddle number x to the the the game template and
        # increment the riddle by 1 each time a correct answer is
        # given.
        riddleNumber = int(request.form["riddleNumber"])
        # Call validateAnswer function
        answer_given = validateAnswer("riddle", "answer")

        if data[riddleNumber]["answer"] in answer_given:

            score += 1
            riddleNumber += 1

            # Write scores to a file that contains our username, score for each question and
            # time the question was answered.
            writeScore(username, score)

            # Flash the number of riddles correct with the dynaminc total of the
            # number of riddles. Yes! The code will update for any number of riddles.
            flash(
                f'Well done! Thats a score of {score} out of {countRiddles()} riddles right!')

            # Determins what happens next when the last riddle is used.
            if riddleNumber == countRiddles():
                write_LeaderboardScores(score, username, date)
                return redirect(f'/leaderboard/{username}/{score}')

        else:
            flash(
                f'Sorry {username}, \"{answer_given}\" is not the right answer... \nIt was \"{data[riddleNumber]["answer"]}\". \nLets try another.\nUse the picture clue above for help')
            riddleNumber += 1

            # Determins what happens next when the last riddle is used.
            if riddleNumber == countRiddles():
                write_LeaderboardScores(score, username, date)
                return redirect(f'/leaderboard/{username}/{score}')

    return render_template("game.html", username=username, riddle_me_this=data, riddleNumber=riddleNumber)


@app.route('/leaderboard/<username>/<score>')
@loginRequired
def leaderboard(username, score):
    scores = score
    scores = scores_list()

    return render_template("leaderboard.html", username=current_user.username, player_scores=scores)



if __name__ == '__main__':
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            debug=False)
