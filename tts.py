from gtts import gTTS
import os
speech=gTTS(text="Hello prasanth,How are you?",lang="en")
speech.save('sample.mp3')
os.system('mpg321 sample.mp3')
