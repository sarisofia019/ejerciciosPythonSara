#Construya un algoritmo que calcule el sueldo total de un vendedor, dado su sueldo base y las comisiones de sus ventas. Para esto es necesario definir una variable que almacene el nombre del vendedor, una variable que almacene el sueldo y otra variable que almacene el valor de la comisión de las ventas realizadas. Se debe calcular el valor final de sueldo. El algoritmo debe imprimir el nombre del vendedor, el valor del sueldo, el valor de su comisión y el sueldo total del vendedor. Ejemplo: El vendedor Pepito Pérez, tiene un sueldo de xxxx, durante el mes obtuvo una comisión de yyyy y el valor final a pagar es: zzzz
nombreVendedor=(input("Digite el nombre del vendedor: "))
#se exige que el vendedor digite su nombre
sueldo=int(input("Digite el sueldo: "))
#se exige que el vendedor digite su sueldo
ventas=int(input("Digite el total de ventas: "))
#se exige que el vendedor digite el total de ventas hechas
comision=int(input("Digite la comisión: "))
#se exige que el vendedor digite su comisión
totalComision=ventas*comision
#se multiplica las ventas con la comision
defi= sueldo+totalComision
#se suma el total de la comision con el sueldo
print("El vendedor ", nombreVendedor, "tiene un sueldo de: ", sueldo, " durante el mes obtuvo una comisión de: ", totalComision, "y el valor final a pagar es: ", defi, ) 