#ejercicio7
antiguedad=5
sueldo=300
if antiguedad>5:
    print(sueldo*1.2)
if antiguedad<=5 and antiguedad>1:
    print(sueldo*1.1)
else:
    print(sueldo)
#ejercicio9
control1=int(input("ingrese el primer peso"))
control2=int(input("ingrese el segundo peso"))
control3=int(input("ingrese el tercer peso"))
if control2-control1<300 :
    print("el incremento del control 2 y 1 es menor que 300g")
elif (control3-control2<300):
    print("el incremento del control 3 y 2 es menor que 300g")

#ejercicio de la sumatoria
tot=0
numero=4
for i in range(0,numero+1):
    tot=tot+(i**5+4*i**3+3*(i**2)+5)
print(tot)


