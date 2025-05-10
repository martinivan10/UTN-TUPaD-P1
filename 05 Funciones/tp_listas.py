# Ejercicio 1 Crear una lista con los números del 1 al 100 que sean múltiplos de 4

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

# ----------------------------------------
# Ejercicio 2 Crear una lista con cinco elementos y mostrar el penúltimo
# ----------------------------------------

mi_lista = ['perro', 'gato', 'pájaro', 'pez', 'conejo']
print(mi_lista[-2])

# ----------------------------------------
# Ejercicio 3 Crear una lista vacía, agregar tres palabras con append e imprimirla
# ----------------------------------------

lista_vacia = []
lista_vacia.append('manzana')
lista_vacia.append('banana')
lista_vacia.append('naranja')
print(lista_vacia)

# ----------------------------------------
# Ejercicio 4 Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”
# ----------------------------------------

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# ----------------------------------------
# Ejercicio 5 Explicación del siguiente código:
# ----------------------------------------

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Explicación: El programa busca el número más alto de la lista (max),
# lo elimina con remove() y luego imprime la lista sin ese número. En este caso, elimina el 22.

# ----------------------------------------
# Ejercicio 6 Crear una lista del 10 al 30, saltando de 5 en 5 y mostrar los dos primeros
# ----------------------------------------

numeros = list(range(10, 31, 5))
print(numeros[:2])

# ----------------------------------------
# Ejercicio 7 Reemplazar los valores centrales de la lista autos
# ----------------------------------------

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["mercedes", "audi"]
print(autos)

# ----------------------------------------
# Ejercicio 8 Crear una lista vacía y agregar el doble de 5, 10 y 15
# ----------------------------------------

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# ----------------------------------------
# Ejercicio 9 Modificar la lista compras
# ----------------------------------------

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

# ----------------------------------------
# Ejercicio 10 crear la “lista_anidada”
# ----------------------------------------

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
