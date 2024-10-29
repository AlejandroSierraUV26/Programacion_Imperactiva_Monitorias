def tipo_emplea(x):
    if x == "ADMINISTRATIVO":
        return 2_000_000
    elif x == "EJECUTIVO":
        return 3_000_000
    elif x == "AUXILIAR":
        return 1_500_000
    else:
        return None

def hors_extra(horas_trabajadas, salario_base):
    horas_extra =  horas_trabajadas - 192
    return horas_extra * (salario_base / 192) * 1.20

def añitos(años_trabajados, salario_base):
    if años_trabajados > 5:
        return salario_base * 1.20
    return 0

if __name__ == "__main__":
    tipo_trabaja = "ADMINISTRATIVO"
    horas_trabaja = 199
    años = 8

    salario_base = tipo_emplea(tipo_trabaja)
    
    if salario_base is None:
        print("No se sabe el tipo del empleado")
    else:
        horas_extra = hors_extra(horas_trabaja, salario_base)
        salario_neto = salario_base + horas_extra
        añoses = añitos(años, salario_neto)
        print(salario_base, horas_extra, añoses)
        salario_total = añoses
        print(f"El {tipo_trabaja} para este mes ha ganado {salario_total}")