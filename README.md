

<h1>Milestone 3 Project</h1>


<h2>Riddle-Me-This</h2>
<h3>by Duncan Falconer for the Code Institute, 2018

<h2>Project Goals:</h2>
This project is all about having fun, while making a game which demonstrates Python as the backbone programming language.

The Game is designed to run on Heroku and will facilitate multiple players, playing the same game at the same time.  The players will be able to register their own unique usernames when they log into the game.  Their usernames will be used to tack their progress throughout the game.

A leader-board will show the scores of players from highest to lowest.

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
            <ol>
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
<h2>Wireframes:</h2>

<h2>Game construction:</h2>
<h3>Work in Progress</h3>
This game is still in development mode.
<ol>
<li>The wire frames are under construction.</li>
<li>The development tests are being written</li>
<li>The game code is being developed</li>
<li>The leader board has to be planned along with the game code</li>
</ol>

The game core is written in Python, using Flask to inject player and game information into an off the shelf bootstrap template.

The user names and passwords are stored in a SQL database and processed by SQLAlchemy.  Again, SQLAlchemy is an off the shelf product and is imported into Flask.

The passwords for users logging into the game are protected by encryption.  The passwords are hashed before being written to the database.

The riddles in this game are stored in a JSON file. The format of the game will be that the player is presented with a riddle when the enter the game after login in.

The riddle will the rendered from the JSON using basic escaping characters within the riddle string.
The answer is also contained within the JSON along with an image of the answer which will render when the riddle is answered correctly. Again, inline styles will be used to manage the image size being injected by Flask to the html elements on the game page.

The method of keeping track of the players score is still in development, but will be rendered and incremented as the player progresses through the game.

The leader board will then  display the top 5 player names and scores.  Again this is still under development.

