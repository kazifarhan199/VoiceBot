"""This file contains code that converts speach to text"""
import speech_recognition as sr

def get_text():
    """This function is going to listen and return text"""
    speech = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech.listen(source)
        try:
            text = speech.recognize_google(audio)
            return text
        except Exception:
            return 0
