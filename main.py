from pydub import AudioSegment
from pydub.playback import play
import time
import os

def alarm():
    # Murica
    print("Enter the hour you want the glock to go off at: ") 
    time.sleep(1)
    notification()

def notification():
    print("WAKE UP WAKE UP WAKE UP")
    sound = AudioSegment.from_wav('/home/kenji/Desktop/WAKEUP-APP/sound-affects/alarm-affect.wav')
    play(sound)

alarm()

