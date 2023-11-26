import speech_recognition
from gtts import gTTS
import os
import playsound
from datetime import datetime
import webbrowser
import wikipedia
from selenium import webdriver
import time

now = datetime.now()


# voice
def speak(robot_brain):
    tts = gTTS(text=robot_brain, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


print("Robot: khởi động")

while True:
    # speech
    robot_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        audio = robot_ear.record(mic, duration=3)
    try:
        you = robot_ear.recognize_google(audio, language="vi")
        print("you: " + you)
    except:
        you = []

    # brain
    if you == "mở":
        robot_brain = "xin chào"
        print("robot: " + robot_brain)
        speak(robot_brain)
    elif you == "ngày":
        robot_brain = now.strftime("ngày %d tháng %m năm %Y")
        print("robot: " + robot_brain)
        speak(robot_brain)
    elif you == "giờ":
        robot_brain = now.strftime("%H:%M")
        print("robot: " + robot_brain)
        speak(robot_brain)
    elif you == "Open Google":
        robot_brain = "đã mở google"
        webbrowser.open_new_tab("http://www.google.com")
        print("robot: " + robot_brain)
        speak(robot_brain)
    elif you == "YouTube":
        robot_brain = "đã mở youtube"
        driver = webdriver.Chrome()
        driver.get("https://www.youtube.com/")
        print("robot: " + robot_brain)
        speak(robot_brain)
        robot_ear_test = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
            audio_text = robot_ear_test.record(mic, duration=3)
        try:
            you_text = robot_ear_test.recognize_google(audio_text, language="vi")
            print("you: " + you_text)
        except:
            you_text = []

        if you_text:

            search_box = driver.find_element('xpath',
                                             '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
            search_box.send_keys(you_text)

            search_button = driver.find_element('xpath',
                                                '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button')
            search_button.click()

            time.sleep(2)
            driver.find_element('xpath',
                                '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string').click()

        else:
            robot_brain = "thoát youtube"
            print("robot: " + robot_brain)
            speak(robot_brain)

    elif you == "Wiki":
        robot_brain = "đã mở wiki"
        print("robot: " + robot_brain)
        speak(robot_brain)
        robot_ear_test = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as mic:
            audio_test = robot_ear_test.record(mic, duration=3)
        try:
            you_text = robot_ear_test.recognize_google(audio_test, language="vi")
            print("you: " + you_text)
        except:
            you_text = []
        if you_text:
            wikipedia.set_lang("vi")
            robot_brain = wikipedia.summary(you_text, sentences=1)
            print("robot: " + robot_brain)
            speak(robot_brain)
        else:
            robot_brain = "thoát wiki"
            print("robot" + robot_brain)
            speak(robot_brain)

    elif you == "tắt":
        robot_brain = "sleep"
        print("robot: " + robot_brain)
        speak(robot_brain)
        break
    else:
        robot_brain = "thử lại"
        print("robot: " + robot_brain)
        # speak(robot_brain)
