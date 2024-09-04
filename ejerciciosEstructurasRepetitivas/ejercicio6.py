'''Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un
total de n personas.'''
# Solicitar al usuario el número total de personas en el salón
totalPersonas = int(input("Ingresa el número total de personas en el salón: "))

# Iniciar contadores
cantidadHombres = 0
cantidadMujeres = 0

# Genera el bucle para ingresar y contar el género de cada persona
for i in range(totalPersonas):
    genero = input(f"Ingresa el género de la persona {i + 1} (hombre/mujer): ")

    # Verificar y contar el género
    if genero == "hombre":
        cantidadHombres += 1
    elif genero == "mujer":
        cantidadMujeres += 1
    else:
        print("Género no válido. Por favor ingresa 'hombre' o 'mujer'.")
        # Volver a ingresar el género de la misma persona en caso del ingreso mal de la palabra 
        i -= 1

# Imprimir resultados
print("Cantidad de hombres:", cantidadHombres)
print("Cantidad de mujeres:", cantidadMujeres)
