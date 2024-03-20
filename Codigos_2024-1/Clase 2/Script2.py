import pyautogui
import time

time.sleep(5)
for i in range(0,1000):
    pyautogui.write("Hola Mundo")
    pyautogui.press('enter')

