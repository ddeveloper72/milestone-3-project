from byotest import *

"""
Users will select the game mode, 1 or 2 to either play the game or quit
"""
def game_mode_selection():
    print("To play 'Riddle-Me-This', press 1")
    print("Press 2, to Quit")
    
    option = input("What's your selection: ")
    return option
    
    
def ask_riddles():
    riddles = []
    answers = []
    
    with open("riddles.txt", "r") as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
        if  i%2 == 0:
            riddles.append(text)
        else:
            answers.append(text)
            
    number_of_riddles = len(riddles)
    riddles_and_answers = zip(riddles, answers)
    
    score = 0
    
    for riddle, answer in riddles_and_answers:
        guess = input(riddle + "> ")
        if guess == answer:
            score += 1
            print("Brilliant answer!")
            print(score)
        else:
            print("No, thats wrong!")
        
    print("you got {0} correct out of {1}".format(score, number_of_riddles))

def game_loop():
    while True:
        option = game_mode_selection()
        if option == "1":
            ask_riddles()
        elif option == "2":
            break
        else:
            print("Invalid option")   
        print("")
        
game_loop()