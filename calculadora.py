'''
crea una calculadora donde puedas realizar  operaciones matematicas 
basicas como suma, resta, multiplicacion y division.
'''
#pedimos al usuario
number1 = int(input("ingresa el primer numero: "))

#pedimos el segundo numero
number2 = int(input("ingrese el segundo numero: "))

#colocamos eleccion  de la operacion a realizar en un bucle while

eleccion = 0
#colocamos !=6  para seguir realizan las  operaciones hasta que se ingrese 6
while eleccion !=6:
    print("""
    Indique la operacion a realizar
        
        1) suma
        2) resta
        3) multiplicacion
        4) division
        5) cambio de valores
        6) salir
        """)
    
    
    eleccion = int(input())

    if  eleccion == 1: #suma
        print(" ")#colocamos este print vacio  para que no se impriman los numeros antes de mostrar el resultado
        print("resultado: ", number1,"+",number2, "=" , number1 + number2 )
    
    if eleccion == 2:#resta
        print(" ")
        print("resulrado: ",number1,"-",number2,"=", number1-number2)

    if  eleccion == 3:#multiplicacion
        print(" ")
        print("resultado :",number1,"*",number2,"=",number1*number2)

    if  eleccion == 4: #division
        print(" ")
        print("resultado :",number1,"/",number2,"= ",number1/number2)
    
    
    if eleccion == 5:
        #se repite  el bucle para cambiar los numeros
        #pedimos al usuario
         number1 = int(input("ingresa el primer numero: "))
        #pedimos el segundo numero
         number2 = int(input("ingrese el segundo numero: "))