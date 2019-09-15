#ejercicio8
num1=int(input("ingrese un numero menor que 1000: "))
num2=int(input("ingrese otro numero menor que 1000:"))
if num1<1000 and num2<1000 :
    a=int((num1/10)%10)
    b=int((num2)%10)
    c=int((num2/100)%10)
    suma=a+b+c
    union=(f"{a}{b}{c}")
    print(f"el numero formado es: {union}")
    print(f"la suma de los digitos es: {suma}")
else:
    print("los numeros ingresados son incorrectos")

