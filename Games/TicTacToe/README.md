# Project title
Tic-Tac-Toe.

# Video Link:
https://youtu.be/Z13cuzeDM60


# Introduction
This project is a simple implementation of the classic Tic Tac Toe game using HTML, CSS, and JavaScript. The game allows two players to take turns and place their symbols (X and O) on a 3x3 grid until one of them wins or the game ends in a draw.

# Project Structure
The project consists of three main files:

1. index.html: This file represents the structure and layout of the Tic Tac Toe game interface.

2. style.css: This file contains the CSS styles responsible for the visual presentation and responsiveness of the game interface.

3. script.js: This file contains the JavaScript code that implements the game's logic, including handling player turns, checking for a win or draw, and resetting the game.

# HTML Structure
The index.html file provides the following structure for the game:

* The game interface starts with a navigation bar displaying the game title "TIC-TAC-TOE."

* The main game area consists of a 3x3 grid represented by div elements with the class "box". Each box contains an empty span element (boxtext) initially, where the X and O symbols will be placed during the game.

* The game information area shows a message indicating whose turn it is and a "Restart" button to restart the game.

# CSS Styling
The style.css file applies the following styles to the game:

* Custom fonts from Google Fonts are imported for the navigation bar and game information.

* The navigation bar has a semi-transparent background color, and the text color is set to white.

* The game area is centered on the page using flexbox.

* Each box in the grid has a border and a font size relative to the viewport width, making the game responsive.

* When hovering over a box, its background color changes to a light shade.

* Media queries are used to adjust the grid size and font size for better display on smaller screens.

# JavaScript Logic
The script.js file contains the JavaScript logic responsible for handling the game's functionality:

* It initializes sound effect for each player's turn, and a sound effect for game over.

* The variable turn keeps track of the current player (X or O).

* The function changeTurn() switches the player's turn from X to O and vice versa.

* The function checkWin() checks for a winning condition after each player's move. It looks for three identical symbols in a row, column, or diagonal, and if found, it displays a winning message and highlights the winning combination.

* The function checkDraw() checks if the game is a draw (no more empty boxes) and displays a draw message.

* The main logic sets up event listeners for each box in the grid. When a box is clicked, it checks if it's empty, places the player's symbol, and updates the turn. It then calls checkWin() and checkDraw() to determine if the game should end.

* The "Restart" button is connected to an event listener that clears the grid, resets the turn to X, and removes any game over highlights.

# Game Interaction
To play the game:

1. Open index.html in a web browser.

2. Players take turns by clicking on an empty box in the grid to place their symbol (X or O).

3. The game will indicate whose turn it is and will show a message if someone wins or if the game ends in a draw.

4. Players can click the "Restart" button to start a new game.

# Acknowledgements

In the end & I would like to give my immense gratitude to the Professor David J. Malan, for teaching this fabulous course with great enthusiasm & passion.