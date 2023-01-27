import random
import speech_recognition as sr
import pyttsx3
import cv2



def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic, duration=0.2)
        audio = r.listen(mic)
        MyText=""
        try:
            MyText = r.recognize_google(audio)
        except sr.RequestError as e:
            return 0
    return MyText


x=get_audio()
print(x)


    if (x= "grab"):
        fingers = [0, 0, 0, 0, 0]
        mySerial1.sendData(fingers)
        print("grab")

    elif (x="release"):
        fingers = [1, 1, 1, 1, 1]
        mySerial1.sendData(fingers)
        print("release")

    elif (x="index"):
        fingers = [0, 1, 0, 0, 0]
        mySerial1.sendData(fingers)
        print("release")

    else:
        print("No Command")