# Importing relevant modules 
import time
import cv2
from keras.models import load_model
import numpy as np
import random


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the computer vision model
model = load_model('keras_model.h5', compile = False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Opening the camera and storing info on each frame as a numpy array
cap = cv2.VideoCapture(0)


# Defining a class, with its attributes and methods
class Rps_Game():
    '''
    This is a class containing three attributes and nine (object) methods that helps to play the rock-paper-scissor game.

    The five attributes are
    1. computer_score = Number of rounds won by the computer
    2. user_score = Number of rounds won by the user
    3. game_count = Number of games/rounds played in total

    The nine methods are defined below
    '''
    
    def __init__(self):
        self.computer_score = 0
        self.user_score = 0
        self.game_count = 0

    def  get_computer_choice(self):
        '''
        Generates computer's action randomly between rock, paper and scissors

        Returns:
            Computer's choice
        '''
        comp_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        return comp_choice        

    def screen_text_inputs(self):
        '''
        Provides the main inputs everytime we want to print text to screen.
        It is called on by other functions

        Returns:
            List of inputs needed for printing text to screen
        '''
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50,75)
        fontScale = 3
        color = (255, 255, 255)
        thickness = 10
        text_list = [org, font, fontScale, color, thickness]
        return text_list
   
    def get_user_prediction(self):
        '''
        Predicts user's choice based on the action they present to the camera.

        Returns:
            User's choice
        '''
        start_time = time.time()
        while time.time() - start_time < 5: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            cv2.imshow('frame', resized_frame)
            # data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            image_np = np.asarray(resized_frame, dtype=np.float32).reshape(1, 224, 224, 3)
            normalized_image = (image_np / 127.5) - 1 # Normalize the image
            # data[0] = normalized_image

            # Displaying countdown timer on screen
            text_list = self.screen_text_inputs()
            text = f'{5 - round(time.time()-start_time)}'
            cv2.putText(frame, text, text_list[0], text_list[1], text_list[2], text_list[3], text_list[4], cv2.LINE_AA)
            cv2.imshow('frame', frame)
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        prediction = model.predict(normalized_image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]
        print(f' You chose {class_name} ')
        print(confidence_score)
        return class_name
        

    def get_winner(self, computer_choice, user_choice):
        '''
        Compares actions of computer and user, and declares who won a round
        Prints the result of each round, along with updating scores and game count
        
        Inputs:
            Computer's choice: Action chosen by computer
            User's choice: Action chosen by user
        
        '''
        if (computer_choice == 'Rock' and user_choice == 'Scissors') or \
           (computer_choice == 'Scissors' and user_choice == 'Paper') or \
           (computer_choice == 'Paper' and user_choice == 'Rock'):
            print('Computer wins')
            self.computer_score += 1
            self.game_count += 1
        elif computer_choice == user_choice or user_choice == 'Nothing':
            print('It is a tie')
            self.game_count += 1
        else:
            print('User wins')
            self.user_score += 1
            self.game_count += 1

    def declare_winner(self):
        '''
        Declares who the winner is based on who wins 3 games first
        Shuts down the camera and all windows as as soon as a winner is declared        
        '''

        if (self.computer_score == 3) :
            print(f'Computer wins. Computer {self.computer_score} > User {self.user_score}')
            self.cap_release()

        elif (self.user_score == 3) :
            print(f'User wins. User {self.user_score} > Computer {self.computer_score}')
            self.cap_release()

    def score_printer(self):
        '''
        Prints the computer's and user's score to screen before 
        start of every round        
        '''
        start = time.time()
        while (time.time() - start) < 2:
            text = (f' User {self.user_score} | Computer {self.computer_score}')
            text_list = self.screen_text_inputs()
            ret, frame = cap.read()
            cv2.putText(frame, text, text_list[0], text_list[1], text_list[2], text_list[3], text_list[4], cv2.LINE_AA)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def game_number_printer(self):
        '''
        Prints the game number to screen before 
        start of every round        
        '''
        start = time.time()
        while (time.time() - start) < 2:
            i = self.game_count + 1
            text = (f' GAME {i}')
            text_list = self.screen_text_inputs()
            ret, frame = cap.read()
            cv2.putText(frame, text, text_list[0], text_list[1], text_list[2], text_list[3], text_list[4], cv2.LINE_AA)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    def cap_release(self):
        '''
        Releases the camera and destroys all windows        
        '''
        # Release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    def play(self):
        '''
        Plays the entire game by calling on all other class methods       
        '''
        while max(self.user_score, self.computer_score) < 3:
            self.score_printer()
            self.game_number_printer()
            computer_choice = self.get_computer_choice()
            user_choice = self.get_user_prediction()
            self.get_winner(computer_choice,user_choice)
            self.declare_winner()

# Create an instance of the Rps_Game class
game = Rps_Game()
# Play the game by calling on the play method
game.play()
