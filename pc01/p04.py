print("PROGRAMA DE APUESTAS")
apu=float(input("ingrese el valor para su apuesta:"))
intentos=2
numero=15
intentos=0
while apu>15  :
    if intentos<2:
         print("el numero ingresado es muy alto,intente de nuevo")   
    if intentos==2:
        print("has consumido todos tus intentos, fin del juego.")
        break;
    numero=int(input("ingrese otro numero:"))
    if apu!=15:
        intentos+=1

while apu<15   :
    if intentos<2:
        print("el numero ingresado es muy bajo,intente de nuevo")   
    if intentos==2:
        print("has consumido todos tus intentos, fin del juego.")
        break;    
    numero=int(input("ingrese otro numero:"))
    if apu!=15:
        intentos+=1   
            
if intentos<2 and apu==15:
    print("Respuesta correcta...")