#Elabore un algoritmo que calcule el promedio de tres números, los cuales deben ser almacenados previamente en tres variables. El algoritmo debe imprimir el siguiente mensaje: El promedio de los números ingresado es: xxxx
a=float(input("Digite un valor: "))
#Se le pide un valor
b=float(input("Digite el segundo valor: "))   
#Se le pide que ingrese el segundo valor 
c=float(input("Digite el tercer valor: "))   
#Se le pide que ingrese el segundo valor                           
promedio=(a+b+c)/3
#Se realiza la operación para averiguar el promedio
defi1=round(promedio,1)
#redondea el resultado del promedio
print("El promedio de los valores es: ", defi1,)
