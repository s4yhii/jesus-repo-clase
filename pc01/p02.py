numero=int(input("ingrese un numero : "))
a=int((numero%10))
b=int((numero/10)%10)
c=int((numero/100)%10)
d=int((numero/1000)%10)
if a==d and b==c:        
     print("el numero es capicua")   
if  (numero//100)%10!=0:
     if a==c:
        print("el numero es capicua")  
     else:
        print("el numero no es capicua")          
else:
    print("el numero no es capicua")


