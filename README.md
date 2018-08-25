

# Milestone 3 Project


## [Riddle Me This](https://ddeveloper72-riddle-me-this.herokuapp.com/)
### by Duncan Falconer for the Code Institute, 2018

## 1. Project Goals:
This project is all about having fun, while making a game which demonstrates Python as the backbone programming language.

The Game is designed to run on Heroku and will facilitate multiple players, playing the same game at the same time.  The players will be able to register their own unique usernames when they log into the game.  Their usernames will be used to tack their progress throughout the game.

A leader-board will show the scores of players from highest to lowest.
## 2 .The UX Design:
### 1. Strategy:
1. Focus:
    * My project is to create a game for lovers of old style  Victorian Era Riddles that have been sourced from the [**Gutenberg Project**](https://www.gutenberg.org/)
2. User Needs:
    - To provide a game that a player can log into, so that   they  will then be able to play by answering a number of  riddles. If a     riddle is answered wrong, the game will    respond with the    player's incorrect answer as well as   provide the correct answer    along with a hint for   answering the next questions.
    - The player's score will be added each time they answer a riddle correctly.  When the game is finished, the player can see their final score along with the scores of other players.
  
3.  Business Objectives:
    - To demonstrate my use of the Python programming language in a game for my graded projects portfolio.
 
### 3. Scope:
1. Focus:
    - Features of this design. The requirements of this project from the brief.
2. Functional Specification:
    1. The player must be able to use a    unique     player   name to play the     game.
    2. The player must also be able to     respond     to a    riddle by being able to    type in an     answer.
    3. There has to be process which checks    the    player's     answer and provides    feedback to them  about their    answer.
    4. The play must be able to see their      score.
    5. The player needs to be asked another      riddle.
    6. The player needs to be able to see  the  scores of other    players along with  their own.
    7. The player needs to be able to play     the     game    again.
       
3. Content Requirements:
    1. The game needs a way for users to   create    a unique  user name; a login     facility.
    2.  This is a riddle game, so it has to     have    a source    of riddles to ask.
    3.  The player must be able to submit    their  answer, so a    answer field and  submit button     is needed.
    4.  A logic engine is needed to check the     player's  answer to the correct answer   for a   riddle, with feedback     provided to     the player,     of a wrong or right         answer.
    5.  The game has to increment the score     for     right   answers.    
    6.  The game has to show a score board  with     the results    from other  players.
### 4. Structure:
1. Focus:
   - What are the steps, the progression/flow of information throughout the game process?

2. Interaction Design:
    1. The player login function -> is a data filter.  It is a process which manages and insures the  player uses a unique player name, or else the game wouldn't work properly.
    2. The unique player is given a riddle to  answer.
    3. If the answer is correct, the score is  added and they are given the next riddle.
    4. If the answer is wrong, they are presented the wrong answer as well as  provided a hint. They are asked to try again.
    5. When the last riddle is answered correctly, the player is shown a leader board  of all the players.
    6. If the player wishes to quit the game at any time, they can log out, or play again by   selecting the Home button on the navigation bar.
   
3. Information Architecture:
    - The processes of this game follows a:    
        - *Start:* Riddle, Answer =    Right, Next Riddle + Score, Answer = Right,    Next Riddle + Score  +1, End
        - *Start:* Riddle, Answer =   Wrong, Next Riddle, Answer = Right, Next  Riddle + Score +1, End
    
### 5. Skeleton:
1. Focus:
    1. How will the information be represented?
    2. How will the user navigate to the   information and features?
2. Interface Design:
    - The best way to show the design, was as in the Wireframes.  See below.
3. Navigational Design:
    - The user follows prompts from the index page to either register or login to play the game.  Once in the game, the page will refresh each time an answer is input, which again prompts the player toward completion of the game.  This then ends with the player being brought to the leader-board.
4. Information Design:
    - The player is prompted by both text and imagery throughout their visit to the game.
     
### 6. Surface:
1. Focus:
    The focus is on the triangular layout of the   page, when viewed  on a large screen device.
    
    - To play the riddle game, a player will need  to register their name and then log into the game.   Information is laid out    clearly with little to no     other page distraction.
2. Visual Design:
    The Bootstrap 4 template used in this project  was from [Start Bootstrap - Coming Soon](https://startbootstrap.com/template-overviews/coming-soon/).   
    
    A    video background of an old style ticking  timepiece, marks the passage of time while the   player deliberates over the     answer to  a   riddle.  

### 7. Wireframes:

![Index](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Index.png "Fig 1 showing Index page")

![Register!](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Register!.png "Fig 2 showing Register page")

![Login here!](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Login_here!.png "Fig 3 showing Log-in page")

![Game](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Game.png "Fig 4 showing Game page")

![Leader-board](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Leaderboard.png "Fig 5 showing Leader-board")



## 3. Game construction:
    1. Code Development
   The project brief was to follow a a pattern of **Test Driven Development**.  A series of tests were written at the start of this project and then the run time function was written, based on the test.

Not all functions were written in this way and these will be followed up with tests.

### Test 1

```python
def test_loadUsers(self):
        """
        test to check that the plyers can be loaded from the
        users file which stores player names and wrong answers.
        """
        users = run.loadUsers()
        self.assertEqual(len(users), 3)
```

### Test 1: Run-time function

```python
def loadUsers():
    """ 
    Gets our player names from a text file used to store their wrong guesses: 
    """
    answer_given = []
    with open("data/users.txt", "r") as player_answer:
        answer_given = player_answer.readlines()
        return answer_given

```
<hr>

### Test 2

```python
def test_storePlayerName(self):
        users = run.storePlayerName()
        self.assertGreater(len(users), 0)  
```

### Test 2: Run-time function

```python
def storePlayerName(username, answer_given):
    """ 
    Stores player names and wrong answer to a txt file.  Adapted from chat app tutorial 
    that maintained the chat history: 
    """
    write_to_file('data/users.txt', f'{datetime.now().strftime("%H:%M:%S")}, {username.title()}, {answer_given}\n')

```

<hr>

### Test 3

```python
def test_loadRiddles(self):
    """
    test to check that the users can be loaded from the
    json file
    """
    riddles = run.loadRiddles()
    self.assertEqual(len(riddles), 14)
```


### Test 3: Run-time function

```python
def loadRiddles():
    """ 
    Read the riddles from the riddles txt: 
    """
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
        return data
```

<hr>

### Test 4

```python
def test_validateAnswer(self):
    """
    test to vslidate the user's answer against our own
    from our json file.
    """
    riddles = run.loadRiddles()
    self.assertEqual(run.validateAnswer(riddles[0],"clock"), True)
    self.assertEqual(run.validateAnswer(riddles[0],"house"), False)
```

### Test 4: Run-time function

```python
def validateAnswer(riddle, answer):
    """
    check the player's answer against our own
    """
    answer_given = request.form["answer"].lower()
    return answer_given
```

<hr>

### Test 5

```python
def test_count_eq(self):
    """Will succeed"""
    self.assertCountEqual(self.result, self.expected)
```

### Test 5: Run-time function

```python
def countRiddles():
    """
    Count the number or riddle in out list so we can keep score! This makes our count dynamic.
    """
    numRiddles = len(loadRiddles())
    return numRiddles
```

<hr>

#### Selection of Specialist Functions
### Run-time function #8

```python
def newUserScore(username, score):
    """
    User's inital score has to be created. This is set to 0 and the score file is created on successful login. 
    """
    data ={}
    data['game'] = []
    data['game'].append({
        'date': datetime.now().strftime("%d/%m/%Y"),
        'username': f'{username}',
        'score': (score)
    })

    """
    Every instance of the game, requiers a dedicated
    score board for the game. A pre-existing score,json file is
    removed at login, if it is already present. 
    So, our score alwasy starts from 0.
    """
    dir = f'data/player_data/{username}/'  
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        shutil.rmtree(dir)           #removes all the subdirectories!
        os.makedirs(dir)

    # The score board will alwasy write over itself, permitting the score
    # to increase.
    write_to_json(f'data/player_data/{username}/scores.json', data)
```
<hr>

### Run-time function #9

```python
def writeScore(username, score):
    """
    User's score has to be saved after answering each
    riddle.  To do this, we rewrite the JSON file.
    """
    data ={}
    data['game'] = []
    data['game'].append({
        'date': datetime.now().strftime("%d/%m/%Y"),
        'username': f'{username}',
        'score': (score)
    })

    write_to_json(f'data/player_data/{username}/scores.json', data)
```
<hr>


## 4. Deployment Instructions:
1. Instructions for deployment to a hosing site: [Heroku](https://www.heroku.com/)
    1. In Heroku - Part 1:
        1. Log into Heroku
        2. Select New and Create new App.
        3. Create a App name, select the region.
            - then Create app.
        4. Select Resources.
            -  then select Find more add-ons.
            - Select Heroku Postgres.
            - Install Heroku Postgres, using the hobby plan.
        5. Return to Personal menu then select ddeveloper72-riddle-me-this.
        6. select Deploy 
            - Note the deployment instructions.
    2. From Cloud 9:
        1. Log in to Heroku: `$ heroku login`
        2. Verify the app name is present, created in step 1 above: `$ heroku apps`
        3. Connect git to new app location on Heroku: `$ heroku git:remote -a ddeveloper72-riddle-me-this
 set git remote heroku to https://git.heroku.com/ddeveloper72-riddle-me-this.git`
        1. Create the requirements file, defining the modules imported to Heroku: `sudo pip3 freeze --local > requirements.txt`
        2. Create the proc file: `echo web: python run.py > Procfile`
        3. Add all project files: `$ git add .`
        4. Create a default message for the first commit to Heroku: `$ git commit -am "make it better- Use Heroku"`
        5. Push the project to Heroku: `$ git push heroku master`
        6. `$ heroku buildpacks:clear`
        7. Push the project to Heroku `$ git push heroku master` and watch the installation log for errors.
        8. Scale the app dynos for Heroku: `$ heroku ps:scale web=1`
        9. Set run.py debug to false before publishing: 
            ```python
            if __name__ == '__main__':
             """
             #assign a port ID works with cloud9
             """
             app.run(host=os.environ.get('IP'),
                 port=int(os.environ.get('PORT')),
                 debug=False) 
            ``` 
            Disable Flask developer-mode by setting debug=True to False. Save and execute  `git add run.py`
            

        13.  Execute `$ git commit -m "Turned off server developer mode"`
        14.  Execute `$ git push heroku master`
        14.  Save above changes to existing git profile `$ git push`
    1. In Heroku - Part 2:
        1. Select Settings
            - Select Config Vars:
            - set IP to 0.0.0.0
            - set PORT to 5000
        2. Select More, beside Open app:
            - Click Restart all dynos.
        3. Click Open app
            - Select new tab, [Riddle Me This](https://ddeveloper72-riddle-me-this.herokuapp.com/)
2. Credits:
    - There are loads, to be updated.
3. Bugs & Debugging:
    - Debugging Strategy:
      I thought that the best way to test this game was to run a beta test by putting the game on Heroku and then letting everyone in my college play it.  While doing so, I asked for feedback on the game. This is the feedback I got:
      1. The riddle answer checks were too literal. eg `A clock failed`, but `Clock` passed.
      2. The bottom of the masthead template gets cut-off, hiding my footer so it is no longer visible.
      3. The ordering of the scores from highest to lowest was in random order.
      4. Clicking the home button on the nav bar started the riddle game again, but didn't reset the score to 0.
      5. The image on the index page was too big when seen on a mobile device.
      6. If a player closes the browser without logging out of the game, they remain in session, when they open game again.
   
   - The fixes:
      1. I changed the checking system between player answer and riddle answer from the same as to is in. (from `==` to `ìs`).
      2. I still need to look at debugging the masthead template.
      3. I had been experimenting with the leaderboard code and had left the return result in brackets when I shouldn't have.
      4. In the @app.route('/') I added a line to the if statement which I use on the login decorator.  It creates a new player score, which is set at 0. So the player can play the game again without having to log out and log back in again.
      5. I added a media query in the style.css to change the max-width for the image to 30% on a max screen width of 415px.
      6. I haven't implemented a solution yet, to log a player out of the game, if they close the browser window. I am currently researching [Flask.session persisting after close browser](https://stackoverflow.com/questions/37227780/flask-session-persisting-after-close-browser). 
4. Boilerplate 
    - [Start Bootstrap - Coming Soon](https://startbootstrap.com/template-overviews/coming-soon/) Free Bootstrap Themes and Templates
5. Riddles
    - Victorian Era Riddles that have been sourced from the [Gutenberg Project](https://www.gutenberg.org/).
