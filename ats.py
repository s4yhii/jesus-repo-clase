#funcion
def suma(n1,n2):
    resultado=n1**n2
    return resultado
print(suma(3,4))
#condicional con funcion
nota=input("ingrese la nota del alumno:")
def evaluacion(nota):
    valoracion= "aprobado"
    if nota<=5:
        valoracion= "riesgo academico"
    return valoracion
print(evaluacion(int(nota)))

#condicionales
print("asignaturas para el 2019: marketing,contabilidad,informatica")
opcion=input("escriba la carrera a escoger: ")
asignatura=opcion.lower() #lower sirve para poner en minuscula el texto ingresado y upper para ponerlo en mayuscula
if asignatura in ("marketing","contabilidad","informatica"):
    print(f"asignatura elegida : {asignatura}")
else:
    print("la asignatura escogida no es valida")

#bucles
for i in range(3 , 8): #contara desde 4 hasta 7
    suma=i**3+i**4
print(suma)
for i in range(4,30,3):  #el tercer valor es de cuanto en cuanto queremos que salte
    print(f"valor de la variable{i}")
#bucles
for i in range(5):
    print(i)

#bucles con len
valido=False
email=input("ingrese su email:")
for i in range(len(email)):
    if email[i]=="@":
        valido=True
if valido==True:
    print("email correcto")
else:
    print("email incorrecto")
