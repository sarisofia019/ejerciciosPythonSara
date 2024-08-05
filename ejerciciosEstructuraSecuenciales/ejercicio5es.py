#Desarrolle un algoritmo que Programa que calcule el precio final de una compra, dado el valor de la compra y un descuento. Para esto es necesario declarar dos variables, una que guarde el valor de la compra y otra que almacene el valor del descuento. El algoritmo debe mostrar en pantalla, el valor de la compra el valor del descuento y el valor final a pagar. 
compra=int(input("Digite el valor de la compra: "))
#se exige que digite el valor de la compra
descuento=int(input("Digite el valor del descuento: "))
#se exige que digite el valor del descuento
total=compra*(descuento/100)
#se resta el valor del descuento a la compra
print("La compra fue de ", compra, ", con un descuento de", descuento, " y el valor final a pagar es de: ", total, )
