'''Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa
se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio
,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos
que tiene una altura menor o igual a 1.50 cm. El programa debe finalizar cuando la edad
sea igual a 0.'''
# Definir contadores y sumas de edades
sumaHombres = 0
sumaMujeres = 0
contadorHombres = 0
contadorMujeres = 0

# Solicitar el número total de alumnos
n = int(input("Ingresa el número total de alumnos: "))

# Bucle para procesar cada alumno
for i in range(n):
    genero = input(f"Ingrese el género del alumno {i + 1} (hombre/mujer): ")
    edad = int(input(f"Ingrese la edad del alumno {i + 1}: "))
    altura = float(input(f"Ingrese la altura del alumno {i + 1}: "))
    # Acumular sumas de edades y contar hombres y mujeres
    if genero == "hombre" or genero == "Hombre":
        sumaHombres += edad
        contadorHombres += 1
    elif genero == "mujer" or genero == "Mujer":
        sumaMujeres += edad
        contadorMujeres += 1
    else:
        print("Género no válido. Debe ser 'hombre' o 'mujer'.")
        # Volver a ingresar los datos del mismo estudiante en caso de un ingreso erroneo
        i -= 1

# Calcular promedios
if contadorHombres > 0:
    promedioHombres = sumaHombres / contadorHombres
else:
    promedioHombres = 0

if contadorMujeres > 0:
    promedioMujeres = sumaMujeres / contadorMujeres
else:
    promedioMujeres = 0

promedioGrupo = (sumaHombres + sumaMujeres) / (contadorHombres + contadorMujeres)

# Imprimir resultados
print("Promedio de edad de los hombres:", promedioHombres)
print("Promedio de edad de las mujeres:", promedioMujeres)
print("Promedio de edad del grupo completo:", promedioGrupo)