import googletrans # googletrans==3.1.0a0
import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init()
recogonizer=sr.Recognizer()

with sr.Microphone() as source:
    print("wait for calibrations")
    recogonizer.adjust_for_ambient_noise(source,1)
    print("start speaking")
    audio=recogonizer.listen(source)
    print("recorded successfully")
    speech=recogonizer.recognize_google(audio)
    speech=speech.lower()
    print(speech)
    


def trans():
    print("Translating")
    print(googletrans.LANGCODES)
    language=input("Type the translation language code:").lower()
    translator=googletrans.Translator()
    translation=translator.translate(text=speech,dest=language)
    print("Translation: ",translation.text)
    engine.setProperty("rate",120)
    engine.say(translation.pronunciation)
    engine.runAndWait()

trans()
