# ----------------------------------------
# Ejercicio 1: Mayor de edad
# ----------------------------------------
edad = int(input("Ejercicio 1 - Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

# ----------------------------------------
# Ejercicio 2: Aprobado o desaprobado
# ----------------------------------------
nota = float(input("Ejercicio 2 - Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# ----------------------------------------
# Ejercicio 3: Validar número par
# ----------------------------------------
numero = int(input("Ejercicio 3 - Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# ----------------------------------------
# Ejercicio 4: Clasificación por edad
# ----------------------------------------
edad = int(input("Ejercicio 4 - Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# ----------------------------------------
# Ejercicio 5: Validación de contraseña
# ----------------------------------------
contraseña = input("Ejercicio 5 - Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ----------------------------------------
# Ejercicio 6: Análisis de sesgo estadístico
# ----------------------------------------
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Ejercicio 6 - Análisis de sesgo:")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana > moda:
    print("Distribución con sesgo positivo")
elif media < mediana < moda:
    print("Distribución con sesgo negativo")
elif media == mediana == moda:
    print("Distribución sin sesgo")
else:
    print("Distribución no cumple patrón definido")

# ----------------------------------------
# Ejercicio 7: Agregar exclamación si termina en vocal
# ----------------------------------------
texto = input("Ejercicio 7 - Ingrese una frase o palabra: ")
if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)

# ----------------------------------------
# Ejercicio 8: Transformar nombre según opción
# ----------------------------------------
nombre = input("Ejercicio 8 - Ingrese su nombre: ")
opcion = int(input("Ingrese una opción (1: mayúsculas, 2: minúsculas, 3: capitalizado): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")

# ----------------------------------------
# Ejercicio 9: Clasificación de terremoto
# ----------------------------------------
magnitud = float(input("Ejercicio 9 - Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# ----------------------------------------
# Ejercicio 10: Determinar estación según fecha y hemisferio
# ----------------------------------------
hemisferio = input("Ejercicio 10 - Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Convertimos la fecha a un número para comparar fácilmente
fecha = (mes, dia)

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print(f"La estación es: {estacion}")
