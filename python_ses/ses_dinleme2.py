import speech_recognition as sr
from gtts import gTTS

r = sr.Recognizer()
with sr.Microphone() as source:
    print("dinlemedeyem")
    audio = r.listen(source)
    metin = str(r.recognize_google(audio,language = "tr"))
    print("dediginiz soz:"+metin)
