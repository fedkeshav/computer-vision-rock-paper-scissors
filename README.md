# Computer Vision RPS
This project contains a way to play rock-paper-scissor with the computer using the computer's camera to indicate user's choice. Hence the name computer vision. It leverages image model from [teachable-machine]([url](https://teachablemachine.withgoogle.com/)), wherein the image model is trained using images for different actions. The image model (keras_model.h5) and associated text file (labels.txt) are stored in this repository. They cannot be executed directly but rely on running python code.
Rules of the game are simple: rock beats scissors, scissors beats paper, paper beats rock. User has four options: show image for rock, paper, scissor or do nothing.
