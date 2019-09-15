#ejercicio1
a=12
b=13
c=10
promedio=(a+b+c)/3
print(f"tu promedio de practicas es: {promedio:.2f}")
#ejercicio2
d=10
e=11
f=12
g=13
prom=(d+e+f+g-min(d,e,f,g))/3
print(f"tu otro promedio de practicas es: {prom:.2f}")
#ejercio3
precio=int(input("Ingrese el precio del articulo:"))
precio2=precio*0.18
print(f"El igv es: {precio2:.2f}")
#ejercicio4
subtot=int(input(f"Ingrese el subtotal:"))
total=subtot*0.82
print(f"El monto total es:{total:.2f}")
#ejercicio5
promedi=3.9
if 0<=promedi and promedi<3:
    print("En observación")
if 3<=promedi and promedi<4.5:
    print("Bueno")
if 4.5<=promedi and promedi<=5:
    print("Sobresaliente")
#ejercicio6
A="Computo"
B="TV"
C="Celulares"
D="Entretenimiento"
E="Electrohogar"
F="Infantil"
print(F)
#ejercicio10
año=int(input("Ingrese el año:"))
X=año%4
Y=año%100
if X==0 and Y!=0:
    print("Año bisiesto")
else:
    print("Año no bisiesto")






