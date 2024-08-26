import random
compra=int(input("Digite el valor de la compra: "))
colores = ["verde", "roja", "blanca"] 
balota=random.choice(colores)
#se pide el valor de la compra 
print (balota)
#se genera una balota de color aleatorio
if balota == "verde":
    descuento = 0.2
    print(f"la balota {balota}  tiene un descuento del 20%")
elif balota == "roja":
    descuento = 0.15
    print(f"la balota {balota} tiene un descuento del 15%")
elif balota == "blanca":
    descuento = 0.0
    print(f"la balota {balota} no tiene descuento")
totalCompra=compra * (1-descuento)
#De acuerdo al color de la balota se genera un descuento a la compra
print(f"Valor de la compra: {compra}") 
print(f"Color de balota: {balota}") 
print(f"Valor a pagar: {totalCompra}") 
#Se imprime el valor de la compra de acuerdo al descuento que le da el color de la balota generada