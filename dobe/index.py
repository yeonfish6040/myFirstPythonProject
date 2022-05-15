import pyautogui
from pynput.keyboard import Listener, Key

text = input("Input: ")

escPress = False

while not escPress:
    pyautogui.write(text)
    pyautogui.press('enter')