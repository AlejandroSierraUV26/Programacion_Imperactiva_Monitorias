# import tkinter as tk 
# from tkinter import messagebox, simpledialog



# ventana = tk.Tk()

# ventana.title("Mi primera ventana")
# ventana.resizable(0,0)

# # Distrubucion de la ventana
# ventana_width=800
# ventana_height=500
# screen_width=ventana.winfo_screenwidth()
# screen_height=ventana.winfo_screenheight()
# x=(screen_width/2)-(ventana_width/2)
# y=(screen_height/2)-(ventana_height/2)
# ventana.geometry(f'{ventana_width}x{ventana_height}+{int(x)}+{int(y)}')

# espacio1 = tk.Frame(ventana, width=400, height=250, bg="red")

# texto = tk.Label(espacio1, text="Hola mundo", font=("Arial", 20), padx=10)
# texto.grid(row=0, column=0)


# texto = tk.Label(espacio1, text="Hola mundo", font=("Arial", 20), padx=10)
# texto.grid(row=1, column=1)


# texto = tk.Label(espacio1, text="Hola mundo", font=("Arial", 20), padx=10)
# texto.grid(row=2, column=2)


# texto = tk.Label(espacio1, text="Hola mundo", font=("Arial", 20), padx=10)
# texto.grid(row=3, column=3)

# texto = tk.Label(espacio1, text="Hola mundo", font=("Arial", 20), padx=10)
# texto.grid(row=4, column=4)

# espacio1.pack()

# espacio2 = tk.Frame(ventana, width=400, height=250, bg="green")
# espacio2.pack()
# ventana.mainloop()


import customtkinter
from PIL import Image, ImageTk
    
window = customtkinter.CTk()
window.geometry("1000x1000")
    
button_image = customtkinter.CTkImage(Image.open(fr"Clase 10\img.jpeg"), size=(800, 400))
texto = customtkinter.CTkLabel(master=window, image= button_image, text = "")

texto.pack()
    
window.mainloop()

