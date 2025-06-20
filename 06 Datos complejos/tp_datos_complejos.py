# 1) Crear un diccionario con precios de frutas y agregar nuevas frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agregamos nuevas frutas al diccionario
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios de frutas existentes

precios_frutas['Banana'] = 1330     # nuevo precio para Banana
precios_frutas['Manzana'] = 1700    # nuevo precio para Manzana
precios_frutas['Melón'] = 2800      # nuevo precio para Melón

# 3) Crear una lista que contenga solo los nombres de las frutas (sin los precios)

solo_frutas = list(precios_frutas.keys())
print("Lista de frutas:", solo_frutas)

# 4) Programa para cargar contactos y consultar números telefónicos

contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero

# Consultar un número telefónico por nombre
consulta = input("¿Qué contacto desea consultar?: ")
if consulta in contactos:
    print("Número:", contactos[consulta])
else:
    print("Contacto no encontrado.")

# 5) Analizar una frase: mostrar palabras únicas y contar ocurrencias

frase = input("Ingrese una frase: ").lower()
palabras = frase.split()

# Crear un set con las palabras únicas
palabras_unicas = set(palabras)

# Crear un diccionario para contar cuántas veces aparece cada palabra
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Recuento de palabras:", recuento)

# 6) Ingresar notas de 3 alumnos y mostrar su promedio

alumnos = {}
for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(int(input(f"Ingrese la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

# Calcular y mostrar el promedio por alumno
print("\nPromedios de los alumnos:")
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: Promedio = {promedio:.2f}")

# 7) Operaciones con sets: estudiantes que aprobaron parciales

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 6, 7}

print("Aprobaron ambos parciales:", parcial1 & parcial2)       # Intersección
print("Aprobaron solo uno:", parcial1 ^ parcial2)              # Diferencia simétrica
print("Aprobaron al menos uno:", parcial1 | parcial2)          # Unión

# 8) Gestión de stock de productos

stock = {"pan": 10, "leche": 5}

producto = input("Ingrese el producto a consultar o agregar: ")

if producto in stock:
    cantidad = int(input("¿Cuántas unidades desea agregar?: "))
    stock[producto] += cantidad
else:
    nuevo_stock = int(input("Producto nuevo. ¿Cuántas unidades tiene?: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# 9) Agenda con claves como tuplas (día, hora)

agenda = {("lunes", "10:00"): "Reunión", ("martes", "15:00"): "Clases de inglés"}

dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (HH:MM): ")

evento = agenda.get((dia, hora), "No hay actividades programadas.")
print("Actividad programada:", evento)

# 10) Invertir un diccionario: claves pasan a ser valores y viceversa

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {capital: pais for pais, capital in original.items()}

print("Diccionario invertido:", invertido)