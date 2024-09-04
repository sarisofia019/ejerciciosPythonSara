'''La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad
de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo
dígito de la placa de cada carro, se puede determinar el color de la calcomanía
utilizando la siguiente relación:

PLACA  COLOR
1 o 2: amarillo
3 o 4: rosa
5 o 6: roja
7 o 8: verde
9 o 0: azul'''
# Generar contadores para cada color
contarAmarillo = 0
contarRosa = 0
contarRojo = 0
contarVerde = 0
contarAzul = 0

# Solicitar el número total de autos a el usuario
n = int(input("Ingresa el número total de autos: "))

# Generar Bucle para procesar cada auto
for i in range(n):
    ultimoDigito = int(input(f"Ingrese el último dígito de la placa del auto {i + 1}: "))
    
    # Determinar el color de la placa basado en el último dígito
    if ultimoDigito in [1, 2]:
        contarAmarillo += 1
    elif ultimoDigito in [3, 4]:
        contarRosa += 1
    elif ultimoDigito in [5, 6]:
        contarRojo += 1
    elif ultimoDigito in [7, 8]:
        contarVerde += 1
    elif ultimoDigito in [9, 0]:
        contarAzul += 1
    else:
        print("Último dígito no válido. Debe ser un número del 0 al 9.")
        # Volver a ingresar el último dígito de la misma placa en caso de entrada inválida
        i -= 1

# Imprimir resultados
print("Cantidad de autos con calcomanía color amarillo:", contarAmarillo)
print("Cantidad de autos con calcomanía color rosa:", contarRosa)
print("Cantidad de autos con calcomanía color roja:", contarRojo)
print("Cantidad de autos con calcomanía color verde:", contarVerde)
print("Cantidad de autos con calcomanía color azul:", contarAzul)
