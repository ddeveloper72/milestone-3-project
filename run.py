import os
import json
from flask import Flask, redirect, render_template, request, flash, session, abort

app = Flask(__name__)
app.secret_key = 'some_secret'

def write_to_file(filename, data):
    #Handel the process of writing data to a text file
    with open(filename, "a") as file:
        file.writelines(data)


def validateName(users):
    """
    Test to validate that a user name has not already been 
    registered
    """
    users = request.form["username"]
    with open("data/users.txt", "r") as file:
        data = json.load(file)
        return data              
    
    



def loadUsers():
    """ 
    Lets get our player names from our databse file: 
    """
    with open("data/users.json", "r") as file:
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
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()



@app.route('/<username>/', methods=["GET", "POST"])
def game(username):   
    

    return render_template("game.html")   


@app.route('/end')
def end():
    return render_template("end.html", page_title="Your Leader-Board!")



if __name__ == '__main__':
    """
    assign a port ID works with both vscode
    and Heroku
    """
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            #debug set to true to help during development
            debug=True)