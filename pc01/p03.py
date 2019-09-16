ta=float(input("ingrese la nota de tareas: "))
ep=float(input("ingrese la nota del parcial: "))
ef=float(input("ingrese la nota del final: "))
sistema=input("ingrese el tipo de sistema de evaluacion: ")
if sistema=="F":        
    promedi=((ta+ep)*3/10)+((ef)*4/10)
    print(f"su promedio final es: {promedi:.2f}")
if sistema=="G":
    promedio=((ta+ep)/2+ef)/2
    print(f"su promedio final es: {promedio:.2f}")

