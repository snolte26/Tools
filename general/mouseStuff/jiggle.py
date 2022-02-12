from time import sleep as sleeper
from tqdm import tqdm
import os
import pyautogui


def main():
    mins = (int(input("How many minutes between jiggle: "))) * 60
    secs = int(input("How many seconds on top of minutes: "))
    sleepTime = mins + secs

    while True:
        os.system('cls')
        x, y = pyautogui.position()

        for _ in tqdm(range(sleepTime)):
            sleeper(1)
        pyautogui.moveTo(x + 150, y + 150, duration=.5)

        for _ in tqdm(range(sleepTime)):
            sleeper(1)
        pyautogui.moveTo(x - 150, y - 150, duration=.5)


if __name__ == '__main__':
    main()
