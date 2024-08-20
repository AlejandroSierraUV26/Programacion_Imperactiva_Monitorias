import cv2
import numpy as np
import pyt
import pytesseract
from pytesseract import Output

# Cargar la imagen
image = cv2.imread('Prueba 1\imagen.png')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro de mediana
gray = cv2.medianBlur(gray, 5)

# Aplicar un filtro de Canny
edges = cv2.Canny(gray, 50, 150)

# Encontrar los contornos
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Mostrar la imagen
cv2.imshow('Contornos', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Extraer el texto de la imagen
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(image, config=custom_config)
print(text)

# Extraer la información estructurada de la imagen
d = pytesseract.image_to_data(image, output_type=Output.DICT)
print(d.keys())

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
cv2.imshow('Contornos', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

