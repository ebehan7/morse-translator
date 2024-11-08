# Morse Translator

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)


## General Information
- The goal of this prototype is to create a translator that converts typed letters into audible Morse code.
- I undertook this project simply because I found it to be an interesting idea which I had not yet seen achieved.


## Technologies Used
- Python (Latest stable version)
- Playsound 1.3.0 (library)
- mutagen 1.47.0 (library)
- wheel and setuptools (library)


## Setup
1) Need python installed on the device this can be done with either homebrew (for MacOS / Linux) by going to this link https://brew.sh/ and after running the install command there in the terminal running 'brew install python3' or the windows store (for windows) and looking for python 3.13. You can test the installation of python by running python3 in your devices terminal
if it changes your terminal mode to the interpreter (3 coloured arrows), you know that it is working and can exit the interpreter with the command exit().

1.1) Potentially there can be an issue with a homebrew python installation you can run brew link --overwrite python3@13 to override any conflicting files.

2) After this we need to setup a virtual environment for the project to install dependencies we can do this by going:
- into our file system and opening the folder where the project is installed, we can then use get info for macOS or properties for Windows and look for the location of the file (this is where for MacOS or the file path on top in the windows finder). 

2.1) Going back to the terminal we can then post the command cd {the file path just copied} to open the project in our terminal
2.2) Here we will run python3 venv ./ (this means create a virtual environment in the current folder), creating many more folders.
2.3) We will need to cd into 'bin' and run source ./activate to allow the environment to accept changes
2.4) Now we can go back to the main work space with cd .. and run pip3 install setup-tools and pip3 install wheel so that we can install our dependencies
2.5) Run pip3 install -r requirements.txt
2.6) Can run the project with python3 audio.py


## Usage
- After following setup instructions, conduct the following for Mac:
1. Open Terminal
2. Input 'cd ./Desktop/MP3_Keyboard'
3. Input 'source ./bin/activate'
4. Input 'python3 audio.py'
5. See display: "Press a key (a-z) to play a sound. Type 'esc' to exit.
Press a key (a-z): "
6. Type any letter you would like to hear and press 'Enter/Return' to run.
7. When finished press 'Esc' and 'Enter/Return'.



## Project Status
This project is completed as it has accomplished its original goal of translating typed letters into audible Morse code.


## Room for Improvement

Room for improvement:
1. Can make the time out of the application line up better with the ending of the mp3 clip.
2.Could also include handling for numbers as well as other characters
3. Easier setup for an end user

To do:
1. Use the inbuilt keyboard so that we can use inputs off normal key presses, the issue here is that it needs a higher level of access which makes it more difficult to run the program as a whole. 
2. Can think more about a UI / usability outside of a terminal.


## Acknowledgements
- Information sources that assisted in the writing of this code:
- TunePad Documentation. (2024). Learn TunePad. https://learn.tunepad.com/docs/


‌- This project was inspired by:
- My own love for music
- My enthusiastic tutor, Andrew
- My experience of learning to use Tunepad during tutorials
- My friend, Paul, who taught me much of the code used in this project. I learnt a lot from him.
