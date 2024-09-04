'''Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja
de todo el grupo. '''
# Leer la primera calificación para inicializar calificacionAlta y calificacionBaja
calificacion = float(input("Ingrese la  1° calificación del primer alumno: "))

# Inicializar la suma de calificaciones
sumaCalificaciones = 0
calificacionAlta = calificacion
calificacionBaja = calificacion

# Sumar la primera calificación a la suma total
sumaCalificaciones += calificacion

# Bucle para leer las calificaciones de los estudiantes restantes
for i in range(19):
    calificacion = float(input(f"Ingrese la {i+2}° calificación del alumno: "))
    
    # Sumar la calificación a la suma total
    sumaCalificaciones += calificacion
    
    # Actualizar la calificación más alta si la calificación actual es mayor
    if calificacion > calificacionAlta:
        calificacionAlta = calificacion
    
    # Actualizar la calificación más baja si la calificación actual es menor
    if calificacion < calificacionBaja:
        calificacionBaja = calificacion

# Calcular el promedio de los estudiantes
promedio = sumaCalificaciones / 20

# Imprimir resultados de las calificaciones
print("Promedio del grupo:", promedio)
print("Calificación más alta:", calificacionAlta)
print("Calificación más baja:", calificacionBaja)
