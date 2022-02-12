import mouse
import pyautogui

#print out the resolution of the screen
print(pyautogui.size())
print()
print("Moving to (0, 0)")
#move the mouse to the top left corner
pyautogui.moveTo(0, 0, duration = 1)
print()
input("Press ENTER to start collection mouse coordinates")
print()
#constantly getting the location of the mouse and printing it out
while True:
    
    print(mouse.get_position())
