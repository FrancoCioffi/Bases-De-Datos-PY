#Ejercicio 1: Crear una lista de estudiantes con su edad.
#Escribir una función que devuelva el estudiante con mayor y menor edad.
#Ejercicio 2: Crear un diccionario que contenga los nombres de tres productos y su precio. Escribir una función que calcule el total a
# pagar si se compran ciertos productos.
#Ejercicio 3: Crear un programa que permita registrar personas en un diccionario (nombre, edad, correo). Luego, escribir una función
#que filtre a las personas mayores de 18 años.

def edades(edades):
    mayor = edades[0]
    menor = edades[0]
    
    for estudiante in edades[1:]:
        if estudiante["edad"] > mayor["edad"]:
            mayor = estudiante
        if estudiante["edad"] < menor["edad"]:
            menor = estudiante
    
    return mayor, menor
estudiantes = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Carlos", "edad": 22},
    {"nombre": "Franco", "edad": 19},
    {"nombre": "Juan", "edad": 21}
]
mayor, menor = edades(estudiantes)
print(f"1) Estudiante mayor: {mayor['nombre']} ({mayor['edad']} años). Estudiante menor: {menor['nombre']} ({menor['edad']} años)")

def calcular_total(compras):
    total = 0
    for producto, cantidad in compras.items():
        if producto in productos:
            total += productos[producto] * cantidad
    return total
productos = {
    "Carne": 4500,
    "Coca Cola": 2100,
    "Queso Rallado": 1300
}
compras = {
    'Carne': 4,
    'Coca Cola': 2,
    'Queso Rallado': 1
}
total_a_pagar = calcular_total(compras)
print(f"2) El total a pagar es: ${total_a_pagar}")

def registrarPersona(nombre, edad, correo):
    personas[nombre] = {
        'edad': edad,
        'correo': correo
    }

def mostrarMayores():
    mayores = {nombre: info for nombre, info in personas.items() if info['edad'] > 18}
    print("3) Personas mayores de 18 años:")
    for nombre, info in mayores.items():
        print(f"Nombre: {nombre}, Edad: {info['edad']}, Correo: {info['correo']}.")

personas = {}
registrarPersona('Juan', 22, 'ana@gmail.com')
registrarPersona('Franco', 17, 'luis@gmail.com')
registrarPersona('Carlos', 19, 'carlos@gmail.com')

mostrarMayores()




