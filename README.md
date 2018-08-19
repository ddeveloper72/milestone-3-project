

<h1>Milestone 3 Project</h1>


<h2>Riddle-Me-This</h2>
<h3>by Duncan Falconer for the Code Institute, 2018

<ol>
<li>
    <h2>Project Goals:</h2>
    This project is all about having fun, while making a game which demonstrates Python as the backbone programming language.

    The Game is designed to run on Heroku and will facilitate multiple players, playing the same game at the same time.  The players will be able to register their own unique usernames when they log into the game.  Their usernames will be used to tack their progress throughout the game.

    A leader-board will show the scores of players from highest to lowest.
</li>
<li>
    <h2>The UX Design:</h2>
    <ol>
    <li><h4>Strategy:</h4>
        <h4>Focus:</h4>
            <ul style="list-style-type:disc">
                <li>My project is to create a game for lovers of old style  Victorian Era Riddles that have been sourced from the <a href="www.gutenberg.net"><strong>Gutenberg Project</strong></a>
                </li>
            </ul>
        <h4>User Needs:</h4>
            <ul style="list-style-type:disc">
                <li>To provide a game that a player can log into, so that   they  will then be able to play by answering a number of  riddles. If a     riddle is answered wrong, the game will    respond with the    player's incorrect answer as well as   provide the correct answer    along with a hint for   answering the next questions.
                </li>
                <li>The player's score will be added each time they answer a riddle correctly.  When the game is finished, the player can see their final score along with the scores of other players.
                </li>
            </ul>
        <h4>Business Objectives:</h4>
            <ul style="list-style-type:disc">
                <li>To demonstrate my use of the Python programming language in a game for my graded projects portfolio.
                </li>
            </ul>
    </li>
    <li><h4>Scope:</h4>
        <h4>Focus:</h4>
            <ul style="list-style-type:disc">
                <li>Features of this design. The requirements of this project from the brief.
                </li>
            </ul>
        <h4>Functional Specification:</h4>
            <ol>
                <li>The player must be able to use a    unique     player   name to play the     game.
                </li>
                <li>The player must also be able to     respond     to a    riddle by being able to    type in an     answer.
                </li>
                <li>There has to be process which checks    the    player's     answer and provides    feedback to them  about their    answer.
                </li>
                <li>The play must be able to see their      score.
                </li>
                <li>The player needs to be asked another      riddle.
                </li>
                <li>The player needs to be able to see  the  scores of other    players along with  their own.
                <li>The player needs to be able to play     the     game    again.
                </li>
            </ol>   
        <h4>Content Requirements:</h4>
            <ol>
                <li>The game needs a way for users to   create    a unique  user name; a login     facility.
                </li>
                <li>This is a riddle game, so it has to     have    a source    of riddles to ask.
                </li>
                <li>The player must be able to submit    their  answer, so a    answer field and  submit button     is needed.
                </li>
                <li>A logic engine is needed to check the     player's  answer to the correct answer   for a   riddle, with feedback     provided to     the player,     of a wrong or right         answer.
                </li>
                <li>The game has to increment the score     for     right   answers.
                </li>
                <li>The game has to show a score board  with     the results    from other  players.
                </li>
            </ol>
    </li>     
    <li><h4>Structure:</h4>
        <h4>Focus:</h4>
            <ul style="list-style-type:disc">
                <li>What are the steps, the progression/flow of information throughout the game process?
                </li>
            </ul>
        <h4>Interaction Design:</h4>
            <ol> 
                <li>The player login function -> is a data filter.  It is a process which manages and insures the  player uses a unique player name, or else the game wouldn't work properly.
                </li>
                <li>The unique player is given a riddle to  answer.
                </li>
                <li>If the answer is correct, the score is  added and they are given the next riddle.
                </li>
                <li>If the answer is wrong, they are    presented the wrong answer as well as  provided a hint. They are asked to try again.
                </li>
                <li>When the last riddle is answered    correctly, the player is shown a leader board  of all the players.
                </li>
                <li>If the player wishes to quit the game at    any time, they can log out, or play again by   logging back in.
                </li>
            </ol>
        <h4>Information Architecture:</h4>
            <ul style="list-style-type:disc">
                <li>The processes of this game follows a    tree/branch structure from start to    finish.
                </li>
                <li><strong>Start:</strong> Riddle, Answer =    Right, Next Riddle + Score, Answer = Right,    Next Riddle + Score  +1, End
                </li>
                <li><strong>Start:</strong> Riddle, Answer =   Wrong, Next Riddle, Answer = Right, Next  Riddle + Score +1, End
                </li>
            </ul>
    </li>    
    <li><h4>Skeleton:</h4>
        <h4>Focus:</h4>
            <ol list-style-type:decimal>
                <li> How will the information be represented?
                </li>
                <li>How will the user navigate to the   information and features?
                </li>
            </ol>
        <h4>Interface Design:</h4>
            <ul style="list-style-type:disc">
                <li>The best way to show the design, was as in the Wireframes.  See below.
                </li>
            </ul>
    <h4>Navigational Design:</h4>
            <ul style="list-style-type:disc">
                <li>The user follows prompts from the index page to either register or login to play the game.  Once in the game, the page will refresh each time an answer is input, which again prompts the player toward completion of the game.  This then ends with the player being brought to the leader-board.
                </li>
            </ul>
    <h4>Information Design:</h4>
            <ul style="list-style-type:disc">
                <li>The player is prompted by both text and imagery throughout their visit to the game.
                </li>
            </ul>
    </li>  
    <li><h4>Surface:</h4>
        <h4>Focus:</h4>
            <ul style="list-style-type:disc">
                <li>The focus is on the triangular layout of the    page, when viewed  on a large screen device.
                </li>
                <li>To play the riddle game, a player will need     to register their name and then log into the game.   Information is laid out    clearly with little to no     other page distraction.  
                </li>
            </ul>
        <h4>Visual Design:</h4>
            <ul style="list-style-type:disc">
                <li>The Bootstrap 4 template used in this project   was from <a href="https://startbootstrap.com/    template-overviews/coming-soon/"><strong>Start Bootstrap - Coming Soon</strong></a>   
                </li>   
                <li>A    video background of an old style ticking  timepiece, marks the passage of time while the   player deliberates over the     answer to  a   riddle.  
                </li> 
            </ul>        
    </li>
