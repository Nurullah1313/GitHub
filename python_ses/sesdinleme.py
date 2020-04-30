from gtts import gTTS
import os
import speech_recognition as sr

"""tts = gTTS(text = 'Merhaba Nurullah bugün nasılsın',lang = 'tr')
tts.save('merhaba.mp3')
os.system('merhaba.mp3')"""
r = sr.Recognizer()

with sr.Microphone() as source:
    print('Birşeyler Söyle')
    audio = r.listen(source)
data = ''
try:
    data = r.recognize_google(audio, language = 'tr-tr')
    data = data.lower()
    print('Bunu söyledin : ' + data)
except sr.UnknownValueError:
    print('Ne dediğini anlamadım')
    

