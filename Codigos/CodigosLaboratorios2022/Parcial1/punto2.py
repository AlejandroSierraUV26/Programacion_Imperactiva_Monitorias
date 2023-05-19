"""
Autor: Alejandro Sierra Betancourt
Fecha: 8 de Abril 2022
Descripcion: Registro tienda
"""
def panaderia(n_productos):
    t_postre = 0
    t_pan = 0
    t_bebidas = 0

    n_postres = int(input("Ingrese el numero total de postres: "))
    for x in range(0, n_postres):
        valor_postre = float(input("Ingrese el precio del postre: "))
        t_postre = valor_postre + t_postre
    n_panes = int(input("Ingrese el numero total de panes: "))
    for y in range(0, n_panes):
        valor_pan = float(input("Ingrese el precio del pan: "))
        t_pan = valor_pan + t_pan
    n_bebidas = int(input("Ingrese el numero total de bebidas: "))
    for y in range(0, n_bebidas):
        valor_bebidas = float(input("Ingrese el precio del bebidas: "))
        t_bebidas = valor_bebidas + t_bebidas
    if n_productos == n_panes + n_bebidas + n_postres:
        return(f"Los postres tienen un valor de {t_postre} \n los panes de {t_pan} \n las bebidas un valor de {t_bebidas}.\n El total del inventario es por: {t_bebidas + t_postre + t_pan}")
    else:
        return("Los valores no concuerdan con el numero de productos, intenta de nuevo.")


n_productos = int(input("Ingrese el numero de productos: "))
print(panaderia(n_productos))