</ol>
</li>
<li>
<h2>Wireframes:</h2>

![Index](https://raw.githubusercontent.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Index.png)

![Register!](https://raw.githubusercontent.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Register!.png)

![Login here!](https://raw.githubusercontent.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Login_here!.png)

![Game](https://raw.githubusercontent.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Game.png)

![Leader-board](https://raw.githubusercontent.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Leaderboard.png)




</li>
<li>
<h2>Game construction:</h2>
    <h3>Work in Progress</h3>
<p>The project brief was to follow a a pattern of <strong>Test Driven Development</strong>.  A series of tests were written at the start of this project and then the run time function was written, based on the test.</P>

<p>Not all functions were written in this way and these will be followed up with tests.</p>

<h3>Test 1</h3>

```python
def test_loadUsers(self):
        """
        test to check that the plyers can be loaded from the
        users file which stores player names and wrong answers.
        """
        users = run.loadUsers()
        self.assertEqual(len(users), 3)
```

<h3>Test 1: Run-time function</h3>

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

<h3>Test 2</h3>

```python
def test_storePlayerName(self):
        users = run.storePlayerName()
        self.assertGreater(len(users), 0)  
```

<h3>Test 2: Run-time function</h3>

```python
def storePlayerName(username, answer_given):
    """ 
    Stores player names and wrong answer to a txt file.  Adapted from chat app tutorial 
    that maintained the chat history: 
    """
    write_to_file('data/users.txt', f'{datetime.now().strftime("%H:%M:%S")}, {username.title()}, {answer_given}\n')

```

<hr>

<h3>Test 3</h3>

```python
def test_loadRiddles(self):
    """
    test to check that the users can be loaded from the
    json file
    """
    riddles = run.loadRiddles()
    self.assertEqual(len(riddles), 14)
```


<h3>Test 3: Run-time function</h3>

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

<h3>Test 4</h3>

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

<h3>Test 4: Run-time function</h3>

```python
def validateAnswer(riddle, answer):
    """
    check the player's answer against our own
    """
    answer_given = request.form["answer"].lower()
    return answer_given
```

<hr>

<h3>Test 5</h3>

```python
def test_count_eq(self):
    """Will succeed"""
    self.assertCountEqual(self.result, self.expected)
```

<h3>Test 5: Run-time function</h3>

```python
def countRiddles():
    """
    Count the number or riddle in out list so we can keep score! This makes our count dynamic.
    """
    numRiddles = len(loadRiddles())
    return numRiddles
```

<hr>

<h4>Selection of Specialist Functions</h4>
<h3>Run-time function #8</h3>

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

<h3>Run-time function #9</h3>

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

</li>
<li>
<h2>Deployment Instructions:</h2>
</li>
<p>Instructions for deployment to a hosing site: Heroku</p>
</ol>
