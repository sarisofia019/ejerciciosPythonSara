a=float(input("Digite un valor: "))
#se pide la primera nota
b=float(input("Digite el segundo valor: "))  
#se pide la segunda nota 
c=float(input("Digite el tercer valor: "))         
#se pide la tercera nota                  
promedio=(a+b+c)/3
#se saca el promedio de las notas
defi1=round(promedio,1)
#se redondea el promedio
if defi1 > 70:
    print(f"El aprendiz aprueba Algoritmia con {defi1} ")
else:
    defi1 < 70
    print (f"El aprendiz reprueba Algoritmia con {defi1} ")
    