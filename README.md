<h1>Milestone 3 Project</h1>

<h2>Riddle-Me-This</h2>

<h3>Project Goals:</h3>
This project is all about having fun, while making a game which demonstrates Python as the backbone programming language.

The Game is designed to run on Heroku and will facilitate multiple players.  The players will be able to register their own unique usernames.  

A leader-board will show the scores of players from highest to lowest.

<h3>Game construction:</h3>

<h4>Work in Progress</h4>
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

