import time
from playsound import playsound #enables sound files to play
from mutagen.mp3 import MP3 #imports data of mp3 files
import os #locates files

audio_dir = "./audio_files" #sets audio file directory; searches for mp3's with a key

def play_sound(key): 
    file = os.path.join(audio_dir,f"{key}.mp3") #sets file by using key from main function & extracting data
    audio_data = MP3(file)
    if key.isalpha() == True:
        try:
            print(f"playing {file}")
            playsound(file)
            time.sleep(audio_data.info.length) #use play sound library to use file for duration of run time
        except Exception as e:
            print(f"Error playing sound for {key}: {e}")
    else:
        print("Error handling input ensure you are entering alphabetical characters") #raising any errors if key pressed is not alphabetical

def main(): 
    print("Press a key (a-z) to play a sound. Type 'esc' to exit.")
    
    while True:
        key = input("Press a key (a-z): ").lower() #handling inputs by converting them to lowercase

        if key == 'esc': #check for escape statement
            print("Exiting...")
            break #exit program
        elif len(key) == 1:
            play_sound(key) #forward to play_sound()
        else:
            print("Invalid input. Please press a key from 'a' to 'z'.") #display error message

if __name__ == "__main__":
    main() #run the function
