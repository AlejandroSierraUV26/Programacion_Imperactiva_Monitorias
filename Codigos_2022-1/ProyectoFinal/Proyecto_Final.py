"""
Autores: 
        Carlos Stiven Ruiz Rojas(2259629)
        Juan Manuel Ramirez Agudelo(2259482)
        Juan David Rojas Narvaez(2259673)
        Alejandro Sierra Betancourt(2259559)
Fecha: 23 de junio del 2022
Descripcion: Proyecto Final - Fundamentos de Programacion Imperativa
"""
from ast import Global
from email.errors import InvalidMultipartContentTransferEncodingDefect
from signal import default_int_handler
import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#Funciones 
def inversion():
    try: 
        global inversion_inicial,porcentaje
        inversion_inicial= float(int1.get())
        if inversion_inicial >0:
            porcentaje= float(int2.get())
            return inversion_inicial,porcentaje
        else: 
            messagebox.showinfo(message=f"La inversion inicial no puede ser {inversion_inicial}", title="Advertencia")
    except ValueError:
        messagebox.showinfo(message="¡Campos vacios! o ¡Formato invalido!", title="Error")  
def flujo_tiempo():
    try: 
        global total
        n=1 
        flujo_periodo = int3.get()
        total(n,flujo_periodo)
    except ValueError:
        messagebox.showinfo(message="¡Campo vacio!  o ¡Formato invalido!", title="Error")  
cantidadarray=np.zeros(25)
flujoarray=np.zeros(25)
m=0
def total(n,flujo_periodo):
    global m    
    m= m+n
    global cantidadarray,flujoarray
    cantidadarray[m] = float(m)
    flujoarray[m] = float(flujo_periodo)
    label10.insert(END,"\n"+str(m)+'\t'+flujo_periodo)
def calculo():
    try: 
        inver= inversion_inicial
        porcen= porcentaje
        global Vpn
        Vf=0
        for i in range(1,m+1):
            Vf = Vf + (flujoarray[i]/(1+(porcen/100))**i)
        Vpn = round((-(inver) + Vf),1)
        
        if Vpn > 0:
            Vpn.astype(str)
            label11["text"]= Vpn
            label12["text"]= "Realizar"
        elif Vpn < 0:
            Vpn.astype(str)
            label11["text"]= Vpn
            label12["text"]= "No realizar" 
    except NameError:
        messagebox.showinfo(message="¡Campos vacio! , No presionaste un boton  o ¡Formato invalido!", title="Advertencia")
#Configuración de la ventana
ventana=Tk()
ventana_width=950
ventana_height=750
screen_width=ventana.winfo_screenwidth()
screen_height=ventana.winfo_screenheight()
x=(screen_width/2)-(ventana_width/2)
y=(screen_height/2)-(ventana_height/2)
ventana.geometry(f'{ventana_width}x{ventana_height}+{int(x)}+{int(y)}')
ventana.title("Valor Presente Neto")
ventana.configure(bg="#95d5b2", borderwidth=20)
ventana.resizable (True,True)
#frame
frame = Frame(ventana)
frame.grid(row=7,column=1)
#Labels
label1=Label(ventana,text="Gestión del proyecto",bg="#95d5b2",font="Helvetica 36 bold underline")
label1.grid(row=0,column=1)
label2=Label(ventana,text="Datos del proyecto",bg="#95d5b2",font="Helvetica 18 bold")
label2.grid(row=1,column=1)
label3=Label(ventana,text="Inversión inicial",bg="#95d5b2",font="Helvetica 12 bold underline")
label3.grid(row=2,column=0)
label4=Label(ventana,text="Porcentaje de rendimiento (%)",bg="#95d5b2",font="Helvetica 12 bold underline")
label4.grid(row=3,column=0)
label5=Label(ventana,text="Peridos de tiempo del proyecto",bg="#95d5b2",font="Helvetica 18 bold")
label5.grid(row=4,column=1)
label6=Label(ventana,text="Flujo del periodo",bg="#95d5b2",font="Helvetica 12 bold underline")
label6.grid(row=5,column=0)
label7=Label(ventana,text="Información",bg="#95d5b2",font="Helvetica 18 bold")
label7.grid(row=6,column=1)
label8=Label(ventana,text="Vpn:",bg="#95d5b2",font="Helvetica 18 bold")
label8.grid(row=9,column=0)
label9=Label(ventana,text="Decisión:",bg="#95d5b2",font="Helvetica 18 bold")
label9.grid(row=9,column=2)
label10= Text(frame, height= 20, width= 70,font="Helvetica 8 bold", borderwidth=15)
label10.insert('1.0',"Periodo\tUtilidad")
label10.grid()
label11=Label(ventana,text="No calculado",bg="#95d5b2",font="Helvetica 18 bold")
label11.grid(row=10,column= 0)
label12=Label(ventana,text="No calculado",bg="#95d5b2",font="Helvetica 18 bold")
label12.grid(row=10,column= 2)
#Entradas
int1=Entry(ventana, borderwidth=10)
int1.grid(row=2,column=1)
int2=Entry(ventana, borderwidth=10)
int2.grid(row=3,column=1)
int3=Entry(ventana, borderwidth=10)
int3.grid(row=5,column=1)
#Botones
boton1=Button(ventana,text="Establecer datos", command= inversion, borderwidth=10)
boton1.grid(row=2,column=2, ipadx=20, ipady=10)
boton2=Button(ventana,text="Ingresar periodo", command= flujo_tiempo, borderwidth=10)
boton2.grid(row=5,column=2, ipadx=20, ipady=10)
boton3=Button(ventana,text="Calcular Vpn", command = calculo, borderwidth=10)
boton3.grid(row=8,column=1,rowspan=4, ipadx=20, ipady=10)
ventana.mainloop()