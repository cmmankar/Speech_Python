# pip install SpeechRecognition
# pip install pyttsx3

import speech_recognition as sr
import pyttsx3

# initialize the recognizer
r = sr.Recognizer()

# Function to convert to text to 
# speech
def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

SpeakText("Hello world")

