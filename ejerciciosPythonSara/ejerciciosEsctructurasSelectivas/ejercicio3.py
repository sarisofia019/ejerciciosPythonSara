compra = int(input("Digite el valor del monto total de la compra: "))
#se le pide al usuario que digite el monto de la compra
if compra > 500000:
    capacidadEmpresa=compra*0.55 
    prestamoBanco=compra*0.3
    credito=(compra*0.15)
    intereses=(credito)+(credito*0.20)
    #se define la cantidad de dinero de cada entidad para completar la compra teniendo en cuenta que supera el monto de 500000
    print(f"Puesto que el monto total de la compra supera los 500000, la empresa tendrá la capacidad de invertir {capacidadEmpresa}, pedir prestado al banco {prestamoBanco} y el resto lo pagará solicitando un crédito de {intereses} ") 
    #se imprime la suma de la cantidad de dinero que aporta cada entidad para realizar la compra dando como resultado el monto total que debe pagar la empresa 
else:
   compra <= 500000
   capacidadEmpresa=compra*0.7 
   credito=compra*0.3
   intereses=credito*0.2
   #se define la cantidad de dinero de cada entidad para completar la compra teniendo en cuenta que es menor o igual el monto de 500000
   print(f"Puesto que el monto total de la compra no supera los 500000, la empresa tendrá la capacidad de invertir {capacidadEmpresa}, y el restante {credito} lo pagará solicitando crédito al fabricante. El fabricante cobra por concepto de intereses un {intereses} sobre la cantidad que se le pague a crédito: ") 
    #se imprime la suma de la cantidad de dinero que aporta cada entidad para realizar la compra dando como resultado el monto total que debe pagar la empresa 