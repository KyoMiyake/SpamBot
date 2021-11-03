from pynput.keyboard import Key, Controller
import time


keyboard = Controller()
t = True
msg = input("What do you want to be spammed?     ")
print("How long do you want between each message?")
s = input("(If it is less than a second, lay out as a float(e.g. .1, .2, .3, etc.))     ")
time.sleep(5)

while t == True:
    time.sleep(int(float(s)))
    keyboard.type(msg)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
