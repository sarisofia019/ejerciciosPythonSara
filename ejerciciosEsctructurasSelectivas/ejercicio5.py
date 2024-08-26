edad=int(input("Digita tu edad: "))
sexo=(input("Digita tu sexo(femenino/masculino): "))
#Se le pide al usuario que digite su edad y su sexo
if sexo == "femenino":
  numPulsaciones=(220-edad)/10
  print(f"el número de pulsaciones que debes tener por cada 10 segundos de ejercicio aeróbico son: {numPulsaciones}")
  #Se imprime el número de pulsaciones que debe tener de acuerdo a su edad y si es de sexo femenino
elif sexo == "masculino":
  numPulsaciones=(210-edad)/10
  print(f"el número de pulsaciones que debes tener por cada 10 segundos de ejercicio  aeróbico son: {numPulsaciones}")
  #Se imprime el número de pulsaciones que debe tener de acuerdo a su edad y si es de sexo masculino
else:
    print("sexo no valido")  
    #se imprime si digita un sexo diferente 