compra = int(input("Digite el valor de las zapatillas: "))
#se pide el valor de las zapatillas
cantidad = int(input("Digite la cantidad de zapatillas que compró: "))
#se pide la cantidad de zapatillas que va a comprar
if cantidad >= 3:
    descuento=compra*0.2
    total=compra-descuento
    print(f"el valor de la compra con descuento de 20% es de {total}: ")
#se imprime que si compra 3 o más zapatillas tiene un descuento del 20%    
else:
    cantidad < 3
    descuento = compra*0.1
    total=compra-descuento
    print(f"el valor de la compra con descuento de 10% es de {total}: ")
    #se imprime que si compra menos de 3 zapatillas tiene un descuento del 10%