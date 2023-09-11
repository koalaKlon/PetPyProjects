from gtts import gTTS
from playsound import playsound


text = input("input your text: ")
language = "en"

obj = gTTS(text=text, lang=language, slow=False)
obj.save("test.mp3")

playsound("test.mp3")








