'''Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos
números.'''
# Definimos la variable para la suma total
sumaTotal = 0

# Se genera el bucle para leer 10 números negativos
for i in range(10):
    numero = float(input("Ingresa un número negativo: "))
    
    # Convertimos el número negativo a positivo
    if numero < 0:
        numeroPositivo = numero * -1  
        sumaTotal += numeroPositivo  
    else:
        print("El número ingresado no es negativo, por favor ingresa un número negativo.")

# Imprimimos la suma total de los números convertidos
print("La suma de los números convertidos a positivos es:", sumaTotal)
