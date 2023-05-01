import speech_recognition as sr
import pyttsx3, nltk
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

#defining and creating virtual assistant's responses. For this we will use prompt-answer format
dialogs = [
    #setting forms of greeting user
    [
        r"i am (.*)", ["Hello %1, What can I do for you today?"]
    ],
    [
        r"hey there|hello|how are you|hi", ["Hey, do you need my assistance?"]
    ],
    #Creating answers to intro prompt
    [
        r"what is your name|how should i call you|do you have a name", ["My name is Nyx, I am your virtual assistant. Nice to meet you!"]
    ],
    #Starting to describe actions
    [
        r"search for (.*)", ["Searching %1...", "Here is what I found for %1"]
    ],
    [
        r"send a message to (.*) |send an email to (.*)", ["Sure, what should I type?"]
    ],
    #Anything else, say that you don't know the answer
    [
        r"(.*)", ["I am sorry, I do not understand, do you mind repeating?", "Oops, I did not catch that, repeat please!", "Someone needs to practice diction, try saying it again slower!"]
    ]
]


#defining chatbot using imported Chat and reflections plus our dialogs (created above)
chatbot = Chat(dialogs, reflections)

#funtion to hear user's voice input and return text
def get_audio():
    with sr.Microphone() as source:
        print("Can I help you with anything? I am listening...")
        audio = recog_engine.listen(source)

        try:
            message = recog_engine.recognize_google(audio)
            print("you said: ", message)
            return message
        except:
            print("SOrry, I didn't understand you!")
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
    user_message = get_audio().lower()

    if user_message == "":
        continue
    answer = chatbot.respond(user_message)
    print("Virtual assistant: ", answer)
    talk_back(answer)

