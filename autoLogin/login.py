from pynput.keyboard import Listener, Key
import pyautogui

releaseKey = ""

def handleKeyPress(key):
    pass
 
def handleKeyRelease(key):
    try:
        global releaseKey
        ok = False
        for i in "20220413":
            if i == key.char:
                releaseKey = releaseKey + key.char
                ok = True
                break

        if not ok:
            releaseKey = ""

        print(releaseKey)

        if releaseKey == "20220413":
            pyautogui.keyDown('ctrl')  # hold down the shift key
            pyautogui.press('a')
            pyautogui.keyUp('ctrl')
            pyautogui.press('backspace')
            pyautogui.write("tnrwptlfgdj1818$mycomputer")
            pyautogui.press('enter')
            releaseKey = ""
        
        if releaseKey.__len__() > 8:
            releaseKey = ""
            
        if key == Key.esc:
            return False
    except AttributeError:
        pass
 
with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
    listener.join()
