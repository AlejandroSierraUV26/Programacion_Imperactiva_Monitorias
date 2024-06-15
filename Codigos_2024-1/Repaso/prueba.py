import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk


class VentanaLogin(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Login")
        self.geometry("400x300")
        self.configure(bg="#1a1a1a")

        self.parent = parent

        self.label = tk.Label(self, text="Ingrese su nombre de usuario:", font=(
            "Times New Roman", 16), bg="#1a1a1a", fg="white")
        self.label.pack(pady=20)

        self.entry = tk.Entry(self, font=("Times New Roman", 14))
        self.entry.pack(pady=10)

        self.button_entrar = tk.Button(self, text="Entrar", font=(
            "Times New Roman", 14), bg="#4CAF50", fg="white", command=self.guardar_usuario)
        self.button_entrar.pack(pady=20)

        self.grab_set()

    def guardar_usuario(self):
        usuario = self.entry.get()
        if usuario:
            with open("usuarios.txt", "a") as file:
                file.write(usuario + "\n")
            self.parent.deiconify()
            self.destroy()
        else:
            self.label.config(
                text="Por favor, ingrese un nombre de usuario", fg="red")


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("¿QUIÉN QUIERE SER MILLONARIO?!")
        self.geometry("1280x820")
        self.configure(bg="#1a1a1a")
        self.preguntas_mostradas = []
        self.crear_interfaz()

        self.withdraw()
        VentanaLogin(self)

    def crear_interfaz(self):
        # Añadir imagen
        self.img = Image.open("Imageninicio.png")
        self.img = self.img.resize((200, 200), Image.ANTIALIAS)
        self.img_tk = ImageTk.PhotoImage(self.img)

        self.label_img = tk.Label(self, image=self.img_tk, bg="#1a1a1a")
        self.label_img.pack(pady=20)

        tk.Label(self, text="¡Bienvenido a ¿Quién quiere ser millonario?!", font=(
            "Times New Roman", 24, "bold"), bg="#1a1a1a", fg="white").pack(pady=20)
        tk.Button(self, text="INICIAR", font=("Times New Roman", 15), height=2,
                  width=20, bg="#4CAF50", fg="white", command=self.start_action).pack(pady=20)
        tk.Button(self, text="SALIR", font=("Times New Roman", 15), height=2,
                  width=20, bg="#f44336", fg="white", command=self.salir).pack()

    def obtener_pregunta(self):
        lista = [
            """¿Qué palabra se usa para referirse a los abdominales bien marcados?
            A. Lavadora
            B. Lavadero
            C. Lavanda
            D. Lavaloza""",
            "¿Cuál es el planeta más cercano al Sol?\nA. Venus\nB. Marte\nC. Mercurio\nD. Júpiter",
            "¿Cuál es el país más grande del mundo?\nA. Canadá\nB. China\nC. Estados Unidos\nD. Rusia",
            "¿Quién escribió 'Don Quijote de la Mancha'?\nA. William Shakespeare\nB. Gabriel García Márquez\nC. Miguel de Cervantes\nD. Jorge Luis Borges",
            "¿Cuál es la capital de Australia?\nA. Sídney\nB. Melbourne\nC. Canberra\nD. Perth",
            "¿En qué año llegó el hombre a la luna?\nA. 1965\nB. 1969\nC. 1972\nD. 1962"
        ]

        if len(self.preguntas_mostradas) == len(lista):
            self.preguntas_mostradas.clear()
            self.mostrar_mensaje(
                "Fin del juego", "¡Has respondido todas las preguntas disponibles!")
            self.deiconify()
            if hasattr(self, 'new_window') and self.new_window:
                self.new_window.destroy()
            return ""

        preguntas_disponibles = [
            pregunta for pregunta in lista if pregunta not in self.preguntas_mostradas]
        pregunta = random.choice(preguntas_disponibles)
        self.preguntas_mostradas.append(pregunta)

        return pregunta

    def comprobar_respuesta(self, respuesta, botones):
        for boton in botones:
            boton.config(state=tk.DISABLED)
        correcta = self.obtener_respuesta_correcta()
        if respuesta == correcta:
            salida = "¡Correcto! La opción {} es la respuesta correcta.".format(
                correcta)
        else:
            salida = "Respuesta incorrecta. La opción correcta era la {}.".format(
                correcta)
        self.mostrar_mensaje("Resultado", salida)

    def obtener_respuesta_correcta(self):
        pregunta_actual = self.new_window.pregunta_actual
        if "Lavadora" in pregunta_actual:
            return "A"
        elif "Mercurio" in pregunta_actual:
            return "C"
        elif "Rusia" in pregunta_actual:
            return "D"
        elif "Cervantes" in pregunta_actual:
            return "C"
        elif "Canberra" in pregunta_actual:
            return "C"
        elif "1969" in pregunta_actual:
            return "B"
        else:
            return "A"

    def cambiar_pregunta(self, new_window):
        pregunta = self.obtener_pregunta()
        if pregunta:
            new_window.actualizar_pregunta(pregunta)
            self.new_window = new_window
            for boton in new_window.botones:
                boton.config(state=tk.NORMAL)

    def start_action(self):
        self.withdraw()
        new_window = VentanaSecundaria(self, self.obtener_pregunta())
        self.cambiar_pregunta(new_window)

    def continuar_despues_respuesta(self):
        self.cambiar_pregunta(self.new_window)

    def salir(self):
        self.destroy()

    def mostrar_mensaje(self, titulo, mensaje):
        message_box = CustomMessageBox(self, titulo, mensaje)
        self.wait_window(message_box)


class CustomMessageBox(tk.Toplevel):
    def __init__(self, parent, titulo, mensaje):
        super().__init__(parent)
        self.title(titulo)
        self.geometry("400x200")
        self.configure(bg="#1a1a1a")
        self.parent = parent

        self.label = tk.Label(self, text=mensaje, font=(
            "Times New Roman", 14), bg="#1a1a1a", fg="white", padx=20, pady=20)
        self.label.pack()

        self.button_ok = tk.Button(self, text="Aceptar", font=(
            "Times New Roman", 12), bg="#4CAF50", fg="white", command=self.cerrar)
        self.button_ok.pack(pady=10)

        self.grab_set()

    def cerrar(self):
        self.parent.continuar_despues_respuesta()
        self.destroy()


class VentanaSecundaria(tk.Toplevel):
    def __init__(self, parent, label_text):
        super().__init__(parent)
        self.title("Preguntas")
        self.geometry("1280x820")
        self.configure(bg="#1a1a1a")
        self.parent = parent
        self.label_text = label_text
        self.pregunta_actual = ""

        self.crear_interfaz()

    def crear_interfaz(self):
        self.label = tk.Label(self, text=self.label_text, font=(
            "Times New Roman", 18), bg="#1a1a1a", fg="white")
        self.label.pack(pady=50)

        self.frame_botones = tk.Frame(self, bg="#1a1a1a")
        self.frame_botones.pack(pady=20)

        self.botones = []
        for texto in ['A', 'B', 'C', 'D']:
            boton = tk.Button(self.frame_botones, text=texto, font=("Times New Roman", 14), height=2, width=10,
                              bg="#4CAF50", fg="white", command=lambda t=texto: self.parent.comprobar_respuesta(t, self.botones))
            boton.pack(side=tk.LEFT, padx=20)
            self.botones.append(boton)

    def actualizar_pregunta(self, pregunta):
        self.pregunta_actual = pregunta
        self.label.config(text=pregunta)
        for boton in self.botones:
            boton.config(state=tk.NORMAL)


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
