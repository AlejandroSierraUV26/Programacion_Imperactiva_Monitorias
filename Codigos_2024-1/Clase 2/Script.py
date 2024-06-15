import pyautogui
import time

def escribir_y_enter(palabra):
    pyautogui.write(palabra)  # Escribe la palabra
    pyautogui.press('enter')  # Simula la pulsación de la tecla "Enter"

# Ejemplo de usodo

palabra_a_escribir = "MENSAJE"
time.sleep(5)
for i in range(0,10):
    escribir_y_enter(palabra_a_escribir)
    time.sleep(0.1)