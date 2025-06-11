import math  # Importamos la librería math para usar funciones matemáticas como pi

# 1. Función que imprime un saludo simple
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función que genera un saludo personalizado con el nombre
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función que imprime información personal del usuario
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4a. Función que calcula el área de un círculo dado su radio
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# 4b. Función que calcula el perímetro de un círculo dado su radio
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Función que imprime la tabla de multiplicar de un número del 1 al 10
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Función que realiza operaciones básicas y retorna una tupla con los resultados
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida"  # Evitamos división por cero
    return (suma, resta, multiplicacion, division)

# 8. Función que calcula el Índice de Masa Corporal (IMC)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Función que convierte grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Función que calcula el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal donde se llaman todas las funciones
if __name__ == "__main__":
    # 1. Hola Mundo
    imprimir_hola_mundo()

    # 2. Saludo personalizado
    nombre = input("\nIngrese su nombre: ")
    print(saludar_usuario(nombre))

    # 3. Información personal
    nombre = input("\nNombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    # 4. Área y perímetro de un círculo
    radio = float(input("\nIngrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

    # 5. Conversión de segundos a horas
    segundos = int(input("\nIngrese la cantidad de segundos: "))
    print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f}")

    # 6. Tabla de multiplicar
    numero = int(input("\nIngrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

    # 7. Operaciones básicas
    a = float(input("\nPrimer número: "))
    b = float(input("Segundo número: "))
    suma, resta, multiplicacion, division = operaciones_basicas(a, b)
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

    # 8. Cálculo del IMC
    peso = float(input("\nIngrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")

    # 9. Conversión Celsius a Fahrenheit
    celsius = float(input("\nIngrese la temperatura en Celsius: "))
    print(f"Temperatura en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")

    # 10. Promedio de tres números
    n1 = float(input("\nIngrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    promedio = calcular_promedio(n1, n2, n3)
    print(f"Promedio: {promedio:.2f}")
