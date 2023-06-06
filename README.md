# Computer Vision: Rock paper scissors game
This project contains a way to play rock-paper-scissor with the computer using the computer's camera to indicate user's choice. Hence the name computer vision. It leverages image model from [teachable-machine]([url](https://teachablemachine.withgoogle.com/)), wherein the image model is trained using images for different actions. The image model (keras_model.h5) and associated text file (labels.txt) are stored in this repository. They cannot be executed directly but rely on running python code.

## Rules of the game
User needs to choose one of the four actions by showing a hand sign: rock, paper, scissors or nothing
Computer randomly chooses from one of the three actions: rock, paper, scissor
Rules of the game are simple: rock beats scissors, scissors beats paper, paper beats rock. User has four options: show image for rock, paper, scissor or do nothing.

## How to play the game
Create an instance of the `Rps_Game` class. Call on the `play` method of the object to play the game.

## Defining a class to play the game
We have created a class called `Rps_Game`, with three attributes and nine (object) methods.

### Attributes of the class
The `Rps_Game` class has three attributes:
- `computer_score`: Number of rounds won by the computer
- `user_score`: Number of rounds won by the user
- `game_count`: Number of games/rounds played in total

### Methods of the class
The `Rps_Game` class has nine methods.
- `get_computer_choice`: Uses Random module to get computer's action randomly from a list of three actions (Rock, Paper, Scissors)
- `screen_text_inputs`: Provides the main inputs everytime we want to print text to screen. It is called on by other functions
- `get_user_prediction`: Predicts user's choice based on the action they present to the camera.
- `get_winner`: Compares actions of computer and user, and declares who won a round. Prints the result of each round, along with updating scores and game count
- `declare_winner`: Declares who the winner is based on who wins 3 games first. Shuts down the camera and all windows as as soon as a winner is declared
- `score_printer`: Prints the computer's and user's score to screen before start of every round
- `game_number_printer`: Prints the game number to screen before  start of every round
- `cap_release`: Releases the camera and destroys all windows
- `play`: Plays the entire game by calling on all other class methods

## Ideas to improve the game further
- Keep scores on top left, and game/round number on top right always
- Nothing should be printed in command line. Print everything to screen including user choice, computer choice and result of the game
