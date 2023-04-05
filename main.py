from playsound import playsound
import time
import os


def alarm():
    print("Enter the hour you want the glock to go off at: ") 
    time.sleep(1)
    notification()

def notification():
    print("WAKE UP WAKE UP WAKE UP")
    playsound('ALARM_SOUND_AFFECT.mkv')

alarm()

