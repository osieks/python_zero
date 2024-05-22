from gtts import gTTS
import os
import playsound as sound

def create_audio_file(filename,myText):
    language = "pl"

    output = gTTS(text=myText,lang=language,slow=False)

    output.save(filename+".mp3")
    sound.playsound(filename+".mp3", True)

if __name__ == "__main__":
    create_audio_file("zasloniete","zasłonięte")