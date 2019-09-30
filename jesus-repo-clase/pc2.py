#imprimir los numeros de una lista
numeros=[1,2,3,4,5]
for i in numeros:
    print(i,end="")
#tambien
numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice+=1
#para modificar los numeros de una lista
indice = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    numeros[indice] *= 10
    indice+=1
print(numeros)
#programa con opciones
a=float(input("Ingrese un numero: "))
b=float(input("Ingrese otro numero: "))
print("sumar los numeros(1)")
print("restar los numeros(2)")
print("multiplicar los numeros(3)")
op=int(input("ingrese una ocpion:"))
suma=a+b
resta=a-b
multi=a*b
if op==1:
    print(suma)
elif op==2:
    print(resta)
elif op==3:
    print(multi)
else:
    print("la opcion ingresada no es correcta")
#Puedes utilizar la funciones sum() y range() para hacerlo más fácil.
#El tercer parámetro en la función range(inicio, fin, salto)
#indica un salto de números, pruébalo.
# Primera forma con función sum()
suma = sum( range(0, 101, 2) )
print(suma)

# Segunda forma con bucles
num = 0
suma = 0

while num <= 100:
    if num % 2 == 0:
        suma += num
    num += 1
print(suma)
#Realiza un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética.
suma = 0
numeros = int(input("¿Cuántos números quieres introducir? ") )
for x in range(numeros):
    suma += float(input("Introduce un número: ") )
print("Se han introducido", numeros, "números que en total han sumado",
        suma, "y la media es", suma/numeros)
#invertir una palabra con funcion
a=input("ingrese una palabra:")
def inversa(texto):
    invertida = " "
    for letra in texto:
        invertida = letra + invertida
    return invertida
print(inversa(a))
# funcion para hallar el mcd de dos numeros
def mcd(a, b):
    resto = 0
    while (b > 0):
        resto = b
        b = a % b
        a = resto
    return a
# solicitamos los dos números
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
print("El máximo común divisor de ", num1, " y ", num2, " es ", mcd(num1, num2))
#saber si un numero o una palabra es capicua con funcion
a=input("ingrese una numero: ")
def inversa(texto):
    invertida = ""
    for letra in texto:
        invertida = letra + invertida
    return invertida
if (a)==(inversa(a)):
    print("el numero es capicua")
else:
    print("el numero no es capicua")
#calcular la longitud de un segmento
import math
a=float(input("ingrese la coordenada x del punto P: "))
b=float(input("ingrese la coordenada y del punto P: "))
c=float(input("ingrese la coordenada x del punto Q: "))
d=float(input("ingrese la coordenada y del punto Q: "))
print("la longitud del segmento PQ es", math.sqrt((a-c)**2+(c-d)**2))