import time
import urllib.request
import os

def test(url):

    try:
        urllib.request.urlopen(url)
        return True
    except:
        return False

def main():
    while True:
        os.system('cls')
        print("What would you like to do:")
        print("1. Test url")
        print("0. Exit")
        userChoice = int(input())

        if userChoice == 1:
            print()
            url = input("URL to test: ")
            success = test(url)

            if success:
                print()
                print("Success! Should be up")
                time.sleep(5)
            else:
                print()
                print("Failure! Might be down", "/n", "or you aren't connected")
                print("Check Connectivity and Try Again Later")
                time.sleep(5)
        else:
            break



main()