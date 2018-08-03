"""
The login system for players uses SQLAlchemy.  The code has been adapted and 
reworked from a tutorial by PrettyPrinted to suit this game environment.  
Exception handling was added to def signup() function to inform a player 
that a user name has already been taken.  The username for the game is pulled
from the SQL database and pushed to the game.html
"""

import os
import shutil
import json
import datetime
import time
from flask import Flask, redirect, render_template, request, flash, session, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
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


# SQL classes for managing user names and login data, providing a basic level
# of security for our player's data.
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
    

# Backend Python functions
#1
def write_to_file(filename, data):
    """
    Handel multiple function calls to write data to a text file
    """
    with open(filename, "a") as file:
        file.writelines(data)

#2
def write_to_json(filename, data):
    """
    Handel multiple function calls to write data to a json file
    """
    with open(filename, 'w+') as json_data:
        json.dump(data, json_data)

#3
def loadUsers():
    """ 
    Gets our player names from a text file used to store
    their wrong guesses: 
    """
    answer_given = []
    with open("data/users.txt", "r") as player_answer:
        answer_given = player_answer.readlines()
        return answer_given

#4
def storePlayerName(username, answer_given):
    """ 
    Stores player names and wrong answer to a txt file.  Adapted
    from chat app tutorial that maintained the chat history: 
    """
    write_to_file("data/users.txt", "{0} {1} {2}\n".format(
        datetime.now().strftime("%H/%M/%S"),
        username.title(),
        answer_given))

#5
def loadRiddles():
    """ 
    Read the riddles from the riddles txt: 
    """
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
        return data

#6
def validateAnswer(riddle, answer):
    """
    check the player's answer against our own
    """
    answer_given = request.form["answer"].lower()
    return answer_given


#7
def countRiddles():
    """
    Count the number or riddle in out list so we
    can keep score! This makes our count dynamic.
    """
    numRiddles = len(loadRiddles())
    return numRiddles

#8
def newUserScore(username, score):
    """
    User's iniotal score has to be created.
    This is set to 0 and the score file is
    created on successful login. The file is
    stored in a directory consisting of the
    user's name, which will allow unique 
    instances of the game, so long as the 
    player names are unique. This is insured
    but the login registration form, which 
    specifies unique registration names. 
    """
    data ={}
    data['game'] = []
    data['game'].append({
        'date': datetime.now().strftime("%d/%m/%Y"),
        'username': '{}'.format("username"),
        'score': (score)
    })
    
    """
    Every instance of the game, requiers a dedicated
    score board for the game. A pre-existing score,json file is
    removed at login, if it is already present. 
    So, our score alwasy starts from 0.
    """
    dir = 'data/player_data/{}/'.format("username")   
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        shutil.rmtree(dir)           #removes all the subdirectories!
        os.makedirs(dir)

    # The score board will alwasy write over itself, permitting the score
    # to increase.
    write_to_json("data/player_data/{}/scores.json".format("username"), data)



#9
def writeScore(username, score):
    """
    User's score has to be saved after answering each
    riddle.  To do this, we rewrite the JSON file.
    """
    data ={}
    data['game'] = []
    data['game'].append({
        'date': datetime.now().strftime("%d:%m:%Y"),
        'username': '{}'.format("username"),
        'score': (score)
    })

    write_to_json("data/player_data/{}/scores.json".format("username"), data)


#10
def loadScore(username):
    """ 
    Read player score: 
    """
    with open("data/player_data/{}/scores.json".format("username"), "r") as json_data:
        data = json.load(json_data)
        return data


#11
def write_LeaderboardScores(score, username, date):
    """
    Writes all the different payer's score to player-scores.txt
    """
    file  =  open("data/player-scores.txt", "a")
    file.write("Score: {0}, Player: {1}, Date: {2}".format("score","username","date") + '\n')
    file.close()

#12
def get_leaderboardScores():
    """
    Get player-scores.txt and return the data to the leader board
    """
    scores = []
    with open("data/player-scores.txt", "r") as player_scores:
        scores = player_scores.readlines()        
    return scores
    

# The Flask decorators below, process and render data to our front end
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        flash('Logged in as '+ username + '/nClick home on the nav bar to return to game')
        return redirect(url_for('game', username = session['username']))
        
    return render_template('index.html')




@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm() 
    error = None
    score = 0   # our score at login is 0

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                session['username'] = (form.username.data)
                newUserScore(form.username.data, score) # Create a score tracker.
                return redirect(url_for('game', username = session['username']))

        flash(u'This is an invalid username or password', 'error')        

    return render_template('login.html', form = form, error = error)






@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    error = None
    
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
        flash(u'This username already exists, please click register above and try a different name.', 'error')

    return render_template('signup.html', form=form, error=error)



    

@app.route('/game/<username>', methods=["GET", "POST"])
@login_required
def game(username):     
    
    # riddles are stored in JSON file and are indexed
    data = []

    # Load JSON data from riddles.json
    data = loadRiddles()
        
        
    # Set the first riddle
    riddleNumber = 0

    
    # Get the current score from the scores json file
    score = (loadScore(username)['game'][0]['score'])


    if request.method == "POST":
    
        # post riddle number x to the the the game template and
        # increment the riddle by 1 each time a correct answer is
        # given.
        riddleNumber = int(request.form["riddleNumber"])

        # I plan to only show the image if the user gets the riddle
        # either right, or wrong. It serves two purposes:
        # A reward as well as a hint.
        # image = int(request.form["riddleNumber"]) 
        
        
        # Call validateAnswer function
        answer_given = validateAnswer("riddle", "answer")
            
            
        
        if data[riddleNumber]["answer"] == answer_given:
            score += 1            
            riddleNumber += 1
            
            # Write scores to a file that contains our username, score for each question and
            # time the question was answered.            
            writeScore(username, score)      
            
            # Flash the number of riddles correct with the dynaminc total of the
            # number of riddles. Yes! The code will update for any number of riddles.
            flash('Well done! Thats {0} out of {1} right!'.format("score", "countRiddles()"))
            
            

            if riddleNumber == countRiddles():  # production if statement
                
                flash('Excellent, you\'ve reached the end. Now to compare your score with other players...')
                           
                time.sleep(3)                
                return redirect('/leaderboard/{0}/{1}'.format(username, score))
    
        else:
            # The project breif requires that the incorrect answer be
            # stored and presented back to the players.  See funcion
            # storePlayerName above, to see this happening.
            storePlayerName(username, answer_given)
            flash('Incorrect {username}, \"{answer_given}" is not the right answer... \nTry again?'.format("username", "answer_given"))

      
    
    return render_template("game.html", username=username, riddle_me_this=data, riddleNumber=riddleNumber)

@app.route('/leaderboard/<username>/<score>')
@login_required
def leaderboard(username, score):
    date = datetime.now().strftime("%d/%m/%Y")
    write_LeaderboardScores(score, username, date)
    
    
    scores = get_leaderboardScores()

    return render_template("leaderboard.html", name=current_user.username, player_scores=scores)





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