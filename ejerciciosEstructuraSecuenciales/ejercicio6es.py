#Desarrolle un algoritmo que permita calcular nota final de algoritmia de un estudiante dadas las siguientes apreciaciones:
# Actividades en clase equivalen a un porcentaje de 30%
# Proyecto final 50%
# Evaluaciones parciales 20%

name=(input("Digite su nombre: "))
#se pide que el aprendiz digite su nombre
califactividades=float(input("Ingrese su calificación promedio de las actividades en clase: (30%) "))
#se crea una variable para solicitar al aprendiz que ingrese su calificación promedio de las actividades en clase
califProyecto=float(input("ingrese su calificaión del proyecto final (50%): "))
#se crea una variable para solicitar al aprendiz que ingrese ingrese su calificación del proyecto final
califEvaluaciones= float(input("ingrese su calificación promedio de las evaluaciones parciales (20%): "))
#se crea una variable para solicitar al aprendiz que ingrese su calificación promedio de las evaluaciones parciales
notaFinal=(califactividades*0.3) + (califProyecto*0.5) + (califEvaluaciones*0.2)
#se declara una variable para calcular la nota final
print("La nota final del aprendiz", name, "en algoritmia es:", notaFinal)
#se imprimen los resultados