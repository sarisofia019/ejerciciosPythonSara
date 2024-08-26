cantidad = int(input("Digite la cantidad de llantas que va a comprar: "))
#se le pide al usuario que digite la cantidad de llantas que va a comprar
if cantidad < 5:
    precio=int(cantidad*300)
    print(f"el valor de la compra es de {precio} ")
    #Se define el valor de la compra teniendo en cuenta que se compran menos de 5 llantas
elif 5 <= cantidad <=10: 
   precio=int(cantidad*250)
   print(f"el valor de la compra es de {precio} ")
    #Se define el valor de la compra teniendo en cuenta que el número de llantas que se compra está en un rango de entre 5 y 10 llantas
else: 
    cantidad > 10
    precio=int(cantidad*200)
    print(f"el valor de la compra es de {precio} ")
    #Se define el valor de la compra teniendo en cuenta que se compran mas de 10 llantas