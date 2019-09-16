import math
ladoa=float(input("ingrese el primer lado del triangulo"))
ladob=float(input("ingrese el segundo lado del triangulo"))
ladoc=float(input("ingrese el tercer lado del triangulo"))
if ladoa==ladob and ladoa==ladoc:
    print("el triangulo es equilatero")
elif ladoa==ladob and ladoa!=ladoc or ladoa==ladoc and ladob!=ladoc:
    print("el triangulo es isosceles")
else:
    print("el triangulo es escaleno")

if ladoa**2+ladob**2==ladoc**2 or ladob**+ladoc**2==ladoa**2 or ladob**2+ladoc**2==ladoa**2:
    print("el triangulo es rectangulo")
else:
    print("el triangulo no es rectangulo")
perimetro=ladoa+ladob+ladoc
semi=(ladoa+ladob+ladoc)/2
area= math.sqrt(semi*(semi-ladoa)*(semi-ladob)*(semi-ladoc))
print(f"el perimetro es: {perimetro:.2f}")
print(f"el area es : {area:.2f}")
