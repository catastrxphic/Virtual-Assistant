import speech_recognition as sr
import pyttsx3, nltk
import pywhatkit
import wikipedia
import requests
from bs4 import BeautifulSoup
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

def search_answer(instructions):
    #this code section function is to search online
    query = instructions
    print("query = ", query)
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"

    } 
    
    url_search = f"https://google.com/search?q={query}"


    answer = requests.get(url_search,headers=headers)
    print("status code= ", answer.status_code)
    
    soup = BeautifulSoup(answer.text, 'html.parser')
    answers = []
    
    for result in soup.select('.tF2Cxc'):
        url = result.a['href']
        title = result.a.text
        answers.append((title,url))

    if len(answers) > 0:
        print("top search results: ", + answers)
        talk_back("The top search result is: " + answers[0][0])
    else:
        talk_back("No search results were found for " + query)


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

    elif "search for" in instructions:
        instructions = instructions.replace('search for', "")
        print("Virtual assistant: " , search_answer(instructions))

    elif "tell me about" in instructions:
        figure = instructions.replace('tell me about', "")
        biography = wikipedia.summary(figure, 1)
        print("virtual assistant: ", biography)
        talk_back(biography)