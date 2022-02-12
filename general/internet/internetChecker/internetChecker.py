import time
import os
import urllib.request
from playsound import playsound

def tryConnection():
    host = "https://duckduckgo.com"
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def main():
    while True:
        connected = tryConnection()
        if connected:
            print("Success! You're Connected!")
            time.sleep(5)
            os.system('cls')
            continue
        elif not connected:
            print("Failure! Unconnected!")
            directory = os.path.dirname(os.path.abspath(__file__))
            soundEffect = "Bruh.mp3"
            soundPlay = directory + ("\\" + soundEffect)
            playsound(soundPlay)
            time.sleep(30)
            os.system('cls')
        else:
            continue
main()