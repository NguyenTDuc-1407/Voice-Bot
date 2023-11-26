import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text, lang='vi')
    os.remove('voice.mp3')
    filename = 'voice.mp3'
    tts.save(filename)
    time.sleep(1)
    playsound.playsound(filename)

speak("mệt quá")
