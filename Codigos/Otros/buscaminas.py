import pyautogui
import time

# Espera 5 segundos antes de comenzar a escribir
time.sleep(5)

# Escribe la palabra en el teclado
for i in range(0,10):
    pyautogui.typewrite("Hola Mundo")
# Presiona Enter
    pyautogui.press("enter")



