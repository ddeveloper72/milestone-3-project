import os
import json
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

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



if __name__ == '__main__':
    """
    assign a port ID works with both vscode
    and Heroku
    """
    app.run(host=os.getenv('IP'),
            port=os.getenv('PORT'),
            #debug set to true to help during development
            debug=True)