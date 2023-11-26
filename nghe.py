import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening")
    audio =robot_ear.record(mic, duration=5)
try:
 you = robot_ear.recognize_google(audio,language="vi")
except:
    you ="try agian"

print(you)