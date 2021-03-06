import time
import speech_recognition as sr
import webbrowser
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexa_speak("Sorry, I did not get that.")
        except sr.RequestError:
            alexa_speak("Sorry, my speech service is down.")
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang = 'en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        alexa_speak('My name is Alexa')
    elif 'what time is it' in voice_data:
        alexa_speak(time.ctime())
    elif 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexa_speak('Here is what I found: ')
    elif 'find location' in voice_data:
        location = record_audio('What is the location? Specify a city and state.')
        url = 'https://google.ml/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexa_speak('Here is what I found: ')
    elif 'exit' in voice_data:
        exit()
        

time.sleep(1)
print('How can I help you?')
while 1:   
    voice_data = record_audio()
    respond(voice_data)
