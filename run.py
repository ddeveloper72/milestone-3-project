"""
The login system for players uses SQLAlchemy.  The code has been adapted and 
reworked from a tutorial by PrettyPrinted to suit this game environment.  
Exception handling was added to def signup() function to inform a player 
that a user name has already been taken.
"""

import os
import json
from flask import Flask, redirect, render_template, request, flash, session, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


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
    write_to_file("data/users.txt", f"{username}'s answer was {answer_given}\n")



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




@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm() 

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('game', username=form.username.data))

        flash('This is invalid username or password')
        

    return render_template('login.html', form = form)






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
        
        
    # beging at first riddle
    riddleNumber = 0

    if request.method == "POST":
    
        # post riddle number x to the the the game template and
        # increment the riddle by 1 each time a correct answer is
        # given.
        riddleNumber = int(request.form["riddleNumber"])

        
        # Call validateAnswer function
        answer_given = validateAnswer("riddle", "answer")
            
            
        
        if data[riddleNumber]["answer"] == answer_given:
             riddleNumber += 1

        else:
            # The project breif requires that the incorrect answer be
            # stored and presented back to the players.  See funcion
            # storePlayerName above, to see this happening.
            storePlayerName(username, answer_given)
    
   
    return render_template("game.html", username=username, riddle_me_this=data, riddleNumber=riddleNumber)





@app.route('/leaderboard/<username>')
@login_required
def leaderboard():
    return render_template("leaderboard", name=current_user.username)





@app.route('/logout')
@login_required
def logout():
    logout_user()
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