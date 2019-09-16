#ejercicio de bucle infinito
num1=int(input("ingrese un numero: "))
num2=int(input(f"ingrese un numero mayor que {num1} :"))

while num2 >= num1:         #while es un bucle que significa mientras
    num1=num2
    num2=int(input(f"ingrese un numero mayor que {num1} : "))
print()
print("el numero ingresado es incorrecto")

#ejercicio de bucle con sumatoria
num3=int(input(f"ingrese un numero:"))
suma=0
while num3>=0 :
    suma = suma + num3
    num3=int(input(f"ingrese otro numero:"))
print()
print(f"la suma de los numeros introducidos es:{suma}")







