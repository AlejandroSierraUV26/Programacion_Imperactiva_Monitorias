import tkinter as tk
import tkinter.messagebox as mb
from PIL import ImageTk, Image
def saludar():
    mb.showinfo("Saludo", "Hola, bienvenido a mi restaurante")

root = tk.Tk()
root.geometry("400x300")

frame = tk.Frame(root, width=200, height=150)
frame.configure(bg="blue")  # Cambiar el color de fondo del frame a azul

label = tk.Label(root)
img = Image.open(r"descarga.png")
photo = ImageTk.PhotoImage(img)
label.config(image=photo)
label.image = photo  # Mantener una referencia para evitar que la imagen sea eliminada por el recolector de basura



label.pack()

frame.grid(row = 0, column=0)

frame2 = tk.Frame(root, width=200, height=150)
texto1 = tk.Label(frame2, text="Hola, bienvenido a mi restaurante")
texto1.configure(font=("Arial", 10), fg="black")
frame2.configure(bg="red")  

texto1.grid(row=0, column=0)
frame2.grid(row = 0, column=1)

frame3 = tk.Frame(root, width=200, height=150)
frame3.configure(bg="red")  # Cambiar el color de fondo del frame a azul


frame3.grid(row = 1, column=0)



frame4 = tk.Frame(root, width=200, height=150)
frame4.configure(bg="blue")  # Cambiar el color de fondo del frame a azul
boton1 = tk.Button(frame4, text= "Saludar", command=saludar)
boton1.pack()

frame4.grid(row = 1, column=1)

root.mainloop()



f""