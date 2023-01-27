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

# SpeakText("Hello world")

# use the microphone as source for input
with sr.Microphone() as source2:
        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
    print("Silence please, caliberating background noise")
    r.adjust_for_ambient_noise(source2, duration=2)
    print("Caliberated, now speak .....")

    # listen for the user's input
    audio2 = r.listen(source2)

    # Using google to recognize audio
    MyText = r.recognize_google(audio2)
    MyText = MyText.lower()

    print("Did you say"+MyText)
    SpeakText(MyText)

    






