# print("""
#       Eliga la opcion que pertenece: 
      
#       1. Administrativo
#       2. Ejecutivo
#       3. Auxiliar
      
      
#       """) 
tipo = 1
horas = 199
años = 8
match tipo:
    case 1:
        salario = 2_000_000
    case 2:
        salario = 3_000_000
    case 3:
        salario = 1_500_000
    case _:
        print("No se sabe el tipo del empleado")
        salario = None
    
if horas >= 192:
    horas_extra = (horas - 192)
    valor_hora = salario / 192
    
    horas_extra = horas_extra * valor_hora * 1.20
    
    if años > 5:
        salario = (salario + horas_extra) * 1.20
        
    print(f"El salario total es: {salario}")
else:
    print("No se puede calcular el salario")
    

    
    



    