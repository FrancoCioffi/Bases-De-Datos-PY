#Ejercicio 1
productos = []

while True:
    print("\nMenú de Opciones:")
    print("1. Mostrar lista de productos")
    print("2. Agregar nuevo producto")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        if productos:
            print("\nLista de productos: ")
            for producto in productos:
                print(f"- {producto}")
        else:
            print("\nNo hay productos en la lista.")
    elif opcion == "2":
        nuevo_producto = input("Ingresa el nombre del nuevo producto: ")
        productos.append(nuevo_producto)
        print(f"Producto '{nuevo_producto}' agregado.")
    elif opcion == "3":
        break

#Ejercicio 2
estudiantes = {}

nombre = input("Ingresa el nombre del estudiante: ")
notas = []

for i in range(3):
    nota = float(input(f"Ingresa la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
estudiantes[nombre] = notas

print(f"El promedio de {nombre} es: {promedio:.2f}")

#Ejercicio 3
import sqlite3

conexion = sqlite3.connect('escuela1.db')
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        promedio REAL
    )
''')

cursor.execute("INSERT INTO estudiantes (nombre, promedio) VALUES ('Franco', 8.5)")
cursor.execute("INSERT INTO estudiantes (nombre, promedio) VALUES ('Gaspi', 9.2)")
cursor.execute("INSERT INTO estudiantes (nombre, promedio) VALUES ('Maxi', 7.8)")
conexion.commit()

buscarNombre = input("Ingresa el nombre del estudiante que deseas buscar: ")
cursor.execute("SELECT promedio FROM estudiantes WHERE nombre = ?", (buscarNombre,))
resultado = cursor.fetchone()

if resultado:
    print(f"El promedio de {buscarNombre} es: {resultado[0]}")
else:
    print(f"El estudiante {buscarNombre} no fue encontrado.")

conexion.close()

#Ejercicio 4
with open('notas.txt', 'a') as archivo:
    nombre = input("Ingresa el nombre del estudiante: ")
    promedio = input("Ingresa el promedio del estudiante: ")
    archivo.write(f"{nombre}, {promedio}\n")

with open('notas.txt', 'r') as archivo:
    contenido = archivo.read()
    print("Contenido de notas.txt:")
    print(contenido)

#Ejercicio 5
import sqlite3

conexion = sqlite3.connect('escuela2.db')
cursor = conexion.cursor()

with open('datos_estudiantes.txt', 'w') as archivo:
    archivo.write("Franco, 8.5\n")
    archivo.write("Gaspi, 9.2\n")
    archivo.write("Maxi, 7.8\n")

with open('datos_estudiantes.txt', 'r') as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    nombre, promedio = linea.strip().split(", ")
    cursor.execute("SELECT * FROM estudiantes WHERE nombre = ?", (nombre,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO estudiantes (nombre, promedio) VALUES (?, ?)", (nombre, promedio))

conexion.commit()

cursor.execute("SELECT * FROM estudiantes")
registros = cursor.fetchall()

print("Registros en la base de datos:")
for registro in registros:
    print(registro)

conexion.close()
