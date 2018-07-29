"""
The login system for players uses SQLAlchemy.  The code has been adapted and 
reworked from a tutorial by PrettyPrinted to suit this game environment.  
Exception handling was added to def signup() function to inform a player 
that a user name has already been taken.  The username for the game is pulled
from the SQL database and pushed to the game.html
"""

import os
import json
import time
from flask import Flask, redirect, render_template, request, flash, session, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'some_secret'
# I've used a relative path from sqlite to my database.db file
# becase an absolute path failed to work.
# I believe that this was because of an error in the path neame or sqlite3
# doesn't like spaces in my windows 10 folder path names.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view ='login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class SignUpForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    


#1
def write_to_file(filename, data):
    #Handel the process of writing data to a text file
    with open(filename, "a") as file:
        file.writelines(data)

#2
def loadUsers():
    """ 
    Gets our player names from a text file used to store
    their wrong guesses: 
    """
    answer_given = []
    with open("data/users.txt", "r") as player_answer:
        answer_given = player_answer.readlines()
        return answer_given


#3
def storePlayerName(username, answer_given):
    """ 
    Stores player names and wrong answer to a txt file.  Adapted
    from chat app tutorial that maintained the chat history: 
    """
    write_to_file("data/users.txt", "({0} {1} {2}\n".format(
        datetime.now().strftime("%H:%M:%S"),
        username.title(),
        answer_given))



#4
def loadRiddles():
    """ 
    Read the riddles from the riddles txt: 
    """
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
        return data



#5 Redundant function from development
def validateAnswer(riddle, answer):
    """
    check the player's answer against our own
    """
    answer_given = request.form["message"].lower()
    return answer_given


#6
def countRiddles():
    """
    Count the number or riddle in out list so we
    can keep score! This makes our count dynamic.
    """
    numRiddles = len(loadRiddles())
    return numRiddles



#8 
def writeScore(username, score):
    """
    User's score has to be saved before refreshing the page,
    or score resets to 0 for each new riddle on page refresh.
    """
    write_to_file("data/score.txt", "{0} - {1} - {2}\n".format(
        datetime.now().strftime("%H:%M:%S"),
        username.title(),
        score))



@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        flash('Logged in as '+ username)
        
    return render_template('index.html')




@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm() 
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                session['username'] = (form.username.data)
                return redirect(url_for('game', username = session['username']))

        flash(u'This is invalid username or password', 'error')
        

    return render_template('login.html', form = form, error = error)






@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    # The code below was modified to return an exception if a duplicate user name was
    # attempted, during a new user registration.
    try: 
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            flash('The data is confimred. A new user has been added')
            

    except Exception:
        flash('This username already exists, please click register above and try a different name.')

    return render_template('signup.html', form=form)



    

@app.route('/game/<username>', methods=["GET", "POST"])
@login_required
def game(username):  
    
    
    
    # riddles are stored in JSON file and are indexed
    data = []

    # Load JSON data from riddles.json
    data = loadRiddles()
        
        
    # Set the first riddle
    riddleNumber = 0

    
    # Set the user score to start at 0
    score = 0
    

    if request.method == "POST":
    
        writeScore(username, score)

        # post riddle number x to the the the game template and
        # increment the riddle by 1 each time a correct answer is
        # given.
        riddleNumber = int(request.form["riddleNumber"])

        # I plan to only show the image if the user gets the riddle
        # either right, or wrong. It serves two purposes:
        # A reward as well as a hint.
        image = int(request.form["riddleNumber"]) 
        
        
        # Call validateAnswer function
        answer_given = validateAnswer("riddle", "answer")
            
            
        
        if data[riddleNumber]["answer"] == answer_given:
            score += 1
            riddleNumber += 1
            image=riddleNumber

            render_template("game.html", riddle_me_this=data, riddleNumber=riddleNumber)

            # Test to return message as fixed html
            # render_template("game.html", riddle_me_this=data, riddleNumber=riddleNumber, score=f"Well done! Thats '{score}' out of '{countRiddles()}' right!")  
                  
            #flash the number of riddles correct with the dynaminc total of the
            # number of riddles. Yes! The code will update for any number of riddles.
            flash(f'Well done! Thats {score} out of {countRiddles()} right!')

            
                      
        else:
            # The project breif requires that the incorrect answer be
            # stored and presented back to the players.  See funcion
            # storePlayerName above, to see this happening.
            storePlayerName(username, answer_given)
            flash(f'Incorrect {username}, \"{answer_given}" is not the right answer... \nTry again?')

    if request.method == "POST": 
        if answer_given ==  "mole" and countRiddles() == 2:      # development if statement  
        #if answer_given ==  "hour-glass" and riddleNumber == countRiddles():  # production if statement
            flash(f'Excellent, youve reached the end. Thats {score} out of {countRiddles()} right!')
            time.sleep(3)                
            return render_template('leaderboard.html')
        
   
    return render_template("game.html", username=username, riddle_me_this=data, riddleNumber=riddleNumber)
    




@app.route('/leaderboard/<username>')
@login_required
def leaderboard(username):
    return render_template("leaderboard", name=current_user.username)





@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('username', None)
    return redirect(url_for('index'))




if __name__ == '__main__':
    """
    assign a port ID works with both vscode
    and Heroku
    """
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            #debug set to true to help during development
            debug=True)