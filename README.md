

# Milestone 3 Project


## [Riddle Me This](https://ddeveloper72-riddle-me-this.herokuapp.com/)
### by Duncan Falconer for the Code Institute, 2018

1. The project brief can be found by clicking [here](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/readme/brief.md)
2. The project guidelines can be found by clicking [here](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/readme/guidlines.md)

## 1. Project Goals:
This project is all about having fun, while making a game which demonstrates Python as the backbone programming language.

The Game is designed to run on Heroku and will facilitate multiple players, playing the same game at the same time.  The players will be able to register their own unique usernames when they log into the game.  Their usernames will be used to tack their progress throughout the game.

A leader-board will show the scores of players from highest to lowest.
## 2 .The UX Design:
#### 1 Strategy

| Focus                                                       | User Needs                                                            | Business Objectives                             |
|-------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| What are you aiming to achieve?                             | To be able to play a simple game of riddles. | To demonstrate my coding ability with the use of simple user authentication. |
|                                                             | To see the score for each played riddle. | Deploy sessions as well as basic security principles to insure the player can enjoy the game without the site breaking if tampered with. |
| For whom?                                                   | To see the total score amongst other players on the leader-board.|  |
| TARGET AUDIENCE                                             |  |  |




#### 2 Scope

| Focus                                                       | Functional Specification                                              | Content Requirements                            |
|-------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------|
| |  My project is to create a game for lovers of old style  Victorian Era Riddles that have been sourced from the [**Gutenberg Project**](https://www.gutenberg.org/) | |
| Which features?                                             | User name and authentication. | SQL database for username and encrypted password storage.  Flash messaging for user feedback with conditional style formatting. |
| What’s on the table?                                        | View a riddle to be played. | A list of riddles, answers and imagery. |
|                                                             | Submit an answer to a riddle and have it checked. | A form field for submitting an answer. |
|                                                             | If the the answer is correct, to move on to the next riddle. | Flash messaging to inform the player of their progress. |
|                                                             | If an answer is incorrect, to be provided with the correct answer.| Answer/Data validation check which shows the correct answer in a flash message. |
|                                                             | To increment the player score for each correct answer given. | An internal score card, for logging the players score. |
|                                                             | On completion of the riddles, to present a leader board of the top 5 scores. | A leader board which reads from all the players score cards. |
|                                                             | Version control managed with Git & GitHub |  |



#### 3 Structure

| Focus                                                       | Interaction Design                                                           | Information Architecture                                                               |
|-------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| How is the information structured?                          | Where am I? / How did I get here? / What can I do here? / Where can I go?    | Organizational / Navigational schemas (tree / nested list / hub and spoke / dashboard) |
|                                                             | User sign-up or login | Tree Structure |
| How is it logically grouped?                                | Unsuccessful login prompts user to register first. | Start/home page|
|                               							  | TThe user is asked a riddle.  If answered correctly, the next riddle is given. | Answer riddle, progress through all riddles, ending at leader board. |
|                                                             | If the wrong answer is given, the correct answer is shown.  The user is then given a new riddle to answer. |  |
|                                                             | Following the last riddle, the leader board ins shown. The player ban play again from the home button. |  |


#### 4 Skeleton

| Focus                                                       | Interface Design                                       | Navigational Design  | Information Design  |
|-------------------------------------------------------------|--------------------------------------------------------|----------------------|---------------------|
| How will the information be represented?                    | See wireframes                                         |    Flash messaging with conditional formatting                  |                     |
| How will the user navigate to the information and features? | Home button and navbar links. |  | Title and informational typescripts |



#### 5 Surface

| Focus                                                       | Visual Design                       |
|-------------------------------------------------------------|-------------------------------------|
| What will the finished product look like?                   | The Bootstrap 4 template used in this project  was from [Start Bootstrap - Coming Soon](https://startbootstrap.com/template-overviews/coming-soon/). |
| | A    video background of an old style ticking  timepiece, marks the passage of time while the   player deliberates over the     answer to  a   riddle. |
|                                                             | I tried to use typography that works on both mobile and large screens. |
| What colours, typography and design elements will be used?  | I worked with feedback from test users |


### 6. Wireframes:

![Index](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Index.png "Fig 1 showing Index page")

![Register!](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Register!.png "Fig 2 showing Register page")

![Login here!](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Login_here!.png "Fig 3 showing Log-in page")

![Game](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Game.png "Fig 4 showing Game page")

![Leader-board](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/readme/Leaderboard.png "Fig 5 showing Leader-board")



## 3. Game construction

1. Tools used
   * Written in VSCode
   * SQL database was created with SQLite3 (see database included with repository)
   * css files were compiled from scss using sass watch (_Please see programming comments within the [styles.css](https://github.com/ddeveloper72/milestone-3-project/blob/master/static/css/styles.css)_) 
   * Tested Chrome dev tools & VSCode debugger
   * HTML and CSS checked with help from the Mark-up Validation Service
   * Version management and test branches created in git
   * Web deployment hosted on Heroku

2. Reference Literature
   * [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
   * [Flask-Session](Flask-Session)
   * [Message Flashing](http://flask.pocoo.org/docs/1.0/patterns/flashing/)


3. Code Development
   The project brief was to follow a a pattern of **Test Driven Development**.  A series of tests were written at the start of this project and then the run time function was written, based on the test. I used user feedback to assist with identifying and debugging the code.

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
    
### In Heroku - Part 1

1. Log into Heroku
2. Select New and Create new App.
3. Create a App name, select the region.
    - then Create app.

4. Select Resources.
    - then select Find more add-ons.
    - Select Heroku Postgres.
    - Install Heroku Postgres, using the hobby plan.
    
5. Return to Personal menu then select ddeveloper72-riddle-me-this.
6. select Deploy 
    - Note the deployment instructions.
  
### From Cloud 9

1. Log in to Heroku:         
   - `$ heroku login`
1. Verify the app name is present, created in step 1 above: 
    - `$ heroku apps`
2. Connect git to new app location on Heroku: 
    - `$ heroku git:remote -addeveloper72-riddle-me-this set git remote herokutohttps://git.heroku.com/ddeveloper72-riddle-me-this.git`
3. Create the requirements file, defining the modules imported to Heroku:
    - `sudo pip3freeze --local > requirements.txt`
4. Create the proc file: 
    - `echo web: python run.py > Procfile`
5. Add all project files: 
    - `$ git add .`
6. Create a default message for the first commit to Heroku:
   - `$ git commit -am "makeit better- Use Heroku"`
7. Push the project to Heroku: 
   - `$ git push heroku master`
   - `$ heroku buildpacks:clear`
8.  Push the project to Heroku 
    - `$ git push heroku master` (watch the installation log for errors).
9.  Scale the app dynos for Heroku:
    - `$ heroku ps:scale web=1`
10. Set run.py debug to false before publishing
            
    ```python
    if __name__ == '__main__':
     """
     #assign a port ID works with cloud9
     """
     app.run(host=os.environ.get('IP'),
         port=int(os.environ.get('PORT')),
         debug=False) 
    ``` 

11. Disable Flask developer-mode by setting debug=True to False. Save and execut11. 
    - `git add run.py`
12.   Execute 
      -   `$ git commit -m "Turned off server developer mode"`
14.   Execute 
      -   `$ git push heroku master`
16.    Save above changes to existing git profile 
       -    `$ git push`
   
### In Heroku - Part 2
        
1. Select Settings
    - Select `Config Vars`
    - set `IP` to `0.0.0.0`
    - set `PORT` to `5000`
    - set `SECRET_KEY` to `Some_Secret`
2. Select More, beside Open app:
    - Click `Restart all dynos`.
3. Click Open app
    - Select new tab, [Riddle Me This](https://ddeveloper72-riddle-me-this.herokuapp.com/)
  

## 5. Development & Testing

   * During development, media responsiveness of the game was tested using Chrome dev tools to simulate different small and large screen devices.  
   * I later shared my game with family and friends on WhatsApp so that they could follow the Heroku link to the game app and see the game on their mobile handsets.  In this way  I found that I had to limit the sizes of my riddle images as well as title page images.  
   * I found response issues when viewing the game when switching between portrait and landscape modes in my development environment.  I was able to correct these by adding in media queries to my sass file.
   * When testing the game in multiplayer mode-  I created several player logins by running different browsers simultaneously.  The browsers and hardware that I used were:
      
        1.  Chrome
        2.  Firefox
        3.  Opra Browser
        4.  Internet Explorer
        5.  Edge
        6.  Samsung Galaxy S5
        7.  Samsung Galaxy S8+
      
## - Debugging Strategy
  
  I thought that the best way to test this game was to run a beta test by putting the game on Heroku and then letting everyone in my college play it.  While doing so, I asked for feedback on the game. This is the feedback I got:

  ### _The issues found_

  1. The riddle answer checks were too literal. eg `A clock` failed, but `Clock` passed.
  2. The bottom of the masthead template gets cut-off, hiding my footer so it is no longer visible.
  3. The web page itself doesn't permit a user to scroll down on smaller screens.
  4. The ordering of the scores from highest to lowest was in random order.
  5. Clicking the home button on the nav bar started the riddle game again, but didn't reset the score to 0.
  6. The image on the index page was too big when seen on a mobile device.
  7. The log in, log out and sign up nav links were disabled on certain pages by design, but still visible.
  8. I had written in an overflow-x scroll-bar feature for riddles, which were sometimes too long to view on the screen.  User feedback was to remove this as it was too awkward to use on computers with smaller screens.
  9. If a player closes the browser without logging out of the game, they remain in session, when they open game again.
   _
### _The fixes implemented_

   1. I changed the checking system between player answer and riddle answer from the same as to is in. (from `==` to `ìs`).
   2. I changed the masthead height to 100% and added overflow-y scroll. This was a very difficult fix to resolve, because it wasn't know what was causing the problem preventing vertical page scrolling.
   3. I had been experimenting with the leader board code and had left the return resulting brackets when I shouldn't have.
   4. In the @app.route('/') I added a line to the if statement which I use on the login decorator.  It creates a new player score, which is set at 0. So the player can play the game again without having to log out and log back in again.
   5. I added a media queries for the main image as well as the leader board images for smaller screen sizes.
   6. I implemented an if else flask function which uses session, to manage the navbar login, logout and sign-up nav links for the secure and insecure areas of the site.
   7. I added a height auto to the riddles dialog box, so as to remove the need for the vertical scroll bars.
   8. I haven't implemented a solution yet, to log a player out of the game, if they close the browser window. I am currently researching [Flask.session persisting after close browser(https://stackoverflow.com/questions/37227780/flask-session-persisting-after-close-brower).
   

## 6. Credits

- I used Victorian Era Riddles that have been sourced with thanks from the [Gutenberg Project](https://www.gutenberg.org/).

- There are loads of people that I want to give credit to.  These include, first and foremost my family for their support!

- My friends within the Code Institute who go by the Slack handles @JoWings, @Eventret, @Miro, @saraloh, @JohnL3, @Sonya my Mentor, Nishant and tutors @niel_ci and @nakita_ci and many others.  You guys have helped me to find my way, introduced me to using various online resources like [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ) and personally shared resources like UXD design templates-to help keep my thoughts on task and on track and help with my C9 coding environment.  Thank you ladies and gentlemen!

- To create a login function for my game site, I adapted the tutorial from Pretty Printed to create an SQL dataset for storing my player names and passwords in an secure environment.  The tutorial which I followed was called: [Build a User Login System With Flask-Login, Flask-WTForms, Flask-Bootstrap, and Flask-SQLAlchemy](https://youtu.be/8aTnmsDMldY).
    
<h6><span class="text-muted">Milestone 3 project for the Code Institute <br />by Duncan Falconer, 2018</span></h6>
