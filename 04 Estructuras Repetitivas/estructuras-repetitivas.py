# Ejercicio 1 Programa que imprime los números enteros del 0 al 100, uno por línea

for num in range(101):
    print(num)

# ---------------------------------------------------------
# Ejercicio 2 Solicitar un número entero y mostrar la cantidad de dígitos
# ---------------------------------------------------------

num = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(num)))
print("La cantidad de dígitos en", num, "es:", cantidad_digitos)

# ---------------------------------------------------------
# Ejercicio 3 Suma de enteros entre dos valores dados (excluyendo los extremos)
# ---------------------------------------------------------

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
if num1 > num2:
    num1, num2 = num2, num1
suma = 0
for i in range(num1 + 1, num2):
    suma += i
print("La suma de los números entre", num1, "y", num2, "es:", suma)

# ---------------------------------------------------------
# Ejercicio 4 Sumar números ingresados por el usuario hasta que se ingrese un 0
# ---------------------------------------------------------

suma = 0
while True:
    num = int(input("Ingrese un número entero (0 para salir): "))
    if num == 0:
        break
    suma += num
print("La suma total es:", suma)

# ---------------------------------------------------------
# Ejercicio 5 Juego: Adivinar un número aleatorio del 0 al 9
# ---------------------------------------------------------

import random

numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
        break
    elif intento < numero_aleatorio:
        print("El número es mayor.")
    else:
        print("El número es menor.")

# ---------------------------------------------------------
# Ejercicio 6 Imprimir números pares del 100 al 0 en orden decreciente
# ---------------------------------------------------------

for num in range(100, -1, -1):
    if num % 2 == 0:
        print(num)

# ---------------------------------------------------------
# Ejercicio 7 Suma de números desde 0 hasta un valor ingresado
# ---------------------------------------------------------

num = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(num + 1):
    suma += i
print("La suma de los números entre 0 y", num, "es:", suma)

# ---------------------------------------------------------
# Ejercicio 8 Ingresar 100 números y contar pares, impares, positivos y negativos
# ---------------------------------------------------------

cantidad_pares = 0
cantidad_impares = 0
cantidad_positivos = 0
cantidad_negativos = 0
for i in range(10):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1
    if num > 0:
        cantidad_positivos += 1
    elif num < 0:
        cantidad_negativos += 1
print("Cantidad de números pares:", cantidad_pares)
print("Cantidad de números impares:", cantidad_impares)
print("Cantidad de números positivos:", cantidad_positivos)
print("Cantidad de números negativos:", cantidad_negativos)

# ---------------------------------------------------------
# Ejercicio 9 Ingresar 100 números y calcular la media
# ---------------------------------------------------------

suma = 0
cantidad_numeros = 10
for i in range(cantidad_numeros):
    num = int(input("Ingrese un número entero: "))
    suma += num
media = suma / cantidad_numeros
print("La media de los números ingresados es:", media)

# ---------------------------------------------------------
#Ejercicio 10 Invertir los dígitos de un número
# ---------------------------------------------------------

num = int(input("Ingrese un número entero: "))
inverso = 0
while num > 0:
    digito = num % 10
    inverso = inverso * 10 + digito
    num //= 10
print("El número invertido es:", inverso)