# Solicitar que digite la edad, sexo y el nivel de hemoglobina
edad = float(input("Ingresa tu edad en años: "))
sexo = input("Ingresa tu sexo (M para masculino, F para femenino): ")
nivHemoglobina = float(input("Ingresa tu nivel de hemoglobina en g%: "))

# se pone la decision para designar el rango de hemoglobina
if edad <= 0.0833: 
    rangoHemoglobina = (13, 26)
elif 0.0833 < edad <= 0.5: 
    rangoHemoglobina = (10, 18)
elif 0.5 < edad <= 1: 
    rangoHemoglobina = (11, 15)
elif 1 < edad <= 5:
    rangoHemoglobina = (11.5, 15)
elif 5 < edad <= 10:
    rangoHemoglobina = (12.6, 15.5)
elif 10 < edad <= 15:
    rangoHemoglobina = (13, 15.5)
elif sexo == "F" or sexo == "f": 
    rangoHemoglobina = (12, 16)
else:
    rangoHemoglobina = (14, 18)

# se inserta la decision para ver si la persona tiene anemia
if nivHemoglobina < rangoHemoglobina[0] or nivHemoglobina > rangoHemoglobina[1]:
    resultado = "positivo"
else:
    resultado = "negativo"

# se imprime el resultado del análisis
print("El resultado del análisis es:", resultado)