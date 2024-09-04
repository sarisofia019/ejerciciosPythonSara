'''Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se
digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.'''
# Solicitar al usuario que ingrese un número
numero=int(input("Digite el numero el cual desea ver su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar del número ingresado
print(f"Tabla de multiplicar de {numero}:")

# se genera el bucle que realiza la tabla de multiplicacion con el numero dado por el usuario
for i in range(1, 20):  
    producto = numero * i
    print(f"{numero} x {i} = {producto}")
