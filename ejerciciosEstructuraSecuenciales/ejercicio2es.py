#Construya un algoritmo que calcule el perímetro y el área de un rectángulo dada su base y su altura. La base y la altura deberán ser almacenadas previamente en dos variables respectivamente. El algoritmo debe mostrar en pantalla el siguiente mensaje: El perímetro del rectángulo es: xxx el área del rectángulo es: yyyy
#Nota: Se debe consultar la fórmula para hallar el perímetro y el área de un rectángulo.

base=float(input("Digite la base del rectángulo: "))
#Se le pide el valor de la base del rectángulo
altura=float(input("Digite la altura del rectángulo: "))   
#Se le pide el valor de la altura del rectángulo              
area=base*altura
#Se realiza la operación para averiguar el area del rectángulo
defi1=round(area,1)
#redondea el resultado del area
perimetro=base+base+altura+altura
#Se realiza la operación para averiguar el perimetro del rectángulo
defi2=round(perimetro,1)
#redondea el resultado del perimetro
print("El area del rectángulo es: ", defi1, "y el perimetro de este es:", defi2,)

