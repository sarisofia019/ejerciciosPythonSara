a=int(input("Digite su primera calificación: "))
b=int(input("Digite su segunda calificación:"))
c=int(input("Digite su tercera calificación:"))
pension = int(input("Digite el valor de su pensión: "))
#se le pide al usuario que digite las calificaciones y el valor de su pensión
promedio=(a+b+c)/3
#Se realiza la operación para definir el promedio de las calificaciones
if promedio >= 9:
    descuento=pension*0.3
    defi=pension-descuento
    print (f"El descuento por tener un promedio igual o superior a 9 es del {descuento} dando un total a pagar de la pensión de {defi}")
    #se define el valor del descuento de acuerdo a si el promedio es igual o mayor a 9
else:
    promedio < 9
    iva=pension*0.1
    defi=pension+iva
    print (f"Por tener un promedio menor a 9 se debe de pagar la pensión completa y un iva de {iva} dando un total a pagar de {defi}")
#se define el valor del descuento de acuerdo a si el promedio es menor a 9