import aiml
import speech_recognition as sr
import pyttsx
#from time import 
import os

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "chitti_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("chitti_brain.brn")

def vocalize(audioStr):
    print audioStr
    engine = pyttsx.init()
    engine.say(audioStr)
    engine.runAndWait()

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

while True:
    data = recordAudio()
    if "exit" in data:
        break
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        vocalize("Locating " + location)
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

    elif len(data)!=0:
        ProData = kernel.respond(data)
        vocalize(ProData)
