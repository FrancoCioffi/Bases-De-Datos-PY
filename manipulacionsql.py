#Ejercicio 1
with open("mi archivo.txt" ,  "w") as arch:
    arch.writelines("Hola, estoy aprendiendo Python")
    
with open("mi archivo.txt" , "r") as arch:
    archivotexto = arch.read()
    print(archivotexto)

# Ejercicio 2

with open('notas.txt', 'w') as arch:
    arch.write("Matemáticas: Me encanta resolver problemas\n")
    arch.write("Ciencias: Me fascina aprender sobre el mundo\n")
    arch.write("Historia: Disfruto conocer el pasado\n")

with open('notas.txt', 'r') as arch:
    lineas = arch.readlines()

for linea in lineas:
    print(linea.strip())


# Ejercicio 3
import sqlite3

conn = sqlite3.connect('escuela.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS alumnos (
                  id INTEGER PRIMARY KEY,
                  nombre TEXT,
                  curso TEXT)''')

cursor.execute("INSERT INTO alumnos (nombre, curso) VALUES ('Franco', 'Matemáticas')")
cursor.execute("INSERT INTO alumnos (nombre, curso) VALUES ('Carlos', 'Ciencias')")
cursor.execute("INSERT INTO alumnos (nombre, curso) VALUES ('Gaspi', 'Historia')")

conn.commit()
conn.close()

