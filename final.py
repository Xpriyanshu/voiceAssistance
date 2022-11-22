import speech_recognition as sr
import pyttsx3
import requests
import aiml
import os

ses = requests.Session()
r = sr.Recognizer()

kernel = aiml.Kernel()

if os.path.isfile("brain.brn"):
    kernel.bootstrap(brainFile = "brain.brn") 
else:
    kernel.bootstrap(learnFiles = "model.aiml", commands = "load aiml")
    kernel.saveBrain("brain.brn")

engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.veena')   
    

while True:
    print('Listening...')
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            audio2 = r.listen(source2)
            inp = r.recognize_google(audio2)

            # inp = inp.lower()

            print('Did you say', inp)
            res = kernel.respond(inp)
            print(res)
            engine.say(res)
            engine.runAndWait()
            engine.stop()
            

    except sr.RequestError as e:
        print('Could not request results;', e)
        
    except sr.UnknownValueError:
        print('unknown error occured')