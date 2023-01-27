import random
import speech_recognition as sr
import pyttsx3
import cv2
import cvzone

mySerial1 = cvzone.SerialObject("COM3", 9600, 1)


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

def check_word(sentence, word):
    if sentence.find(word) != -1:
        return True
    else:
        return 0

while True:

    sentence=get_audio()
    print(sentence)




    if ( check_word(sentence, "grab") == True or check_word(sentence, "Grab") == True ):
        fingers = [0, 0, 0, 0, 0]
        mySerial1.sendData(fingers)
        print("grab")

    elif ( check_word(sentence, "release") == True or check_word(sentence, "Release") == True ):
        fingers = [1, 1, 1, 1, 1]
        mySerial1.sendData(fingers)
        print("release")

    elif ( check_word(sentence, "index") == True or check_word(sentence, "Index") == True ):
        fingers = [0, 1, 0, 0, 0]
        mySerial1.sendData(fingers)
        print("release")

    else:
        print("No Command")


