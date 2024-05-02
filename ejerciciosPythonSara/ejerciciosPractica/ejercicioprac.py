import random
compra=int(input("Digite el valor de la compra: "))
colores = ["verde", "amarilla", "roja", "blanca"] 
balota=random.choice(colores)
print (balota)
if balota == "verde":
    descuento = 1.0
    print(f"la balota {balota}  tiene un descuento del 100%")
elif balota == "amarilla":
    descuento = 0.75
    print(f"la balota {balota} tiene un descuento del 75%")
elif balota == "roja":
    descuento = 0.5
    print(f"la balota {balota} tiene un descuento del 50%")
elif balota == "blanca":
    descuento = 0.0
    print(f"la balota {balota} no tiene descuento")
totalCompra=compra * (1-descuento)
print(f"Valor de la compra: {compra}") 
print(f"Color de balota: {balota}") 
print(f"Valor a pagar: {totalCompra}") 
