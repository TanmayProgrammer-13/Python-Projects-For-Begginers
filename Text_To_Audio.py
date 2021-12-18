from gtts import gTTS
import os

#Enter The Text You Want To Be Converted In Audio
Text_Enter = "Hello Everyone, This Program is Created By Mr Programmer In Python"

#Enter the Language In Which You Want To Listen The Text
Lang = 'en'

#creating an object
my_obj = gTTS(text=Text_Enter,lang=Lang,slow=False)

#Converting Your Text File Into Audio(.mp3 ) Format
my_obj.save("PyAudio.mp3")
print("Audio Saved")

os.system("PyAudio.mp3")