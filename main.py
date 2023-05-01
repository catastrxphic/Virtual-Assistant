import speech_recognition as sr
import pyttsx3, nltk
import pywhatkit
import wikipedia
from nltk.chat.util import Chat, reflections

#initializing speech recognition engine:
recog_engine = sr.Recognizer()

#initializing text-to-speech engine
tts_engine = pyttsx3.init('sapi5')
voice = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voice[1].id)

#setting voice rate from text-to-speech (tts_engine), by default it is 200
voice_rate = tts_engine.getProperty('rate')
tts_engine.setProperty('rate', 130)


#funtion to hear user's voice input and return text
def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recog_engine.listen(source)

        try:
            instruction = recog_engine.recognize_google(audio)
            print("you said: ", instruction)
            return instruction
        except:
            print("Sorry, I didn't understand  !")
            return ""
        
#funtion for the chatbot to speak the answer to the user
def talk_back(message):
    tts_engine.say(message)
    tts_engine.runAndWait()

#Beggining of conversation between VA and user:
talk_back("Hello, this is your virtual assistant, how can I help you today?")

#continue conversation
while True:
    #get the anser fo the user and process it
    instructions = get_audio().lower()

    #open a video in youtube
    if "play" in instructions:
        song = instructions.replace('play', "")
        talk_back("playing " + song)
        pywhatkit.playonyt(song)

    elif "hey there" in instructions:
        talk_back("Hello, how can I help you?")
    
    elif "your name" in instructions and 'what' in instructions:
        print("Virtual assistant: " , "I am nyx, your virtual assistant, Nice to meet you!")
        talk_back("I am nyx, your virtual assistant, Nice to meet you!")

    elif "tell me about" in instructions:
        figure = instructions.replace('search for', "")
        biography = wikipedia.summary(figure, 1)
        print("virtual assint: ", biography)
        talk_back(biography)