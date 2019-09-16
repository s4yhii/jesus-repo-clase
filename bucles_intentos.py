import math
print("programa para hallar la raiz cuadrada")
numero=int(input("ingrese un numero:"))
intentos=0
while numero<0:
    print("no se puede hallar la raiz cuadrada")
    if intentos==2:
        print("has consumido todos tus intento, gracias")
        break;
    numero=int(input("ingrese otro numero:"))
    if numero<0:
        intentos+=1
if intentos<2:
    solucion=math.sqrt(numero)
    print(f"la raiz cuadrada es: {solucion:.2f}")


