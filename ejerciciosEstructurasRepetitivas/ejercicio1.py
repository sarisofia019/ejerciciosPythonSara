'''Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos
neutros'''
# contadores para positivos, negativos y neutros
positivos = 0
negativos = 0
neutros = 0

# Se utiliza el for para hacer un Bucle y leer 20 números
for i in range(20):
    numero = float(input("Ingresa un número: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1

# Imprimimos los resultados
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números neutros:", neutros)
