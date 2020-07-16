
## **Cows And Bulls**

There is still a lot more scope for improvement so feel free to contribute.

This is a fun python game developed with Pygame and Tkinter.

This game involves two players: Player A and Player B. Here Player A is expected to write any number of 4-digit numbers in a file "Wordlist.txt". This set of numbers written by Player A would be unknown to Player B. The aim of the game is to guess the number of Player A by the Player B with the help of some hints given. The Player B should guess the number of the Player A with 10 set of chances  after which the player would be given an extra chance which the player may or may not choose. The hints given to the Player B would be in terms of the number of cows and bulls he obtains when he tries to guess the Player 1's number.

Number of cows is the number of digits that are there in player A's number but in the wrong position.

Number of bulls is the number of digits that are in the correct place as that of the Player A's position.
<hr>
For Example:

The Number entered by Player A in the word file :  3758

The Number guessed by the Player B  :  2781

By comparing the two numbers we would observe that there is only one digit (The number 7) of Player B's guess that is in the same position as that of Player A. Hence the Number of Bull's would be equal to 1.

We also observe that the Player B's guessed number contains a digit that is in Player A's number but is not in the correct position (The number 8). So the number of Cows would be equal to 1.

The Player B by comparing his previous entries and the number of Cows and Bulls obtained should try to guess the number within 10 chances.
<hr>
The project uses Python for the development of this game. Some modules used for the development of this game includes Tkinter and PyGame.

**Tkinter** is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit

**Pygame** is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.

<p align="center">
    <img src = "images/Tkinter.png" width = 180>
    <br><br>
    <img src = "images/Pygame.png" width = 200>
</p>


## **Flowchart**:

<img src = "images/Flowchart.png">

## **Classes and Functions definitions used in the program:**

In `main.py` program:

· `class frame_title` :- This class is used for the creation of a frame for the Tkinter interface.

· `class login_frame` :- This class is used to create the Login Page for the user. It includes the following functions.

i) `def __init__`  :-The function that initialises all the variables used in the class.

ii)`def centerWindow` :- This function is to align the Tkinter interface window towards  the center of the screen.

iii) `def quit` :- The functions that quits the program.

iv) `def login` :- The function that does the work of allowing the user to login

v) `def signup` :- The function that does the work of sign up.
<br><br>

In `Pre-final.py` program:

· `def text` :- This function sets the Pygame display

· `def set_word` :- This function is used for Player A to enter the 4-Digit number into the text file

· `def alph` :-This function is used to display numbers on the Pygame display

· `def waitforkey` :- This function is used to wait for an input

· `def terminate` :- This function is used to kill the program

· `def displayTime` :- This function is used to display time

· `def dispGame` :- The function used to Display/Refresh the game screen

· `def updateguess` :- Function To Display/Refresh User Input

· `def startGame` :- This function is used for the main game loop

· `def callback` :- This function asks the user about the extra chance

· `def show` :- This function is executed when the Player B doesn't want to take an extra chance

· `def loop` :- This function check the number of turns and executes series of statements

· `def calc` :- This function updates tscore when turn is 10

· `def endGame` :-  Function To Display The End Game Screen


## **Screenshot of the output:**

<center>
<img src = "images/Picture1.png">

*The Text file Wordlist.txt where the Player A stores the set of 4-Digit Numbers*

<img src = "images/Picture2.png">

*The Login Screen*

<img src = "images/Picture3.png">

*The Starting Game Screen*

<img src = "images/Picture4.png">

*The Game while being played*

<img src = "images/Picture5.png">

*The dialog box opens asking for and extra chance when the Player B has still not guessed the Player A's number*

<img src = "images/Picture6.png">

*When the Player B takes the extra chance and guesses a completely wrong number*

<img src = "images/Picture7.png">

*When the Player B takes the extra chance and guesses a Partially correct answer with 1 cow and 1 bull in the extra chance*

<img src = "images/Picture8.png">

*When the player B doesn't take up the extra chance*
</center>

## **References taken for the project:**

· www.google.com

· https://www.pygame.org/docs/

· https://docs.python.org/2/library/tkinter.html

· www.youtube.com
