import json

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



