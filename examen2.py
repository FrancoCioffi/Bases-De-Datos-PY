#1. Manipulación de Listas y Diccionarios
#Escribe un código en Python que haga lo siguiente:
#o Crea una lista llamada alumnos que almacene al menos ocho nombres de alumnos.
#o Crea un diccionario llamado notas donde cada clave sea un nombre de alumno y el valor sea una lista de seis notas.
#o Calcula el promedio de notas para cada alumno e imprime el nombre del alumno junto a su promedio.
print("CONSIGNA 1")
alumnos = ["Ana", "Carlitos", "Franco", "Maxi", "Gaspar", "Dorrego", "Di Giusto", "Ivan"]

notas = {
    "Ana":[7,8,6,9,10,6],
    "Carlitos":[ 10, 9, 10, 8, 9, 10],
    "Franco":[ 7,8,6,9,10,6 ],
    "Maxi":[ 7,8,6,9,10,6 ],
    "Gaspar":[9, 10, 10, 8, 9, 10],
    "Dorrego":[ 6, 7, 5, 8, 7,6 ],
    "Di Giusto":[ 7,8,6,9,10,6 ],
    "Ivan":[ 6, 7, 5, 8, 7, 6 ]
}
for alumno in alumnos:
    promedio = sum(notas[alumno]) / len(notas[alumno])
    print(f"{alumno}: {promedio:.2f}")

#2. Conexión y manipulación de datos con SQLite
#En Python, realiza los siguientes pasos en SQLite:
#o Conéctate a una base de datos llamada EESTN5.db (si no existe, créala).
#o Crea una tabla llamada alumnos con las columnas id (entero), nombre (texto), y edad (entero).
#o Inserta ocho registros en la tabla con nombres y edades de tu elección.
#o Realiza una consulta que seleccione a todos los alumnos que tengan una edad mayor a 17 años e imprime los resultados.
print("CONSIGNA 2")
import sqlite3
import os
db_name = 'EESTN5.db'

conn = sqlite3.connect('EESTN5.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS alumnos (
                  id INTEGER PRIMARY KEY,
                  nombre TEXT,
                  edad INTEGER)''')

cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES ('Franco', 18)")
cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES ('Carlos', 17)")
cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES ('Gaspi', 19)")
cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES ('Maxi', 18)")
cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES ('Ivan', 17)")
cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES ('Dorrego', 19)")
cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES ('Di Giusto', 18)")
cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES ('Ana', 17)")

conn.commit()

# Consultar alumnos con edad mayor a 17 años
cursor.execute('SELECT * FROM alumnos WHERE edad > 17')
resultados = cursor.fetchall()
for alumno in resultados:
    print(alumno)

conn.close()
if os.path.exists(db_name):
    os.remove(db_name)

#3. Uso de Estructuras de Control
#Realiza un programa en Python que permita al usuario ingresar una lista de calificaciones 
# (usa un bucle para que el usuario ingrese varias calificaciones).
#Luego, muestra la calificación más alta, la más baja y el promedio de todas las calificaciones ingresadas.
print("CONSIGNA 3")
calificaciones = []
cantidad = int(input("Ingrese la cantidad de calificaciones: "))

for i in range(cantidad):
    while True:
        calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
        calificaciones.append(calificacion)
        break

calificacionMaxima = max(calificaciones)
calificacionMinima = min(calificaciones)
promedio = sum(calificaciones) / len(calificaciones)
    
print(f"\nCalificación más alta: {calificacionMaxima}")
print(f"Calificación más baja: {calificacionMinima}")
print(f"Promedio de calificaciones: {promedio:.2f}")

    
