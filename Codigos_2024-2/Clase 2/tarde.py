import pyautogui
import time 

def escribir_mensaje(palabra):
    pyautogui.write(palabra)
    pyautogui.press('enter')
    
time.sleep(4)
for i in range(100):
    escribir_mensaje("Hola TEEMO")