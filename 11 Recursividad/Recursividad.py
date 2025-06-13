# 1) Función recursiva para calcular factorial
def factorial(n):
    # Caso base: factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * factorial de n-1
    return n * factorial(n - 1)

# 2) Función recursiva para calcular Fibonacci en la posición n
def fibonacci(n):
    # Casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursión: suma de los dos valores anteriores
    return fibonacci(n - 1) + fibonacci(n - 2)

# 3) Función recursiva para calcular potencia base^exponente
def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Recursión: base * potencia(base, exponente-1)
    return base * potencia(base, exponente - 1)

# 4) Función recursiva para convertir decimal a binario (como cadena)
def decimal_a_binario(n):
    # Caso base especial para n=0
    if n == 0:
        return "0"
    # Caso base para n=1
    if n == 1:
        return "1"
    # Recursión: concatenar resultado de dividir entre 2 y el resto
    return decimal_a_binario(n // 2) + str(n % 2)

# 5) Función recursiva para verificar si una palabra es palíndromo
def es_palindromo(palabra):
    # Caso base: palabra de 0 o 1 caracteres es palíndromo
    if len(palabra) <= 1:
        return True
    # Si el primer y último caracter son diferentes, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    # Recursión: llamar con la palabra sin el primer y último carácter
    return es_palindromo(palabra[1:-1])

# 6) Función recursiva para sumar los dígitos de un número (sin convertir a string)
def suma_digitos(n):
    # Caso base: si es un solo dígito, devuelve el dígito
    if n < 10:
        return n
    # Recursión: último dígito + suma de los demás dígitos
    return (n % 10) + suma_digitos(n // 10)

# 7) Función recursiva para contar bloques en pirámide con n bloques en base
def contar_bloques(n):
    # Caso base: si solo queda un bloque
    if n == 1:
        return 1
    # Recursión: bloques del nivel actual + bloques del resto de la pirámide
    return n + contar_bloques(n - 1)

# 8) Función recursiva para contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    # Caso base: si el número es 0, termina la cuenta
    if numero == 0:
        return 0
    # Extrae el último dígito
    ultimo = numero % 10
    # Suma 1 si coincide con el dígito buscado, más el resultado en el resto del número
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)


# --- Código para probar las funciones ---

# Ejercicio 1: Factorial
limite = int(input("Ingresá un número para calcular factoriales hasta ese valor: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

print("\n")

# Ejercicio 2: Serie de Fibonacci
pos = int(input("Hasta qué posición querés la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")
print("\n")

# Ejercicio 3: Potencia
b = int(input("Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")

print("\n")

# Ejercicio 4: Decimal a binario
numero = int(input("Número decimal para convertir a binario: "))
print(f"Binario: {decimal_a_binario(numero)}")

print("\n")

# Ejercicio 5: Palíndromo
texto = input("Palabra para verificar si es palíndromo (sin espacios ni tildes): ").lower()
print("Es palíndromo" if es_palindromo(texto) else "No es palíndromo")

print("\n")

# Ejercicio 6: Suma de dígitos
numero = int(input("Número para sumar sus dígitos: "))
print(f"Suma de dígitos: {suma_digitos(numero)}")

print("\n")

# Ejercicio 7: Contar bloques pirámide
nivel = int(input("Bloques en el nivel más bajo de la pirámide: "))
print(f"Total de bloques necesarios: {contar_bloques(nivel)}")

print("\n")

# Ejercicio 8: Contar dígito en número
n = int(input("Número donde buscar dígito: "))
d = int(input("Dígito a contar (0-9): "))
print(f"El dígito {d} aparece {contar_digito(n, d)} veces.")
