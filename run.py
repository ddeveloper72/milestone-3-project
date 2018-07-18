import os
import json
from flask import Flask, redirect, render_template, request, flash

app = Flask(__name__)

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
    with open("data/users.json", "r") as file:
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




@app.route('/', methods=["GET", "POST"])
def start():

    if request.method == "POST":    
        """
        Gets a user login name, checks to see if it has already
        been used and if not, writes it to the users.json file.
        """ 
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
                 


    return render_template("start.html")
            


    
    
    
        
    

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