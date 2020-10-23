# Smart-Adaptive-Brightness [v1]

This is a python3 based application that uses camera and screen content to calculate the brightness level required, and then applies it.
This application works on Windows and Linux based OS.

# Working

This application does the following things to get the value of brightness required at any given point of time:
- Capture an image using camera, convert it into greyscale and then evaluate the average ambient brightness of the image.
- Take a screenshot, and repeat the above process.

Use the above two calculated value to decide the correct amount of brightness for the screen.
- Greater the amount of ambient light, more brightness required.
- Darker the screen content is , more the brightness is required.

# How to Run?
- Clone the Repository
- Install requirements.txt by typing "pip install -r requirements.txt" into Command Prompt in working Directory.
- Run the file main.py.
