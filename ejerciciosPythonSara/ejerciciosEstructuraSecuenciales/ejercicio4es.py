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