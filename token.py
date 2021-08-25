from gtts import gTTS
from playsound import playsound
import os

token = input('Enter token number ')
txt = "ടോക്കൺ നമ്പർ " + token
txt2 = 'Hello how are you?'

ob = gTTS(text=txt, lang='ml')
ob.save("token.mp3")
os.system('token.mp3')
playsound('token.mp3')

ob2 = gTTS(txt2, lang='en')
ob2.save('hello.mp3')
playsound('hello.mp3')